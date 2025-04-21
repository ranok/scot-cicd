#!/usr/bin/env python3

import requests, sys, json, tempfile
from typing import Optional, Dict

TOKENS_URL='https://canarytokens.org'

def _gen_req_data(type: str, email: str, memo: str) -> Dict[str, str]:
    return {
        'type': type,
        'email': email,
        'memo': memo,
        'fmt': '',
        'webhook': '',
        'redirect_url': '',
        'cmd_process': '',
        'azure_id_cert_file_name': '',
        'clonedsite': '',
        'sql_server_table_name': 'TABLE1',
        'sql_server_view_name': 'VIEW1',
        'sql_server_function_name': 'FUNCTION1',
        'sql_server_trigger_name': 'TRIGGER1'
    }

def get_web_token(email : str, memo : str) -> Optional[str]:
    '''
    Returns a web bug token URL given an email and memo
    '''
    req_data = _gen_req_data('web', email, memo)
    res = requests.post(TOKENS_URL + '/generate', data=req_data)
    if res.status_code != 200:
        return None
    return res.json().get('token_url', None)

def get_aws_token(email : str, memo: str) -> Optional[Dict[str, str]]:
    '''
    Returns a dict of an AWS access key given an email and memo
    '''
    req_data = _gen_req_data('aws_keys', email, memo)
    res = requests.post(TOKENS_URL + '/generate', data=req_data)
    if res.status_code != 200:
        return None
    return {'access_key': res.json().get('aws_access_key_id'), 'secret_key': res.json().get('aws_secret_access_key')}

def get_ms_word_token(email : str, memo : str) -> Optional[str]:
    '''
    Generates a MS word token and returns the temporary file name
    '''
    req_data = _gen_req_data('ms_word', email, memo)
    res = requests.post(TOKENS_URL + '/generate', data=req_data)
    if res.status_code != 200:
        print("Error generating token")
        print(res.text)
        return None
    tf = tempfile.NamedTemporaryFile(suffix='.docx', delete=False)
    dl = requests.get(TOKENS_URL + '/download', params={'fmt': 'msword', 'auth': res.json().get('auth_token', ''), 'token': res.json().get('token', '')}, stream=True)
    tf.write(dl.content)
    name = tf.name
    tf.close()
    return f'Downloaded token to: {name}'

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Please call with type (web, aws, msword), email, and memo")
        sys.exit(-1)
    if sys.argv[1] == 'web':
        print(get_web_token(sys.argv[2], sys.argv[3]))
    elif sys.argv[1] == 'aws':
        print(json.dumps(get_aws_token(sys.argv[2], sys.argv[3])))
    elif sys.argv[1] == 'msword':
        print(get_ms_word_token(sys.argv[2], sys.argv[3]))
    else:
        print("Please call with type (web, aws, msword), email, and memo")
        sys.exit(-1)
