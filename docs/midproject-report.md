### Boston University College of Engineering
### EC521 Cyber Security Project Fall 2016
###  Mid Project Report
### Group 3 - Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky
[Fitbit Cyber Project on Github(https://github.com/ssakuma4593/EC521_Fitbit)

### Created: 10/10/16
### Last Updated: 10/23/16

#### Required elements
You need to provide sufficient evidence that you have thought through how to complete the project, and that I can use to assess the appropriateness of its scope and technical merits. To this end, your report topic should contain:


#### Description
A brief description of the project you are planning to complete, including your group number, the members of your group, your chosen project, and a preliminary explanation of what you plan to implement in enough detail that I can assess the potential success of the project.

``` Group 3 (Inna Turshudzhyan, Nick Louie, Satoe Sakuma, Brett Moretzky)```

#### Security Assessment of the Fitbit 

Fitness trackers are an advent of the emerging field of technology wearables and the internet of things. 
Thus, we intend to perform a security assessment of possible attack vectors on the health wearable, the Fitbit. 

We plan on researching vulnerability in Fitbit’s attack surface including:
    - The Fitbit API
    - Bluetooth + Bluetooth Low Energy
    - Mobile application (Android)
    - USB connectivity (Windows)


#### References
A list of the five most relevant references that you have found to the background you need for the project. Ideally, these references should be from high-quality, reputable sources (books with known publishers, peer-reviewed papers, established conference proceedings, specification pages of well-established companies) - not from unreviewed or weakly reviewed web content (e.g. wikipedia). They should also be specific enough to be useful (e.g. "Wall Street Journal, October 5, 2016, Twitter Sale Nears As Bids Come Due " rather than just "The Wall Street Journal").

##### USB - Inna

##### Bluetooth - Satoe

##### Android App - Brett

##### API - Nick
- [API Docs](https://dev.fitbit.com/docs/)
- [Fitbit Scraper](https://cran.cnr.berkeley.edu/web/packages/fitbitScraper/)

##  Schedule
A tentative schedule of goals and deadlines leading up to the project’s completion, and the envisioned role of each person in the group. Although some members may have managerial or documentation roles, every member must also have a substantive technical contribution to the project.

September 28: GroupSelection. [5 points]
September 30: Project selection. [5 points]
October 26: MidProjectReport. [15 points]
November 30: Final report due. [35 points]
December 5, 7, 12: Group presentations. [40 points]

**October 11** - Research attack vectors (start understanding phase)
- Inna - USB
- Brett - Mobile
- Nick - API
- Satoe - Bluetooth

**October 12** - Start Mid Project Report
- Define Description
- Define schedule
- Assign reference work
- Assign roles
    - Define scope
    
**October 12 - 25** - Understanding Phase
- USB (Inna)
- Mobile Android (Brett)
- API (Nick)
- BT (Satoe)

_(Meet sometime)_

**October 24**  - References portion of the mid project report should be completed for each person 
**October 25** - Mid Project report should be done, understanding phase should be completed and each member should have a detailed outline of their topic, and potential avenues for attacks for which we can analyze. This should be all done in github markdown ty. 
**October 26** - Submit Mid Project Report

_(Meet sometime)_

**November 16** - Finish Analysis - Define later

_(Meet sometime in between)_

**November 27** - Finish most of the report
**November 29** - Panic, stay up all night and finish the project
**November 30** - Submit Final Report
**Nov 30** -> Prepare for Group Presentation

###### Envisioned roles
- Nick - Research and Analyze API
- Satoe - Research and Analyze BT
- Brett - Android mobile app
- Inna - USB connectivity


## Technical content
What are the interesting cybersecurity technical challenges involved in bringing this project to completion. Assign qualitative estimates (e.g. fake percentages) for each challenge describing how confident you are that you will be able to meet the challenges. There should be at least some challenges that you are 100% confident that you will complete them (if not, pick some easier challenges), and some that you are less than 100% confident that you will complete.

- Spoofing Bluetooth as Fitbit to mobile (70%)
- Analyzing USB transmission from Fitbit to Computer (70%)
- Finding a vulnerability within the API framework (10%)
- API Proof of concept of data scraping (100%) 
- Reverse Engineer Android App (100%)
- Understanding Android App (75-80%) 


### Comments
A place at the bottom of the topic, where I can provide feedback as appropriate.

```
You guys are great!!!! - AT
A+
```