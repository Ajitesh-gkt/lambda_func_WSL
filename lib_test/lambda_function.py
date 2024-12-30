import numpy as np
import pandas as pd
import json

def lambda_handler(event, context):
    pandas_version = pd.__version__
    numpy_version = np.__version__

    return_statement = f"Pandas version: {pandas_version}, Numpy version: {numpy_version}"
    return{
        'statusCode': 200,
        'body': json.dumps(return_statement)
    }