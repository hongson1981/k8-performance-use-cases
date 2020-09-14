# Information about S3 Presigned URL for download and upload #12

## Prerequisites
	install boto3 :
	 $ pip install boto3
	install requests: 
	 $ pip install requests
	Prepare AWS items below :
	 AWS access key
	 AWS secret key
	 S3 bucket name
	 S3 bucket region
## Usage

### Create session to connect to AWS S3
	
	session = Session(aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
	
### Create S3 client based on session
	
	s3_client=session.client('s3')

### Get URL to download file

	url = create_presigned_url(s3_client,BUCKET_NAME, FILE_NAME, expiration)

### Get URL to upload file
	
	url = create_presigned_post(s3_client,BUCKET_NAME, FILE_NAME, fields, conditions, expiration)
	
### Test 
	
	Refer python code



## License
MIT License
See: LICENSE
