#!/usr/bin python3

# Code to generate a GitLab personal access token for a self-hosted GitLab install
import requests, sys

GITLAB_URL = 'https://git.r4n0k.com'
GITLAB_USERID = '2'
GITLAB_TOKEN = 'glpat_XYZ'

def call_gl_api(method, base_url, api_func, token, data = None):
    headers = {'PRIVATE-TOKEN': token}
    if method == 'GET':
        req = requests.get(base_url + '/api/v4/' + api_func, headers=headers, data=data)
        #print(req.status_code)
        return req.json()
    elif method == 'POST':
        req = requests.post(base_url + '/api/v4/' + api_func, headers=headers, data=data)
        #print(req.status_code)
        return req.json()

def generate_pat(tokenvalue):
    '''Issues a GitLab API request as an admin user to generate a PAT for the USERID being monitored'''
    data = {'name': tokenvalue, 'scopes[]': 'api,read_repository'}
    tokc = call_gl_api('POST', GITLAB_URL, 'users/' + str(GITLAB_USERID) + '/personal_access_tokens', GITLAB_TOKEN, data=data)
    token = tokc.get('token', None)
    if token != None:
        return token.encode('ascii')
    return ''

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Please call with a GitLab URL, uid, creator token, and token_name")
        sys.exit(-1)
    GITLAB_URL = sys.argv[1]
    GITLAB_USERID = sys.argv[2]
    GITLAB_TOKEN = sys.argv[3]
    print(generate_pat(sys.argv[4]))