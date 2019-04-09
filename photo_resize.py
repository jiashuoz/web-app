import boto3
import os
import sys
import uuid
from PIL import Image
from PIL import _imaging
# import Image
     
s3_client = boto3.client('s3')
     
def resize_image_half(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)

def resize_image_quarter(image_path, resized_path):
    with Image.open(image_path) as image:
        image.thumbnail(tuple(x / 4 for x in image.size))
        image.save(resized_path)

     
def resize(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        print(bucket)
        print(key)

        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path_half_thumbnail = '/tmp/resized-half-{}'.format(key)
        upload_path_quarter_thumbnail = '/tmp/resized-quarter-{}'.format(key)

        s3_client.download_file(bucket, key, download_path)
        resize_image_half(download_path, upload_path_half_thumbnail)
        resize_image_quarter(download_path, upload_path_quarter_thumbnail)
        s3_client.upload_file(upload_path_half_thumbnail, '{}resized'.format(bucket), key[0:-4]+'-half-resized.jpg')
        s3_client.upload_file(upload_path_quarter_thumbnail, '{}resized'.format(bucket), key[0:-4]+'-quarter-resized.jpg')