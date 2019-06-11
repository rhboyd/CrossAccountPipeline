import logging
import boto3
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    print(event)
    s3 = boto3.resource('s3')
    for record in event['Records']:
        object = s3.Object(record['s3']['bucket']['name'], record['s3']['object']['key'])
        if object.ssekms_key_id is not None:
            s3.Object(record['s3']['bucket']['name'], record['s3']['object']['key']).download_file('/tmp/hello.txt')
            s3.Object(record['s3']['bucket']['name'], record['s3']['object']['key']).upload_file('/tmp/hello.txt')
    return
