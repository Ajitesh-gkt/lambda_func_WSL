import boto3
from PIL import Image, ImageOps
import io
import math

s3 = boto3.client('s3')

def handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    image_data = response['Body'].read()
    image = Image.open(io.BytesIO(image_data))
    
    # Convert image to grayscale
    grayscale = ImageOps.grayscale(image)
    pixels = grayscale.load()
    
    # Logarithmic enhancement
    for i in range(grayscale.size[0]):
        for j in range(grayscale.size[1]):
            pixels[i, j] = int(255 * math.log1p(pixels[i, j]) / math.log1p(255))
    
    # Save and upload enhanced image
    enhanced_image = io.BytesIO()
    grayscale.save(enhanced_image, format='JPEG')
    enhanced_image.seek(0)
    s3.put_object(Bucket=bucket, Key=f"enhanced-{key}", Body=enhanced_image, ContentType="image/jpeg")
    
    return {"statusCode": 200, "body": "Image processed and uploaded"}