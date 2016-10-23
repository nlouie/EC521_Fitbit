### Boston University College of Engineering
## EC521 Cyber Security Project Fall 2016
##  References
### 10/10/16
### Group 3 - Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky

## Fitbit's Attack Surface

####  Misc Links
[BugCrowd](https://bugcrowd.com/fitbit)
[Fitbit in Academia](http://www.academia.edu/Documents/in/Fitbit)


### Bluetooth

- [\[MIT\] Security Analysis of Wearable Fitness Devices (Fitbit)](https://courses.csail.mit.edu/6.857/2014/files/17-cyrbritt-webbhorn-specter-dmiao-hacking-fitbit.pdf)
		 	 	 		
    As we have described above, Bluetooth communication between the Fitbit device and the smartphone or computer application is authenticated with a MAC in CBC mode using XTEA. Because the phone must contain the key used to authenticate communication, we could extract the key during more analysis of the phone. With the key and algorithm, it would become possible for us to forge a MAC and launch a replay attack over Bluetooth. 

- [\[The Stack\] - Fitbit's Open Bluetooth Port Enables Rapid Viral Malware Infection](https://thestack.com/security/2015/10/21/fitbits-open-bluetooth-port-enables-rapid-viral-malware-infection/)

- [\[Citizen Lab\] Security Privacy Issues Leading Wearable Fitness Tracking Devices ](https://citizenlab.org/2016/02/security-privacy-issues-several-leading-wearable-fitness-tracking-devices/)

    We determined that Fitbit collects extraneous information about users, including the MAC addresses of nearby Fitbits. We also discovered that the android application has access to step data with granularity down to a minute, but the user interface does not present this.
    
    Overall, the Fitbit provides a reasonable level of privacy for user data, but we would prefer a design that provided valid users an easy-to-access method for acquiring the full set of data recorded by the device.

- [\[Fitbit\] - Theoretical Bluetooth Vulnerability](https://community.fitbit.com/t5/Fitbit-com-Dashboard/Theoretical-bluetooth-vulnerability/td-p/995475)

    Only 17 bytes to work with

-[\[The Register\] - Fitbit Hack](http://www.theregister.co.uk/2015/10/21/fitbit_hack/)

Apvrille has pulled off other hacks; she is able to manipulate the number of counted steps and logged distance to earn badges that can be traded in for discounts and prizes.
Those badges can be turned into discounts and gifts through third-party companies such as Higi which in April launched an API to help companies receive health data derived from wearables.

She says communication is over XML and Bluetooth Low Energy while encryption and decryption occurs on the wearable device, and not on the dongle which is "outside of the security boundaries".

https://www.youtube.com/watch?v=qa8qVAPPlTE

- [\[Wired\] - Fitbit Hack Malware Ten Seconds](http://www.wired.co.uk/article/fitbit-hack-malware-ten-seconds)

    On Twitter Apvrille pointed out that the vulnerability was hypothetical and no trackers are known to have been hacked in this manner. Despite Apvrille informing Fitbit of the vulnerability in March it has yet to fix the problem, The Register reports.

https://thestack.com/security/2015/10/21/fitbits-open-bluetooth-port-enables-rapid-viral-malware-infection/

- [\[Secure List\] - How I Hacked my Smart Bracelet](https://securelist.com/blog/research/69369/how-i-hacked-my-smart-bracelet/)
        Researcher claims to have done it.

##### Bottom Line

So it seems like there is conflicting opinions. Fitbit says that there is no significant bluetooth vulnerability since the 17 bytes can’t do anything and also said this theoretical issue has been patched, but other reports show this has not been patched and current vulnerabilities show we can change the number of steps..


#####  Bluetooth low energy hacking

[Hackaday - Dictionary Bluetooth Low Energy](http://hackaday.com/2015/12/02/hackaday-dictionary-bluetooth-low-energy/)

Bluetooth LE, also known as Bluetooth Smart, is part of the fourth version of the Bluetooth standard. Finalized in 2010, Bluetooth 4.0 has been updated several times since, and the current version is 4.2, released in July of 2015. This version creates three different classes of device: Bluetooth, Bluetooth Smart Ready and Bluetooth Smart. The basic idea is that Bluetooth Smart indicates a device such as a pedometer or heart monitor that can only send and receive Bluetooth LE signals, while a Smart Ready device can handle LE and standard Bluetooth signals. A standard Bluetooth 4.2 device (such as a cell phone or USB dongle) can also send and receive Bluetooth LE signals.


#####  [Crackle](https://lacklustre.net/projects/crackle/)
    
Crackle cracks Bluetooth Smart (BLE) encryption. It exploits a flaw in the pairing mechanism that leaves all communications vulnerable to decryption by passive eavesdroppers.
crackle can guess or very quickly brute force the TK (temporary key) used in the pairing modes supported by most devices (Just Works and 6-digit PIN). With this TK, crackle can derive all further keys used during the encrypted session that immediately follows pairing. The LTK (long-term key) is typically exchanged in this encrypted session, and it is the key used to encrypt all future communications between the master and slave.
The net result: a passive eavesdropper can decrypt everything. Bluetooth Smart encryption is worthless.

http://www.forbes.com/sites/thomasbrewster/2015/05/21/context-android-app-spies-on-bluetooth-le/#ff5441a6a354
https://play.google.com/store/apps/details?id=com.contextis.android.BLEScanner
    
RaMBLE can track metadata spewed out by all devices using Bluetooth LE (for “low energy”), a lightweight version of the Bluetooth standard used by scores of wearable products and smartphones. The app logs each device it sees within at least 100 metres, exports the database to the Android phone SD card, and plots the location of the device on a Google Maps plugin.

If it’s easy to attribute a device to a particular person, like a celebrity or a CEO, then it’s easy to tell when they’re nearby, he claimed.

##  Hardware

https://www.ifixit.com/Teardown/Fitbit+Flex+Teardown/16050

Possible Security Flaws: 
Bluetooth antenna (communication with devices)
[Near Field Communications antenna (NFC)](http://www.makeuseof.com/tag/using-nfc-3-security-risks-to-be-aware-of/ )
USB plug (BLE Antenna, USB connection contacts)


### API

- [API Docs](https://dev.fitbit.com/docs/)
- [Terms of use](https://dev.fitbit.com/terms/)

####  Fitbit Login

Users must be presented with either the option to create a Fitbit Account, which will direct them to Fitbit.com, or to login to their Fitbit account using Fitbit's OAuth protocol.
https://dev.fitbit.com/docs/oauth2/

Fitbit uses OAuth 2.0 for user authorization and API authentication. The OAuth 2.0 framework requires your application to obtain an Access Token when the Fitbit user authorizes your app to access their data. The Access Token is used for making HTTP request to the Fitbit API.

http://www.programmableweb.com/api/fitbit


Unlike the Authorization Code Grant Flow, the refresh tokens are not issued with the Implicit Grant flow. Refreshing a token requires use of the client secret, which cannot safely be stored in distributed application code. When the access token expires, users will need to re-authorize your app.
Access tokens from the Implicit Grant Flow are longer lived than tokens from the Authorization Code Grant flow. Users may specify the lifetime of the access token from the authorization page when an application uses the Implicit Grant flow. The access token lifetime options are 1 day, 1 week, and 30 days. Applications can pre-select a token lifetime option, but the user ultimately decides.

####  Python Fitbit Oauth

[\[Fitbit\] Fitbit Api Access using Oauth2.0](http://pdwhomeautomation.blogspot.co.uk/2016/01/fitbit-api-access-using-oauth20-and.html)

 [Fitbit Scraper Example](https://cran.cnr.berkeley.edu/web/packages/fitbitScraper/)

Info an app could get about a user:

- Activity 
- Body Fat
- Food 
- Friends
- Heart rate
- Sleep 

User profile 
```json
{
    "user": {
        "aboutMe":<value>,
        "avatar":<value>,
        "avatar150":<value>,
        "city":<value>,
        "clockTimeDisplayFormat":<12hour|24hour>,
        "country":<value>,
        "dateOfBirth":"<value>,
        "displayName":<value>,
        "distanceUnit":<value>,
        "encodedId":<value>,
        "foodsLocale":<value>,
        "fullName":<value>,
        "gender":<FEMALE|MALE|NA>,
        "glucoseUnit":<value>,
        "height":<value>,
        "heightUnit":<value>,
        "locale":<value>,
        "memberSince":<value>,
        "nickname":<value>,
        "offsetFromUTCMillis":<value>,
        "startDayOfWeek":<value>,
        "state":<value>,
        "strideLengthRunning":<value>,
        "strideLengthWalking":<value>,
        "timezone":<value>,
        "waterUnit":<value>,
        "weight":<value>,
        "weightUnit":<value>
    }
}

```


##  App

https://courses.csail.mit.edu/6.857/2014/files/17-cyrbritt-webbhorn-specter-dmiao-hacking-fitbit.pdf
    
“Live data mode” is a feature of Fitbit devices that displays live metrics on the application display while connected to the Fitbit device. We determined that “live data mode” operates on unencrypted data. 
Heart rate is part of this live data, which is potentially more valuable than the other pieces of data.

One important observation we made was that live data packets are nearly identical, indicating that encryption for live data packets is not used (or at least does not employ randomized encryption). We decided to try to exploit this. We modiﬁed the part of the code where the app reads the live data, changing the step count in the packets. This was partially successful — we were able to control the value displayed on the mobile device. In one instance we were able to convince the app that the device had only counted 7 steps all day. However, this data did not propagate to the server. We believe that the live data is only there so that the user can get immediate updates and that the data it sends is duplicated in the synchronization packets which are better protected. 

The device authenticates with the app by computing a MAC over random bits, using a CBC-MAC with the XTEA block cipher. There is no further authentication as far as we could tell. 

We saw step data in ﬁner granularity than Fitbit provides. The app only shows steps aggregated to 5 minute intervals while the wiﬁ packets have 15 minute intervals. The logging statement contains step data at 1 minute granularity. This is data which is not available (or exportable) by directly using the app. Once the logging statements were functioning, we decided to further investigate the logs provided by “Live Data mode” classes. We observed live data packets which are similar to those shown in ﬁgure 4. 

https://help.fitbit.com/articles/en_US/Help_article/2015/?l=en_US&c=Topics%3AAndroid&fs=Search&pn=1

If you send notifications to your Fitbit tracker from an Android device, some notifications may be unencrypted. If we’re unable to encrypt a notification, which happens periodically on various devices, you'll be alerted and given the choice to retry the encrypted transmission or to allow the transmission to pass unencrypted.
Note that unencrypted in this context means only that the text visible on your tracker is potentially vulnerable to an eavesdropping device. So, a person attempting to intercept Bluetooth transmissions might see the contents of the  message, or if you received a call notification, the phone number. Your personal information stored with Fitbit is always encrypted. You can require that all notifications to your Fitbit tracker are encrypted.

https://help.fitbit.com/articles/en_US/Help_article/1507/?l=en_US&c=Topics%3AWindows_Phone&fs=Search&pn=1

The Windows 8.1 app hasn’t been supported since April. If we can find a documented exploit that has been patched on another OS, it would probably not be patched on Windows 8.1.




