import json
import boto3

def detect_labels(bucket,imageFile):

    session = boto3.Session()
    client = session.client('rekognition')
     
    s3 = boto3.resource('s3')
    s3_object = s3.Object(bucket, imageFile)
    image = s3_object.get()['Body'].read()

    response = client.detect_labels(Image={'Bytes': image},MaxLabels=20)

    print('Detected labels for ' + imageFile)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))


def lambda_handler(event, context):
    
    bucket = 'video-000110-bucket'
    imageFile = 'video-001102/Surfing-Wave.png'
    detect_labels(bucket,imageFile)

    # Return success
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Execution of Lambda')
    }
