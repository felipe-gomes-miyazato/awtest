import boto3
import json
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')

# Get JSON file from source bucket
file = s3.get_object(Bucket='felipe-gomes-miyazato-bucket', Key='random_data.json')
file_content = file["Body"].read().decode('utf-8')
data = json.loads(file_content)

df = pd.DataFrame(data)

csv_buffer = StringIO()
df.to_csv(csv_buffer)

s3.put_object(Body=csv_buffer.getvalue(), Bucket='picsel-case-analytics', Key='output_json')