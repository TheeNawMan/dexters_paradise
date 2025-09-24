import urllib
import requests
import json

aws_access_key_id=""
aws_secret_access_key=""
aws_session_token=""
res = {
    'Credentials': {
        'AccessKeyId': aws_access_key_id,
        'SecretAccessKey': aws_secret_access_key,
        'SessionToken': aws_session_token
    }
}

params = {
        'Action': 'getSigninToken',
        'Session': json.dumps({
            'sessionId': res['Credentials']['AccessKeyId'],
            'sessionKey': res['Credentials']['SecretAccessKey'],
            'sessionToken': res['Credentials']['SessionToken']
    })
}

fed_resp = requests.get(url='https://signin.aws.amazon.com/federation', params=params)

signin_token = fed_resp.json()['SigninToken']

params = {
    'Action': 'login',
    'Issuer': 'imported-default',
    'Destination': 'https://console.aws.amazon.com/console/home',
    'SigninToken': signin_token
}

url = 'https://signin.aws.amazon.com/federation?' + urllib.parse.urlencode(params)

print('[+] Paste the following URL into a web browser to login:')

print(url + "\n")