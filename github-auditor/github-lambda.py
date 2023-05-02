#!/usr/bin/env python3

import json, gzip
import urllib.parse
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        logdata = []
        logs = gzip.decompress(response['Body'].read()).decode('utf-8').split("\n")
        for l in logs:
            logdata.append(json.loads(l))
        for ld in logdata:
            print("Action: " + ld['action'] + ' Token: ' + ld.get('hashed_token', "None") + ' IP: ' + ld.get('actor_ip', 'Unknown'))
        return str(len(logdata))
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
