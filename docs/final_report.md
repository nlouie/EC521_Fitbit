### Boston University College of Engineering
### EC521 Cyber Security Project Fall 2016
### Final Report
### Group 3 - Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky
[Fitbit Cyber Project on Github](https://github.com/ssakuma4593/EC521_Fitbit)

### Created: 11/27/16
### Last Updated: 11/27/16

### Background

#### High-level description

Fitbit - Group 3 (Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky)

#### References

##### USB - Inna
- [Sample USB Hack](http://gizmodo.com/hackers-can-wirelessly-upload-malware-to-a-fitbit-in-10-1737880606)

##### Bluetooth - Satoe
- [The Citizen Lab Bluetooth Vulnerability Assessment](https://openeffect.ca/reports/Every_Step_You_Fake.pdf) </br>
Hilts, Andrew (February 2, 2016). Every Step You Fake: A Comparative Analysis of Fitness Tracker Privacy and Security. The Citizen Lab. Retrieved from https://citizenlab.org/2016/02/fitness-tracker-privacy-and-security/
- [Hacktivity: 10 Second Hack] (https://www.framadrive.org/index.php/s/7Xal6WfggnFxSFY) </br>
Avrille, Axelle (October 22, 2015). Fitbits Can be Hacked to Spew Malware, Security Expert Warns. Wired. Retrieved from http://www.wired.co.uk/article/fitbit-hack-malware-ten-seconds
- [Securelist: Hacking Fitbit] (https://securelist.com/blog/research/69369/how-i-hacked-my-smart-bracelet/) </br>
Unucheck, Roman (March 26, 2015). How I Hacked My Smart Bracelet. SecureList. Retrieved from https://securelist.com/blog/research/69369/how-i-hacked-my-smart-bracelet/

##### Android App - Brett
- [Reverse-Engineering an Android App](http://securitywatch.pcmag.com/mobile-security/321138-rsac-reverse-engineering-an-android-app-in-five-minutes)

##### API - Nick

- [Fitbit API Docs](https://dev.fitbit.com/docs/)
- [Terms of use](https://dev.fitbit.com/terms/)
- [Programmable Web Fitbit API](http://www.programmableweb.com/api/fitbit))
- [OWASP API Abuse](https://www.owasp.org/index.php/Category:API_Abuse)
- [Fitbit Scraper Example](https://cran.cnr.berkeley.edu/web/packages/fitbitScraper/)

##### Technical Content

-----------------------------------------------------------------------

#### Fitbit Analysis

Fitbit is a fitness tracker that allows a user to track his/her life with 
the Fitbit's body sensors.

##### Bug Bounty

Fitbit has a [bug bounty program](https://bugcrowd.com/fitbit), but has 
a large amount of restrictions (CSRF, XSS, SQL Injection).These attack vectors being in the OWASP Top 10, it is disappointing that Fitbit would not provide a bug bounty for these vectors since black hats may be less inclined to follow [Fitbit's Terms of Service](https://dev.fitbit.com/terms).
This may hinder white hats from finding vulnerabilities on Fitbit's platform.

The window of compliance between these two sets of restrictions is slim,
and difficult to perform a comprehensive web security analysis. 

[E-Commerce Platform Shopify](https://hackerone.com/shopify) has a much less restrictive bug bounty program, and in fact, encourages SQL Injection, CSRF, and XSS bounties.

##### API Attack Surface

The Fitbit API allows apps to authorize Fitbit users, obtain the user's
Fitbit data, and make changes to the data. The data includes unique information
such as Activity logs, food logs, sleep logs, and heart rate.

The Fitbit API Scraper is proof of concept of the information that an
adversary may obtain upon obtaining Fitbit oauth access. 

##### API Motivation

API Abuse is a common software vulnerability. Thus, vendors must properly
sanitize arbitrary input to their endpoints, implement tokens, and implement
rate limiting in order to limit exploitation attempts. 

Leaked API keys on code repositories such as Github, are common programmer
mistakes. It is common knowledge in the security community, and most
professional programmers that API secrets must be kept, so. This is due to
the prevalence of online bots that crawl Github for an app's published keys
to exploit them.

**The Fitbit API Scraper is an example of the data extraction process given
the user's access codes, and the Fitbit app secret.** 

##### API Elevation
There are various ways to obtain a user's account access.
This implies that adversary is able to trick the user into authorizing 
his/her Fitbit account. We have not found any novel way for an adversary 
to do this. The attacker would have to resort to traditional social
engineering methods such as phishing. 

CSRF is always a possibility as well, especially since the app owner
controls the redirect URL. If a CSRF vulnerability is found, the malicious
app owner may be able to use Javascript to login to a user's Fitbit without
the account owner's permission.

but!

**Fitbit bans apps trying to perform a CSRF attack on Fitbit's platform!**

or so they say. We did not test for these in order to comply with the tos.

OAuth2 is the same protocol as "Sign in with Facebook/Google/etc", so if
an attacker could compromise oauth, the attacker would compromise all
similar authentication.

####  Fitbit OAuth Login

Users must be presented with either the option to create a Fitbit Account, 
which will direct them to Fitbit.com, or to login to their Fitbit account 
using Fitbit's [OAuth](https://dev.fitbit.com/docs/oauth2/) protocol.

Fitbit uses OAuth 2.0 for user authorization and API authentication. 
The OAuth 2.0 framework requires your application to obtain an Access 
Token when the Fitbit user authorizes your app to access their data. 
The Access Token is used for making HTTP request to the Fitbit API.

##### Authorization Grant Flow

Our Fitbit Scraper Uses Authorization Code Grant Flow (AGF). 
Tokens from this method are short lived, and thus recommended for Web Applications. 

We use AGF in order to stay within the API guidelines that the tokens 
will be used for an actual application. 

Our Fitbit App is [Judgemental Mom](http://github.com/nlouie/judgemental-mom), a social media analyzer that Nick is currently creating with another group in (BU CAS CS411 Fall 2016).

The only ties this project has with JM is the redirect URI and the API 
app request reason.


##### Implicit Grant Flow
Implicit Grant flow is for apps without a webservice.

From Fibit:
> Unlike the Authorization Code Grant Flow, the refresh tokens are not issued with the Implicit Grant flow. Refreshing a token requires use of the client secret, which cannot safely be stored in distributed application code. When the access token expires, users will need to re-authorize your app.

> Access tokens from the Implicit Grant Flow are longer lived than tokens from the Authorization Code Grant flow. Users may specify the lifetime of the access token from the authorization page when an application uses the Implicit Grant flow. The access token lifetime options are 1 day, 1 week, and 30 days. Applications can pre-select a token lifetime option, but the user ultimately decides.

This method would be preferred for a malicious actor. One could have a
much longer lived access token as well as [subscribe](https://dev.fitbit.com/docs/subscriptions/) to user updates in order to maintain persistence.

We choose not to implement this method in order not cross the ethical guidelines set forth by Fitbit. Judgemental Mom is a legitimate app that collects and analyzes user data and returns a report, thus we are using the Fitbit API token in compliance with:

> Fitbit Data may be used solely as necessary to provide your Application to end users. You may make no further use of the Fitbit Data without express User consent.

####  Python Fitbit Oauth

[\[Fitbit\] Fitbit Api Access using Oauth2.0](http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html)

[Fitbit Scraper Example](https://cran.cnr.berkeley.edu/web/packages/fitbitScraper/)

#### Data Collection

Info an app could get about a user:

- Activity 
- Body Fat
- Food 
- Friends
- Heart rate logs
- Sleep Logs

User Friends JSON example
```
{
    "friends":[
        {
            "user":
                {
                    "aboutMe":"I live in San Francisco.",
                    "avatar":"http://www.fitbit.com/images/profile/defaultProfile_100_male.gif",
                    "city":"San Francisco",
                    "country":"US",
                    "dateOfBirth":"1970-02-18",
                    "displayName":"Nick",
                    "encodedId":"257V3V",
                    "fullName":"Fitbit",
                    "gender":"MALE",
                    "height":176.7,
                    "nickname":"Nick",
                    "offsetFromUTCMillis":25200000,
                    "state":"CA",
                    "strideLengthRunning":0,
                    "strideLengthWalking":0,
                    "timezone":"America/Los_Angeles",
                    "weight":80.5
                }
         ]}

 }
```


-------------------------------------------------------------------------


##### Limitations

- The attacker would have to resort to traditional social
engineering methods such as phishing to gain API access.

##### Results

#### Privacy Implications

The privacy implications of fitness trackers have not been evaluated as
much as older technologies have.

With access to a user's heart-rate logs over time, an app could detect
for heart abnormalities or more maliciously, an advertising agency
may be able to use heart rate patterns to fingerprint a user between devices.

**As we attach ourselves to more bodily sensors, we expose more personal
information online.** Personal information has been the new goldmine of the
21st century, as seen by an overwhelming majority of technology companies
 such as Google, Facebook, Amazon, etc...

##### Implications (besides access to basic user info)

    - Targeted advertising for medications based on user's heart rate and/or weight
    - Knowledge of possible heart conditions.
    - Heart Rate "Fingerprinting"
    - A user's habits are valuable information for criminals (activity and sleep logs)
    - Targeted advertising based on user's foods.
    - What the user eats => What the user does **not** eat. Knowledge of diet restrictions is valuable information.

### Materials

#### Requirements

- `Python 3.5`
- A Fitbit account

#### Usage

**Click the link below and look at your URL header for the code=..., then paste that into fitbit.CODE**

1. First, Click the below Authorization URL:

`https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800`

or make a curl

`curl -X POST -i -H 'Authorization: Basic MjI4MzQ5OjdkMzJmMDMwNzRhMmQ5ODJkNjM3ZjhhYjFhZjBiNmZl' -H 'Content-Type: application/x-www-form-urlencoded' -d "clientId=228349" -d "grant_type=authorization_code" -d "redirect_uri=https%3A%2F%2Fjudgementalmom.com%2Ffitbit" -d "code=0716ea988383f3c400e21adbfe70902293218dcc" https://api.fitbit.com/oauth2/token`

The authorization links to my shared web hosting, but will return a 500 error.
**Look at your URL header to see your code!!!**
I don't collect your information! By running the script you are collecting your own information.
Proof is that your oauth wouldn't work if I did try to authorize as you (within the expiration time)
That is, unless a MITM sends you an alternate, working key...

*You can change the redirect URL if you would like.*

2. **Copy the code into the variable CODE in fitbit.py**

3. Run fitbit.py

`python fitbit.py`

You should see the extraction results in output.txt and in your console.

If you recieve an error with oauth then the token may be expired.
    
##### Disclaimer 

This is for use by Team members only. If you would like to use this for your own Fitbit app, simply replace your authorization code in global_headers,
and your redirect_uri in oauth_request_data.

When you run this, you are using this script at your own discretion. We hold no warranty for this script. If you are not redirecting to a secure server (if no https), then you may expose your sensitive information because this app requests for a maximum amount of informational access to your Fitbit account. If you redirect to an unencrypted connection, there is absolutely no guarantee of privacy.

Works only for authorization code flow!

##### Conclusions

Fitbit should be more open to bug bounty collectors, otherwise malicious actors may exploit vulnerabilities instead. Fitbit brushes off "[theoretical vulnerabilities](https://community.fitbit.com/t5/Fitbit-com-Dashboard/Theoretical-bluetooth-vulnerability/td-p/995475)," which does not instill confidence in its security policies. Not enough people care about the personal information they are sending when using a wearable. The information can be used to fingerprint your future movements.



#### Bluetooth Attack Surface
Similar to the API Attack Surface, spoofing bluetooth pairing between a Fitbit device and a laptop or mobile will allow the attacker to have access to vital signs, calories burned, sleep activity, geolocation, phone serial number IMEI Number, steps per interval, and 
reproductive health information. 

#### Bluetooth Motivation
The attacker that has paired to the victim's Fitbit through bluetooth, they can gather information on the victim, but also manipulate the information stored on the device. Although damage is minimal, information leaks still violate users' prviacy.

Bluetooth is most vulnerable for exploitation when it is not paired. Users may be trying to save battery or assume that once the Fitbit device is done syncing, they do not need to keep bluetooth enabled. However, the Fitbit device will revert to "advertising mode" and repeatedly emits a fixed signal and unique ID to alert the phone that it is waiting to re-establish a connection. During this 'advertising mode,' attackers are free to pair with the device and cause disturbance in re-establishing connection with the users' device. 

#### Bluetooth Hacking

##### Scanning
Unucheck used ready code from Android SDK, which is an application to connect to Bluetooth LE devices. 
Kali Linux comes with Bluesnarfer, which scans bluetooth devices. This can be done with a bluetooth dongle by:

    -hciconfig hci0
    -hcitool scan hci0
    -l2ping (device addr)

##### Authentication
In the real authentication process between the Fitbit device and the user, the Fitbit application uses one of the four service located in the wristband. To notify the Fitbit device of any changes made to the characteristic, each characteristic has a flag called 'CharacteristicNotification'. This also goes for the descriptors for each characteristics, with the flag 'ENABLE_NOTIFICATION_VALUE' .

When one of the characteristics' value is changed through the byte buffer, the application reads the buffer containing the header and byte array and initializes a new array. This new array consists of a constant array within the application, followed by the header and byte array that it read from the buffer. The new array is MD5 hashed and sent to the Fitbit device, to which the device responds in this format.

    -Header
    -MD5
    -Verification byte

This will cause the Fitbit Device to vibrate and request the user to tap the screen to finish the authentication. Due to the fact that authentication requires just one tap from the user, one attack method could be to repeatedly try the authentication process within range. 

After the authentication is complete, data on the Fitbit device can be accessed. However, something to note is that once an hour the device transfers information to the cloud, which means some of the information going back may not be accessible.

##### Potential Malicious Actions
Aside from modifying data of steps and distances, Avrille claimed as a proof of concept that the atacker could inject a malicious code into the tracker which only required 10 seconds, with an verification time of 60 seconds (timed to a jog of the victim). Only the initial injection requires that the Fitbit device be near the attacker. The verification can happen even when the victim is out of reach. 

When the victim wants to syncrhonize their data to update their profile, the device will respond. However, added to the original message, the response will be infiltrated with the infected packet, which will then be delivered to the victim's laptop or mobile device. This could then start a back door and even infect other trackers. 

Although the payload is small, just a mere 17 bytes, it is enough for a Trojan such as the Crash Pentium Trojan in 2004, which only required 4 bytes. 

#### Fitbit's Reponse
Fitbit claimed that these claims were false and cannot be reproduced.

>On Wednesday October 21, 2015, reports began circulating in the media based on claims from security vendor, Fortinet, that Fitbit devices could be used to distribute malware. These reports are false. In fact, the Fortinet researcher, Axelle Apvrille who originally made these claims has confirmed to Fitbit that this was only a theoretical scenario and is not possible. Fitbit trackers cannot be used to infect user’s devices with malware. We want to reassure our users that it remains safe to use their Fitbit devices and no action is required.


