import json

def handler(event, context):
    # Parse the input from JSON
    n = event.get("n", 0)
    
    if not isinstance(n, int) or n < 0:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid input. Please provide a non-negative integer."})
        }
    
    # Generate Fibonacci numbers up to n
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    
    # Return the sequence as a JSON response
    return {
        "statusCode": 200,
        "body": json.dumps({"fibonacci": fib_sequence})
    }
