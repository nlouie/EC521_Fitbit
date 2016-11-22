"""
curl -X POST -i -H 'Authorization: Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl' -H 'Content-Type: application/x-www-form-urlencoded' -d "clientId=228349" -d "grant_type=authorization_code" -d "redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit" -d "code=0716ea988383f3c400e21adbfe70902293218dcc" https://api.fitbit.com/oauth2/token


User clicks below link and authorizes, the user is directected with a code in the get request with which the server uses
to make a post request to authorize the app. Fitbit responds to the post request with the user's access and refresh token.
After that, the server now has access to the user's data.

https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800

https://dev.fitbit.com/docs/oauth2/

"""

import requests
from json import load

# authenticate

# secrets
code = "XXXXXXXXXXXXXXXXXXXXX"
client_secret = load(open('auth.json','r'))['fitbit-secret']

# urls

# Use this URL to refresh the access token
TokenURL = "https://api.fitbit.com/oauth2/token"

global_headers = {
    'Authorization': 'Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl',
    'Content-Type': 'application/x-www-form-urlencoded',
}

oauth_request_data = {
  'clientId': '228349',
  'grant_type': 'authorization_code',
  'redirect_uri': 'https://judgementalmom.com/fitbit',
  'code': code
}

extraction_urls = {
    'user_data': 'https://api.fitbit.com/1/user/{0}/profile.json',
    'body_data': 'https://api.fitbit.com/1/user/{0}/body/log/fat/date/2016-10-30.json',
    'devices_data': 'https://api.fitbit.com/1/user/{0}/devices.json',
    'weight_data': 'https://api.fitbit.com/1/user/{0}/body/log/weight/date/2016-10-30.json',
}


extracted_data = {}


def getNewAccessToken(refresh_token):
    data = {'grant_type': 'refresh_token',
            'refresh_token': refresh_token}
    r = requests.post(TokenURL, headers=global_headers, data=data)
    access_token = r.json()['access_token']
    refresh_token = r.json()['refresh_token']
    return access_token, refresh_token


def getData(url, user_id, headers, data, name):
    r = requests.get(url.format(user_id), headers=headers, data=data)
    if r.status_code is 200 and 'errors' not in r.json():
        extracted_data[name] = r.json()


def extract_new(access_token, refresh_token, user_id):

    for key in extraction_urls:
        # set up the request

        # default headers and data
        headers = {'Authorization': 'Bearer ' + str(access_token)}
        data = {}
        url = extraction_urls[key]
        # make the request
        getData(url, user_id, headers, data, name=key)

        # reset
        # refresh the token and refresh the headers
        access_token, refresh_token = getNewAccessToken(refresh_token)
        headers = {'Authorization': 'Bearer ' + str(access_token)}


def extract(access_token, refresh_token, user_id):
    # extract
    # https://dev.fitbit.com/docs/oauth2/#making-requests

    # default headers and data
    headers = {'Authorization': 'Bearer ' + str(access_token)}
    data = {}

    # extract user data
    url = extraction_urls['body_data']
    getData(url, user_id, headers, data, 'user_data')

    # refresh the token
    new_access_token, new_refresh_token = getNewAccessToken(refresh_token)
    headers = {'Authorization': 'Bearer ' + str(new_access_token)}

    # extract body data logs
    url = extraction_urls['body_data']
    getData(url, user_id, headers, data, 'body_data')

    # refresh the token and refresh the headers
    access_token, refresh_token = getNewAccessToken(refresh_token)
    headers = {'Authorization': 'Bearer ' + str(new_access_token)}

    # extract devices data
    url = 'https://api.fitbit.com/1/user/{0}/devices.json'
    getData(url, user_id, headers, data, 'devices_data')

    # refresh the token and headers
    access_token, refresh_token = getNewAccessToken(refresh_token)
    headers = {'Authorization': 'Bearer ' + str(new_access_token)}

    # get weight logs
    url = 'https://api.fitbit.com/1/user/{0}/body/log/weight/date/2016-10-30.json'
    getData(url, user_id, headers, data, 'weight_data')

    # refresh the token and headers
    access_token, refresh_token = getNewAccessToken(refresh_token)
    headers = {'Authorization': 'Bearer ' + str(new_access_token)}


def main():
    r = requests.post(TokenURL, headers=global_headers, data=oauth_request_data)
    oauth_data = r.json()
    if 'errors' not in oauth_data:
        access_token = oauth_data['access_token']
        user_id = oauth_data['user_id']
        refresh_token = oauth_data['refresh_token']
        extract(access_token, refresh_token, user_id)
        print(extracted_data)
    else:
        print('error in oauth', oauth_data)


main()


