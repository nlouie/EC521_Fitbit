### Boston University College of Engineering
### EC521 Cyber Security Project Fall 2016
### Final Report
### Group 3 - Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky
[Fitbit Cyber Project on Github](https://github.com/ssakuma4593/EC521_Fitbit)

### Created: 11/27/16
### Last Updated: 12/12/16

### Background

#### High-level description

Fitbit - Group 3 (Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky)

Fitness trackers are an advent of the emerging field of technology wearables and the internet of things.
Within the competitive market of the IoT, firms typically skimp on security by concentrating resources towards functionality.
Fitbit is no different in this sense, and must be assumed to have undisclosed security vulnerabilities that may compromise
its users' privacy. Compared to most IoT devices such as the common IP Camera, the Fitbit is worn constantly, and contains
several sensors to track one's movements. We believe the attack surface of fitness trackers is comparable to that of a
smart phone, but is not as extensively evaluated for security vulnerabilities for many reasons.

We have created a security assessment of possible attack vectors on the health wearable, the Fitbit. We focus on the
vulnerabilities surrounding information gathering through API exploitation, and also touch upon other Fitbit attack vectors
such as Bluetooth connectivity, USB connectivity, and the Fitbit Android Application. We wish to analyze potential avenues
for attack of the Fitbit devices, and its privacy implications to its users.

We have created a demonstration involving Fitbit API data scraping. The Fitbit collects a plethora of information from
its body sensors. We have learned in Android Security that these body sensors leak a great deal of information. Luckily,
Fitbit keeps most of this information (not real-time), and allows apps to access the data upon a user's consent.

We consider the Fitbit API research to be an extension of "Security Analysis of Wearable Fitness Devices (Fitbit)" by
Britt Cyr, Webb Horn, Daniela Miao, and Michael Specter  at Massachusetts Institute of Technology Cambridge, which can be
found in our searches. The MIT research mentioned API vulnerabilities as an area of study that was not evaluated.

#### References and Resources

##### USB - Inna
- [Sample USB Hack](http://gizmodo.com/hackers-can-wirelessly-upload-malware-to-a-fitbit-in-10-1737880606)
- [Fortinet's Research](https://www.engadget.com/2015/10/21/fitbit-tracker-bluetooth-vulnerability/)
- [Fitbit's Response](http://www.computerworld.com/article/2997561/cybercrime-hacking/researcher-says-fitbit-can-be-wirelessly-hacked-to-infect-pcs-fitbit-says-not-true.html)

##### Bluetooth - Satoe
- [The Citizen Lab Bluetooth Vulnerability Assessment](https://openeffect.ca/reports/Every_Step_You_Fake.pdf)

Hilts, Andrew (February 2, 2016). Every Step You Fake: A Comparative Analysis of Fitness Tracker Privacy and Security. The Citizen Lab. Retrieved from https://citizenlab.org/2016/02/fitness-tracker-privacy-and-security/
- [Hacktivity: 10 Second Hack] (https://www.framadrive.org/index.php/s/7Xal6WfggnFxSFY)

Avrille, Axelle (October 22, 2015). Fitbits Can be Hacked to Spew Malware, Security Expert Warns. Wired. Retrieved from http://www.wired.co.uk/article/fitbit-hack-malware-ten-seconds
- [Securelist: Hacking Fitbit] (https://securelist.com/blog/research/69369/how-i-hacked-my-smart-bracelet/)

Unucheck, Roman (March 26, 2015). How I Hacked My Smart Bracelet. SecureList. Retrieved from https://securelist.com/blog/research/69369/how-i-hacked-my-smart-bracelet/

##### Android App - Brett
- [Reverse-Engineering an Android App](http://securitywatch.pcmag.com/mobile-security/321138-rsac-reverse-engineering-an-android-app-in-five-minutes)
- [Apktool](https://ibotpeaches.github.io/Apktool/)
- [Apkmirror](http://www.apkmirror.com/)
- [Jadx](http://www.javadecompilers.com/apk)

##### API - Nick

- [Fitbit API Docs](https://dev.fitbit.com/docs/)
- [Terms of use](https://dev.fitbit.com/terms/)
- [Fitbit API Access using Oauth2.0](http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html)
- [Programmable Web Fitbit API](http://www.programmableweb.com/api/fitbit)
- [Fitbit Scraper Example](https://cran.cnr.berkeley.edu/web/packages/fitbitScraper/)

##### Misc
- [Fitbit in Academia](http://www.academia.edu/Documents/in/Fitbit)
- [OWASP API Abuse](https://www.owasp.org/index.php/Category:API_Abuse)
- [Fitness trackers data leak](http://www.informationweek.com/mobile/fitbit-other-fitness-trackers-leak-personal-data-study/a/d-id/1324165)
- [MIT Fitbit Hack](https://courses.csail.mit.edu/6.857/2014/files/17-cyrbritt-webbhorn-specter-dmiao-hacking-fitbit.pdf)

##### Technical Content

#### Fitbit Analysis

Fitbit is a fitness tracker that allows a user to track his/her life with the Fitbit's body sensors. By using these sensors,
the device can track various activities such as walking, running, and sleeping. Moreover, the Fitbit is a watch and alarm.
The device can be paired to one's computer through a USB connection, or paired to one's phone app. A user can also view
his/her Fitbit stats on their website.

All the user's data is collected on the device until it is synced with either the Android, iOS, or desktop software.
MIT students have found that no information persists on any of the devices, but instead gets data from Fitbit's cloud.

Fitbit also encrypts transmitted data to its servers over HTTPS, unlike other competitors such as Garmin.
But like many devices Fitbit exposes its Bluetooth information, thus potentially leaking data available to Bluetooth
beacons typically set up in shopping malls to track customers. Apple addresses this issue (haha) by [randomizing their
Bluetooth MAC address](http://www.informationweek.com/mobile/fitbit-other-fitness-trackers-leak-personal-data-study/a/d-id/1324165).

##### Fitbit Surge Sensors and Components

>   Sensors and Components
    GPS.
    3-axis accelerometers.
    3-axis gyroscope.
    Digital compass.
    Optical heart rate monitor.
    Altimeter.
    Ambient light sensor.
    Vibration motor.

Source: [Fitbit](https://www.fitbit.com/surge)

##### Fitbit Attack Vectors

Like many mobile devices, Fitbit has a relatively large attack surface including:

- **API Abuse**
- **USB Connection**
- **Bluetooth**
- Software
    - **Android App**
    - iPhone App
    - Fitbit device software
- Wireless
- Sensors
- Hardware

##### Bug Bounty

Fitbit has a [bug bounty program](https://bugcrowd.com/fitbit), but has 
a large amount of restrictions (CSRF, XSS, SQL Injection).These attack vectors being in the OWASP Top 10,
it is disappointing that Fitbit would not provide a bug bounty for these vectors since black hats may be less
inclined to follow [Fitbit's Terms of Service](https://dev.fitbit.com/terms).
This may hinder white hats from finding vulnerabilities on Fitbit's platform.

The window of compliance between these two sets of restrictions is slim, and difficult to perform a
comprehensive web security analysis.

[E-Commerce Platform Shopify](https://hackerone.com/shopify) has a much less restrictive bug bounty program,
and in fact, encourages SQL Injection, CSRF, and XSS bounties.

---------------------------------------------------------------------------

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

#### Bluetooth Attack Surface (Satoe)
Similar to the API Attack Surface, spoofing Bluetooth pairing between a Fitbit device, and a laptop or mobile will allow the attacker to have access to vital signs, calories burned, sleep activity, geolocation, phone serial number IMEI Number, steps per interval, and
reproductive health information.

Fitbit typically syncs by connecting through Bluetooth to a device, which with Fitbit's software will sync with Fitbit's cloud.

#### Bluetooth Motivation
The attacker that has paired to the victim's Fitbit through Bluetooth,can not only gather information on the victim, but also manipulate the information stored on the device. Although damage is minimal, information leaks still violate users' privacy. It's also possible an attack could impersonate a user at this point.

Bluetooth is most vulnerable for exploitation when it is not paired. Users may be trying to save battery or assume that once the Fitbit device is done syncing, they do not need to keep bluetooth enabled. However, the Fitbit device will revert to "advertising mode" and repeatedly emits a fixed signal and unique ID to alert the phone that it is waiting to re-establish a connection. During this 'advertising mode,' attackers are free to pair with the device and cause disturbance in re-establishing connection with the users' device.
It is also possible that Bluetooth "beacons" in public areas could be used to identify the Fitbit, and thus track the user's physical location.

#### Bluetooth Hacking

Hacking Fitbit's Bluetooth is possible by forging its MAC address and replaying it, but only after gaining its key from
the phone.

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
Aside from modifying data of steps and distances, Avrille claimed as a proof of concept that the attacker could inject a malicious code into the tracker which only required 10 seconds, with an verification time of 60 seconds (timed to a jog of the victim). Only the initial injection requires that the Fitbit device be near the attacker. The verification can happen even when the victim is out of reach.

When the victim wants to synchronize their data to update their profile, the device will respond. However, added to the original message, the response will be infiltrated with the infected packet, which will then be delivered to the victim's laptop or mobile device. This could then start a back door and even infect other trackers.

Although the payload is small, just a mere 17 bytes, it is enough for a Trojan such as the Crash Pentium Trojan in 2004, which only required 4 bytes.

#### Fitbit's Reponse
Fitbit claimed that these claims were false and cannot be reproduced.

>On Wednesday October 21, 2015, reports began circulating in the media based on claims from security vendor, Fortinet, that Fitbit devices could be used to distribute malware. These reports are false. In fact, the Fortinet researcher, Axelle Apvrille who originally made these claims has confirmed to Fitbit that this was only a theoretical scenario and is not possible. Fitbit trackers cannot be used to infect user’s devices with malware. We want to reassure our users that it remains safe to use their Fitbit devices and no action is required.

This does not instill a great amount of confidence in Fitbit's security procedure, as they seem to tend to ignore
vulnerabilities.

-------------------------------------------------------------------------

#### USB Attack Surface
Every Fitbit model is charged through a USB cable, some models also require synchronization through a USB dongle. One possible area of a USB attack is infecting a computer from a Fitbit that has previously been infected wirelessly. The proof-of-concept vulnerability research shows that in close range (Bluetooth range) an attacker can wirelessly inject malicious code into the Fitbit, which then infects a PC or other devices that the Fitbit connects to via USB.


#### USB Hacking
According to the Senior Fortinet researcher Axelle Apvrille, the attacker does not need physical access to the tracker, a close range is enough. It does not even matter if the Fitbit is paired with another device or not. Within the Bluetooth range, the device can be infected and then potentially install a virus, Trojan or other vulnerability to the computer days later when charging the device or synchronizing. Because all Fitbits require charging and synchronization through USB, this becomes a huge vulnerability. 


#### Fitbit’s Response

In defense, Fitbit said that "we believe that security issues reported today are false, and that Fitbit devices can't be used to infect users with malware." It said that while Fortinet did contact them to report a "low-severity issue," there was no indication it could be used to distribute malware. 

----------------------------------------------------------

#### Android App Attack Surface
The Fitbit Android app allows users to view the data their Fitbit wearable tracks. This data includes both the backlogged data that gets sent to Fitbit's servers, and live data that is viewable only from the app. A user can also find friends who have Fitbits by searching through their Google or Facebook contacts if the user chooses to link those accounts to their Fitbit account.

####Android App Motivation
The Fitbit Android app has been downloaded somewhere between 10,000,000 and 50,000,000 times according to the Google Play Store. This means that a vulnerability found in the app could affect tens of millions of people. Additionally, Android apps can be reverse-engineered more easily than iOS apps, as there are many easy-to-use, publicly available decompilers.
Our motivation for reverse-engineering the Fitbit Android app is to both search for any possible vulnerabilities, and to try editing the app in a way that would create a vulnerability for someone who would install the modified version.

####Android App Hacking
First we have to acquire the apk file for Fitbit's app. There are several ways to get this, but the easiest is to download it using [apkmirror](http://www.apkmirror.com/).

There are two processes that should be done to reverse-engineer an Android app:

- Decompile the apk into smali, which is like assembly code for java files. Make any desired changes to the smali code, and compile it back into an apk to run on an Android device. This can be done using *apktool* which is built into Kali Linux.

1. `apktool d <path to fitbit.apk>`
This will decompile the apk into smali files, and will create a directory called "fitbit" in the working directory to contain these files. It does this using baksmali (also built into Kali Linux) on the classes.dex files which can be found in the root directory of the apk. 
Every Android app has a classes.dex file which contains the compiled machine code for app. In the case of the most recent version of fitbit's apk, there are two classes.dex files: classes.dex and classes2.dex. When multiple dex files are present, this is called "multidex", and is used in the case that the app is very large. 
Inside the new fitbit directory there are two directories containing the smali code: smali and smali_classes2. Any modifications the hacker desires to make should be made to the files in those directories.
2. `apktool b fitbit`
Two new directories will be created in the fitbit directory: build and dist. They contain the unzipped and zipped versions respectively of the modified fitbit.apk.
3. `keytool -genkey -v -keystore <key name>.keystore -alias <alias name> -keyalg RSA -keysize 2048 -validity 10000 `
This creates a key to sign the modified apk. Without this step and the next, the phone will see the package as corrupt when installing. This step only needs to be done once, as the key can be reused.
4. `jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore <key name>.keystore fitbit/dist/fitbit.apk <alias_name>`
This signs the apk.
5. `zipalign -f -p 4 fitbit/dist/fitbit.apk fitbit/dist/fitbit-aligned.apk`
This zipaligns the apk, aligned at 4 bytes.
6. Now the apk can be transferred to an Android phone and installed via a file explorer.
- Convert the apk to java code. This won't be fully working java code, but will be more readable than the smali code and will help in understanding what the code does. The easiest way to do this is to use an online decompiler such as [Jadx](http://www.javadecompilers.com/apk). The result will be a downloadable zip file of java code with the same file names as the smali files.

####Modifying the Android app
The first modification that needs to be made is to enable debugging mode. This allows one to view log messages made by the Fitbit app in the Android Monitor in Android Studio. To do this, open the AndroidManifest.xml file within the fitbit directory created by apktool. Add `android:debuggable="true"` anywhere within the `<application/>` tag.
While there are some log messages already, they aren't particularly revealing. To add a log message of our own, we need to write smali code to mimic this Java function call: `Log.d("TAG", "Message");`
We can do this: 
`const-string v0, "TAG"
const-string v1, "Message"
invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I` 
A quick test to make sure that the log can be seen is to add these lines inside the onCreate call in the MainActivity.smali file, found in fitbit/smali/com/fitbit. This log now appears after signing in to the app and selecting "Try a preview of the new dashboard". 
If a log message is placed in the code for an activity that has sensitive data, one can view that data in the Android Monitor. All that needs to be done is to find a page that collects or displays that data, and replace `v1` with that data. Such data that could be sensitive consists of usernames and passwords, heart rate, food/water intake, sleep schedule, names of friends, distance walked, and more.
While this data can be logged easily in the Android Monitor, a hacker would need access to the victim's device in order to connect it to Android Studio. A much more interesting scenario would be to write smali code to send that sensitive data to the Hacker in some way. As writing smali code is hard, a better approach would be to write an Android app that sends data, and then use apktool as described above in order to see how that code would be done in smali, and then make the necessary modifications to the fitbit smali code.
Now all that needs to be done is to convince someone to install the modified fitbit.apk instead of from the Play Store. This can be done using social engineering among various other methods, such as uploading the modified fitbit.apk to a third party app store.

####Miscellaneous interesting information found in the Android app

- The Google Maps API Key can be found in the AndroidManifest.xml file. It is: `AIzaSyCTYIpQi6kwi2Fw6yEskBVS25-lZ0iZ-zU`


-------------------------------------------------------------------------

##### Limitations

###### API Scraping Limitations
- The attacker would have to resort to traditional social
engineering methods such as phishing to gain API access.

- Due to Fitbit's Bug Bounty limitations, CSRF and XSS vulnerabilities may not be examined within strict ethical guidelines.
  We suspect there are numerous CSRF and XSS vulnerabilities, due to Fitbit's desire to obfuscate them.
  This may be why the MIT student researchers did not evaluate API vulnerabilities.

##### Results

#### Privacy Implications

The privacy implications of fitness trackers have not been evaluated as
much as older technologies have.

With access to a user's heart-rate logs over time, an app could detect
for heart abnormalities or more maliciously, an advertising agency
may be able to use heart rate patterns to fingerprint a user between devices.

This pertinent health information is not regulated by HIPAA, and thus companies are allowed
to collect and distribute this data. It's possible this could lead to higher insurance rates if an insurer
was aware that their customer is more susceptible to certain diseases or illnesses.

[Even default privacy settings leak personal information such as one's sexual activity.](https://techcrunch.com/2011/07/03/sexual-activity-tracked-by-fitbit-shows-up-in-google-search-results/)

If an attacker compromises the user's Fitbit device, or syncing device, then the attacker
could gain real-time access to the user's Fitbit sensors. Since the Fitbit the worn constantly,
the data from the Fitbit's sensors may be more accurate, or revealing than a phone's sensors.
It may even be possible to track a user's literal step-by-step location by correlating data from
the Fitbit's GPS, accelerometer, compass and altimeter.

**As we attach ourselves to more bodily sensors, we expose more personal
information online.** Personal information has been the new goldmine of the
21st century, as seen by an overwhelming majority of technology companies
such as Google, Facebook, Amazon, etc... Thus it is very likely that Fitbit is
already profiting from its user data.

Technology wearables increase our attack surface. While cell-phones also contain accelerometers, the activity trackers are
designed to stay on the user at all times, thus bridging the informational gap that adversaries may experience if only
hacking one's phone. The proliferation of wearables along with competition between many firms, implies future fitness trackers will
contain more sensors, thus providing additional attack vectors into our life.

##### API Implications (besides access to basic user info)

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

1. First, Click the below Authorization URL and login to your Fitbit Account:

`https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228349&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Ffitbit&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep20social%20weight&expires_in=604800`

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

If you receive an error with oauth then the token may be expired.
    
##### Disclaimer 

This is for use by Team members only. If you would like to use this for your own Fitbit app, simply replace your authorization code in global_headers,
and your redirect_uri in oauth_request_data.

When you run this, you are using this script at your own discretion. We hold no warranty for this script. If you are not redirecting to a secure server (if no https), then you may expose your sensitive information because this app requests for a maximum amount of informational access to your Fitbit account. If you redirect to an unencrypted connection, there is absolutely no guarantee of privacy.

Works only for authorization code flow!

##### Conclusions

Fitbit should be more open to bug bounty collectors, otherwise malicious actors may exploit vulnerabilities instead.
Fitbit brushes off "[theoretical vulnerabilities](https://community.fitbit.com/t5/Fitbit-com-Dashboard/Theoretical-bluetooth-vulnerability/td-p/995475)," which does not instill confidence in its security policies. Not enough people care about the personal information they are sending when using a wearable.
The information can be used to fingerprint your future movements.
There is no way for users to download all of their collected information (which may be illegal in certain jurisdictions).
The Fitbit Data Scraper may the closest thing a user could use to obtain his/her personal data.

While Fitbit has a fairly large attack surface, it is not clear what vulnerabilities exist due to the back-and-forth
between Fitbit employees and Fitbit hackers. Fitbit's Bug Bounty program should be extended to account for these unknown
vulnerabilities. Unfortunately, due to the competition between fitness trackers, Fitbit may not have a significant
amount of incentive for Fitbit to increase user security, and users also may not care if their data is leaked.

Thus, as with most devices that generate an extensive amount of personal user information, there must
tighter safeguards to limit the data that companies collect. Fitness trackers should be held to higher standards of
privacy expectations. Users should also be able to access their own data, and be able to purge them from a service's database.

All-in-all, Fitbit has reasonable security compared to other fitness tracker competitors. Its security is not perfect,
and fitness trackers are expected to become replaced by smart watches, which may be created by companies such as Apple,
with a larger security base.
