from boto3 import Session
from botocore.exceptions import ClientError
from pip._internal.utils import logging
import requests

ACCESS_KEY = "your access key"
SECRET_KEY = "your_secret_key"
REGION_NAME = "your bucket's region name"
BUCKET_NAME = "your bucket name"

def create_presigned_url(s3_client,bucket_name, object_name, expiration):
    """Generate a presigned URL to share an S3 object
    :param:s3_client : s3 client object
    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response
def create_presigned_post(s3_client, bucket_name, object_name,
                          fields, conditions, expiration):
    """Generate a presigned URL S3 POST request to upload a file
    :param s3_client: S3 client object
    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response

#Create session to connect to AWS S3
session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
#Create S3 client based on session
s3_client=session.client('s3')

#Test create_presigned_url to download file
file = 'test.7z'
expiration=3600
conditions = None
fields = None
url = create_presigned_url(s3_client,BUCKET_NAME,file,expiration)
print('Get url: ',url)

#Test create_presigned_post to upload file
file = 'test2.7z'
url = create_presigned_post(s3_client,BUCKET_NAME,file,fields,conditions,expiration)
print('Post url: ',url) #copy printed url and paste to any browser to download file

object_name=file
response=url
with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(response['url'], data=response['fields'], files=files)
# If successful, returns HTTP status code 204
print(f'File upload HTTP status code: {http_response.status_code}')
