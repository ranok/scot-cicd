#!/usr/bin/env python3

import json
import requests
from datetime import timedelta, datetime

BASE_URL = 'https://git.r4n0k.com'
CT_URL = 'https://canarytokens.org'
PULL_UID = 6

def call_gl_api(method, base_url, api_func, token, data = None):
    if method == 'GET':
        headers = {'PRIVATE-TOKEN': token}
        req = requests.get(base_url + '/api/v4/' + api_func, headers=headers, data=data)
        print(req.status_code)
        return req.json()

def alert_on_token_use(json_data):
    alerts = 0
    for token in json_data:
        if token.get('id') == PULL_UID: # This is the token used to pull token info
            continue
        if token.get('last_used_at') != None:
            print('Token ' + token.get('name') + ' was last used at: ' + token.get('last_used_at'))
            requests.get(CT_URL + '/' + token.get('name'))
            alerts += 1
    return alerts

def lambda_handler(event, context):
    tc = 'glpat-XYZ'
    last_two = (datetime.now() - timedelta(minutes=10)).isoformat()
    tokens = call_gl_api('GET', BASE_URL, 'personal_access_tokens?last_used_after=' + last_two, tc)
    alerts = alert_on_token_use(tokens)
    return {
        'statusCode': 200,
        'body': json.dumps('Reported on ' + str(alerts) + ' tokens used!')
    }
