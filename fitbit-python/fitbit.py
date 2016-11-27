"""
fitbit.py
BU EC521
nlouie@bu.edu

This script takes the authorized fitbit user code and scrapes the user's data by making a series of GET requests.
This is *proof of concept* of various data one could take from a fitbit account.

An added proof would be to host this script, but may be against Fitbit API's TOS.

User clicks below link and authorizes, the user is directected with a code in the get request with which the server uses
to make a post request to authorize the app. Fitbit responds to the post request with the user's access and refresh token.
After that, the server now has access to the user's data.

Works only for authorization code flow!

The authorization links to my shared hosting, but will return a 404.

Authorization URL:

https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800

or make a curl

curl -X POST -i -H 'Authorization: Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl' -H 'Content-Type: application/x-www-form-urlencoded' -d "clientId=228349" -d "grant_type=authorization_code" -d "redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit" -d "code=0716ea988383f3c400e21adbfe70902293218dcc" https://api.fitbit.com/oauth2/token

More info about authentication:

https://dev.fitbit.com/docs/oauth2/

"""


# -------------------- IMPORTS --------------------------------------------#

import requests
from json import load


# --------------------- GLOBALS --------------------------------------------#

# final extracted returned data
FINAL_OUTPUT = {}

# Build authentication POST

# secrets are no fun
code = "7e68eacf8234b7d7717162822fe4e6c66a0dabb6"
client_secret = load(open('auth.json', 'r'))['fitbit-secret']

# Use this URL to refresh the access token
TokenURL = "https://api.fitbit.com/oauth2/token"

global_headers = {
    'Authorization': 'Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl',
    'Content-Type': 'application/x-www-form-urlencoded',
}

oauth_request_data = {
  'clientId': load(open('auth.json', 'r'))['client-id'],
  'grant_type': 'authorization_code',
  'redirect_uri': 'https://judgementalmom.com/fitbit',
  'code': code
}

# All the api endpoints for extraction of user data. note that we are using a static date, 2016-10-30 for proof
# of concept and simplicity, but one could obtain the date the user signed up and request the range between then and
# now in order to obtain all the user's data.
# It's important to note that the [user-id] area of the url must be replaced with {0} in order to be compatible with the
# string formatting done in getData().
# By adding the name and api endpoint url, the extraction function will automatically extract the user's data from the
# provided endpoint
EXTRACTION_URLS = {
    'user_data': 'https://api.fitbit.com/1/user/{0}/profile.json',
    'body_data': 'https://api.fitbit.com/1/user/{0}/body/log/fat/date/2016-10-30.json',
    'devices_data': 'https://api.fitbit.com/1/user/{0}/devices.json',
    'weight_data': 'https://api.fitbit.com/1/user/{0}/body/log/weight/date/2016-10-30.json',
    'food_data': 'https://api.fitbit.com/1/user/{0}/foods/log/date/2016-10-30.json',
    'friends_data':'https://api.fitbit.com/1/user/[user-id]/friends.json',
}


# ----------------- FUNCTIONS --------------------------------------------#


def get_new_access_token(refresh_token):
    """
    after using an access token, we must request another one using the refresh token that we already have.
    :param refresh_token: str ref
    :return: str, str
    """
    data = {'grant_type': 'refresh_token',
            'refresh_token': refresh_token}
    r = requests.post(TokenURL, headers=global_headers, data=data)
    access_token = r.json()['access_token']
    refresh_token = r.json()['refresh_token']
    return access_token, refresh_token


def get_data(url, user_id, headers, data, name):
    """
    Makes the request and puts it into the final output
    :param url: api endpoint
    :param user_id: fitbit user id
    :param headers: header with a fresh access token
    :param data: should be empty dictionary
    :param name: name of data as defined in EXTRACTION_URLS keys
    :return: None
    """
    r = requests.get(url.format(user_id), headers=headers, data=data)
    if r.status_code is 200 and 'errors' not in r.json():
        FINAL_OUTPUT[name] = r.json()


def extract(access_token, refresh_token, user_id):
    """
    Sets up the url requests, calls get_data()
    :param access_token: fresh access token
    :param refresh_token: fresh refresh token
    :param user_id: fitbit user id
    :return: None
    """
    # default headers and data
    headers = {'Authorization': 'Bearer ' + str(access_token)}
    data = {}
    # Make a call for each API endpoint
    for key in EXTRACTION_URLS:
        # set up the request
        url = EXTRACTION_URLS[key]
        # make the request
        get_data(url, user_id, headers, data, name=key)
        # reset
        # refresh the token and refresh the headers
        access_token, refresh_token = get_new_access_token(refresh_token)
        headers = {'Authorization': 'Bearer ' + str(access_token)}


def main():
    r = requests.post(TokenURL, headers=global_headers, data=oauth_request_data)
    oauth_data = r.json()
    if 'errors' not in oauth_data:
        access_token = oauth_data['access_token']
        user_id = oauth_data['user_id']
        refresh_token = oauth_data['refresh_token']
        extract(access_token, refresh_token, user_id)
        print(FINAL_OUTPUT)
    else:
        print('error in oauth', oauth_data)


main()


