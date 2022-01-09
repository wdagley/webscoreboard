from flask import Flask
from flask import render_template
from datetime import datetime
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="Top 25 Scoreboard", games = acc_games, date_now = date_now)

@app.route("/AAC")
def aac():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = aac_games, date_now = date_now)


@app.route("/ACC")
def acc():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = acc_games, date_now = date_now)


@app.route("/B1G")
def b1g():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = b1g_games, date_now = date_now)


@app.route("/BigXII")
def bigxii():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = big12_games, date_now = date_now)


@app.route("/CUSA")
def cusa():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = cusa_games, date_now = date_now)


@app.route("/MAC")
def mac():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = mac_games, date_now = date_now)


@app.route("/MWC")
def mwc():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = mwc_games, date_now = date_now)


@app.route("/PAC12")
def pac12():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = pac_games, date_now = date_now)


@app.route("/SEC")
def sec():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = sec_games, date_now = date_now)


@app.route("/SunBelt")
def sunbelt():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = sun_games, date_now = date_now)


@app.route("/Independent")
def independent():
    aac_games, acc_games, b1g_games, big12_games, cusa_games, mac_games, mwc_games, pac_games, sec_games, sun_games, ind_games = get_games()
    date_now = datetime.today().strftime("%b %d, %Y")
    return render_template("index.html", title="ACC Scoreboard", games = ind_games, date_now = date_now)







def get_games():
    import datetime
    import logging
    import praw
    import pandas as pd
    import re
    #import matplotlib.pyplot as plt
    import math
    import numpy as np
    #import gspread
    #from df2gspread import df2gspread as d2g
    #from oauth2client.service_account import ServiceAccountCredentials

    fbs_teams = ['Air Force',
    'Akron',
    'Alabama',
    'Appalachian State',
    'Arizona',
    'Arizona State',
    'Arkansas',
    'Arkansas State',
    'Army',
    'Auburn',
    'Ball State',
    'Baylor',
    'Boise State',
    'Boston College',
    'Bowling Green',
    'Buffalo',
    'BYU',
    'California',
    'Central Michigan',
    'Charlotte',
    'Cincinnati',
    'Clemson',
    'Coastal Carolina',
    'Colorado',
    'Colorado State',
    'Connecticut',
    'Duke',
    'East Carolina',
    'Eastern Michigan',
    'FAU',
    'FIU',
    'Florida',
    'Florida State',
    'Fresno State',
    'Georgia',
    'Georgia Southern',
    'Georgia State',
    'Georgia Tech',
    'Hawaii',
    'Houston',
    'Illinois',
    'Indiana',
    'Iowa',
    'Iowa State',
    'Kansas',
    'Kansas State',
    'Kent State',
    'Kentucky',
    'Liberty',
    'Louisiana Tech',
    'Louisiana',
    'Louisiana–Monroe',
    'Louisville',
    'LSU',
    'Marshall',
    'Maryland',
    'UMass',
    'Memphis',
    'Miami (FL)',
    'Miami (OH)',
    'Michigan',
    'Michigan State',
    'Middle Tennessee',
    'Minnesota',
    'Mississippi State',
    'Missouri',
    'Navy',
    'NC State',
    'Nebraska',
    'Nevada',
    'New Mexico',
    'New Mexico State',
    'North Carolina',
    'North Texas',
    'Northern Illinois',
    'Northwestern',
    'Notre Dame',
    'Ohio',
    'Ohio State',
    'Oklahoma',
    'Oklahoma State',
    'Old Dominion',
    'Ole Miss',
    'Oregon',
    'Oregon State',
    'Penn State',
    'Pittsburgh',
    'Purdue',
    'Rice',
    'Rutgers',
    'San Diego State',
    'San Jose State',
    'SMU',
    'South Alabama',
    'South Carolina',
    'Southern Mississippi',
    'Stanford',
    'Syracuse',
    'TCU',
    'Temple',
    'Tennessee',
    'Texas',
    'Texas A&M',
    'Texas State',
    'Texas Tech',
    'Toledo',
    'Troy',
    'Tulane',
    'Tulsa',
    'UAB',
    'UCF',
    'UCLA',
    'UNLV',
    'USC',
    'USF',
    'Utah',
    'Utah State',
    'UTEP',
    'UTSA',
    'Vanderbilt',
    'Virginia',
    'Virginia Tech',
    'Wake Forest',
    'Washington',
    'Washington State',
    'West Virginia',
    'Western Kentucky',
    'Western Michigan',
    'Wisconsin',
    'Wyoming']


    # In[10]:


    AAC = ['Cincinnati',
    'Connecticut',
    'East Carolina',
    'Houston',
    'Memphis',
    'Navy',
    'SMU',
    'Temple',
    'Tulane',
    'Tulsa',
    'UCF',
    'USF']

    ACC = ['Boston College',
    'Clemson',
    'Duke',
    'Florida State',
    'Georgia Tech',
    'Louisville',
    'Miami (FL)',
    'North Carolina',
    'NC State',
    'Syracuse',
    'Pittsburgh',
    'Virginia',
    'Virginia Tech',
    'Wake Forest']

    B1G = ['Illinois',
    'Indiana',
    'Iowa',
    'Maryland',
    'Michigan',
    'Michigan State',
    'Minnesota',
    'Nebraska',
    'Northwestern',
    'Ohio State',
    'Penn State',
    'Purdue',
    'Rutgers',
    'Wisconsin']

    BIG12 = ['Baylor',
    'Iowa State',
    'Kansas',
    'Kansas State',
    'Oklahoma',
    'Oklahoma State',
    'TCU',
    'Texas',
    'Texas Tech',
    'West Virginia']

    CUSA = ['Charlotte',
    'FAU',
    'FIU',
    'Louisiana Tech',
    'Marshall',
    'Middle Tennessee',
    'North Texas',
    'Old Dominion',
    'Rice',
    'Southern Mississippi',
    'UAB',
    'UTEP',
    'UTSA',
    'Western Kentucky']

    MAC = ['Akron',
    'Ball State',
    'Bowling Green',
    'Buffalo',
    'Central Michigan',
    'Eastern Michigan',
    'Kent State',
    'Miami (OH)',
    'Northern Illinois',
    'Ohio',
    'Toledo',
    'Western Michigan']

    MWC = ['Air Force',
    'Boise State',
    'Colorado State',
    'Fresno State',
    'Hawaii',
    'Nevada',
    'New Mexico',
    'San Diego State',
    'San Jose State',
    'UNLV',
    'Utah State',
    'Wyoming']

    PAC12 = ['Arizona',
    'Arizona State',
    'California',
    'Colorado',
    'Oregon',
    'Oregon State',
    'Stanford',
    'UCLA',
    'USC',
    'Utah',
    'Washington',
    'Washington State']

    SEC = ['Alabama',
    'Arkansas',
    'Auburn',
    'Florida',
    'Georgia',
    'Kentucky',
    'LSU',
    'Mississippi State',
    'Missouri',
    'Ole Miss',
    'South Carolina',
    'Tennessee',
    'Texas A&M',
    'Vanderbilt']

    SUNBELT = ['Appalachian State',
    'Arkansas State',
    'Coastal Carolina',
    'Georgia Southern',
    'Georgia State',
    'Liberty',
    'Louisiana',
    'Louisiana–Monroe',
    'New Mexico State',
    'South Alabama',
    'Texas State',
    'Troy']

    Independent = ['Army',
    'BYU',
    'UMass',
    'Notre Dame']


    # In[11]:


    reddit = praw.Reddit(client_id='-ffm3p2kXHFQcA',                      client_secret='uv61hwY-PliPcq1fOsPXdIup8Agj9w',                      user_agent='ScoutingReport',                      username='THExDAGGER',                      password='june1996')


    # In[12]:


    subreddit = reddit.subreddit('FakeCollegeFootball')


    # In[13]:


    def find_ball(selftext):
        team_pattern = re.compile(r'''
                                (?P<next>^)
                                (?P<names>^[0-9])
                            ''',
                            re.VERBOSE)
        ball = re.findall(team_pattern, selftext)
        
        return ball


    # In[14]:


    def parseWaitingOn(submissionbody, homeUser, awayUser, homeTeam, awayTeam):
        if("Waiting on a response from" in submissionbody):
            user = submissionbody.split("Waiting on a response from")[1].split("to this")[0].strip()
            if(user == homeUser):
                return homeTeam
            elif(user == awayUser):
                return awayTeam
        
    """
    Parse the home team user from the game thread

    """    
    def parseHomeUser(submissionbody):
        homeUser = submissionbody.split("___")[0].split("\n")[13].split("|")[1].strip()
        return homeUser
        
    """
    Parse the away team user from the game thread

    """    
    def parseAwayUser(submissionbody):
        awayUser = submissionbody.split("___")[0].split("\n")[12].split("|")[1].strip()
        return awayUser


    """
    Parse the quarter from the game thread

    """
    def parseQuarter(submissionbody):
        if(len(submissionbody.split("___")) == 7):
            quarter = submissionbody.split("___")[4].split("\n")[4].split("|")[1].split(" ")[0]
        else:
            quarter = submissionbody.split("___")[4].split("\n")[3].split("|")[1].split(" ")[0]
        if quarter == "1":
            return "1Q"
        elif quarter == "2":
            return "2Q"
        elif quarter == "3":
            return "3Q"
        elif quarter == "4":
            return "4Q" 
        else:
            return "OT"
    
    """
    Parse the yard line from the game thread

    """
    def parseYardLine(submissionbody):
        if(len(submissionbody.split("___")) == 7):
            # Get the time
            yardLineField = submissionbody.split("___")[4].split("\n")[4].split("|")[3]
            if(yardLineField.strip() != "50"):
                sideOfField = yardLineField.split("]")[0].split("[")[1]
                yardLine = yardLineField.split("[")[0]
            else:
                return "50"
        else:
            yardLineField = submissionbody.split("___")[3].split("\n")[4].split("|")[3]
            if(yardLineField.strip() != "50"):
                sideOfField = yardLineField.split("]")[0].split("[")[1]
                yardLine = yardLineField.split("[")[0]
            else:
                return "50"
        return sideOfField + " " + yardLine  
    
    """
    Parse the down from the game thread

    """
    def parseDown(submissionbody):
        if(len(submissionbody.split("___")) == 7):
            # Get the time
            down = submissionbody.split("___")[4].split("\n")[4].split("|")[2]
        else:
            down = submissionbody.split("___")[3].split("\n")[4].split("|")[2]
        return down

    """
    Parse what team has the ball from the game thread

    """  
    def parsePossession(submissionbody):
        possession = "home"
        possession = submissionbody.split("___")[4].split("\n")[4].split("|")[4].split("]")[0].split("[")[-1]
        #Iterate through playlist file
        #with open('data.txt', 'r') as csvfile:
        #    reader = csv.reader(csvfile, delimiter= '|', lineterminator='\n')
        #    for row in reader:
        #        if(row[0] != '--------------------------------------------------------------------------------'):
        #            possession = row[5]
        return possession
        
    """
    Parse the time from the game thread

    """
    def parseTime(submissionbody):
        if(len(submissionbody.split("___")) == 7):
            # Get the time
            time = submissionbody.split("___")[4].split("\n")[4].split("|")[0]
        else:
            time = submissionbody.split("___")[4].split("\n")[3].split("|")[0]
        return time 
        
    """
    Parse the home score from the game thread

    """
    def parseAwayScore(submissionbody):
        # Handle various different thread formats
        if(len(submissionbody.split("___")) == 7):
            scoreboard = submissionbody.split("___")[5].split("\n")
            homeTeamScore = scoreboard[4].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 6):
            scoreboard = submissionbody.split("___")[5].split("\n")
            homeTeamScore = scoreboard[4].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 5):
            scoreboard = submissionbody.split("___")[4].split("\n")
            homeTeamScore = scoreboard[4].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 4):
            scoreboard = submissionbody.split("___")[3].split("\n")
            homeTeamScore = scoreboard[4].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 3):
            scoreboard = submissionbody.split("___")[2].split("\n")
            homeTeamScore = scoreboard[3].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 1):
            scoreboard = submissionbody.split("Q4")[1].split("\n")
            homeTeamScore = scoreboard[2].split(" | ")[-1]
            
        return homeTeamScore

    """
    Parse the away score from the game thread

    """
    def parseHomeScore(submissionbody):
        # Handle various different thread formats
        if(len(submissionbody.split("___")) == 7):
            scoreboard = submissionbody.split("___")[5].split("\n")
            awayTeamScore = scoreboard[5].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 6):
            scoreboard = submissionbody.split("___")[5].split("\n")
            awayTeamScore = scoreboard[5].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 5):
            scoreboard = submissionbody.split("___")[4].split("\n")
            awayTeamScore = scoreboard[5].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 4):
            scoreboard = submissionbody.split("___")[3].split("\n")
            awayTeamScore = scoreboard[5].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 3):
            scoreboard = submissionbody.split("___")[2].split("\n")
            awayTeamScore = scoreboard[4].split("**")[1]
            
        elif(len(submissionbody.split("___")) == 1):
            scoreboard = submissionbody.split("Q4")[1].split("\n")
            awayTeamScore = scoreboard[3].split(" | ")[-1]
        return awayTeamScore
        

    """
    Parse the home team from the game thread

    """
    def parseHomeTeam(submissionbody):
        homeTeam = "blank"
        # Handle various different thread formats
        if(len(submissionbody.split("___")) == 7):
            scoreboard = submissionbody.split("___")[5].split("\n")
            homeTeam = scoreboard[4].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 6):
            scoreboard = submissionbody.split("___")[5].split("\n")
            homeTeam = scoreboard[4].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 5):
            scoreboard = submissionbody.split("___")[4].split("\n")
            homeTeam = scoreboard[4].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 4):
            scoreboard = submissionbody.split("___")[3].split("\n")
            homeTeam = scoreboard[4].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 3):
            scoreboard = submissionbody.split("___")[2].split("\n")
            homeTeam = scoreboard[3].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 1):
            scoreboard = submissionbody.split("Q4")[1].split("\n")
            homeTeam = scoreboard[2].split("]")[0]
            homeTeam = homeTeam.replace('[', '')
        return homeTeam

    """
    Parse the away team from the game thread

    """
    def parseAwayTeam(submissionbody):
        awayTeam = "blank"
        # Handle various different thread formats
        if(len(submissionbody.split("___")) == 7):
            scoreboard = submissionbody.split("___")[5].split("\n")
            awayTeam = scoreboard[5].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 6):
            scoreboard = submissionbody.split("___")[5].split("\n")
            awayTeam = scoreboard[5].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 5):
            scoreboard = submissionbody.split("___")[4].split("\n")
            awayTeam = scoreboard[5].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 4):
            scoreboard = submissionbody.split("___")[3].split("\n")
            awayTeam = scoreboard[5].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 3):
            scoreboard = submissionbody.split("___")[2].split("\n")
            awayTeam = scoreboard[4].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
            
        elif(len(submissionbody.split("___")) == 1):
            scoreboard = submissionbody.split("Q4")[1].split("\n")
            awayTeam = scoreboard[3].split("]")[0]
            awayTeam = awayTeam.replace('[', '')
        return awayTeam


    # In[15]:


    def is_fbs(selftext):
        team_pattern = re.compile(r'''
                                (?P<lead>\[)
                                (?P<names>(.*?))
                                (?P<end>\]\(\#f)
                            ''',
                            re.VERBOSE)
        team = re.findall(team_pattern, selftext)
        
        return [team[0][1], team[1][1]]


    # In[16]:


    def find_conference(team):
        if team in AAC:
            return 'AAC'
        elif team in ACC:
            return 'ACC'
        elif team in B1G:
            return 'B1G'
        elif team in BIG12:
            return 'BIG XII'
        elif team in CUSA:
            return 'C-USA'
        elif team in MAC:
            return 'MAC'
        elif team in MWC:
            return 'MWC'
        elif team in PAC12:
            return 'Pac-12'
        elif team in SEC:
            return 'SEC'
        elif team in SUNBELT:
            return 'Sun Belt'
        elif team in Independent:
            return 'Independent'
        else:
            return 'None'


    # In[17]:


    def print_game(submissionbody, home, away):
        out = []
        quarter = parseQuarter(submissionbody)
        time = parseTime(submissionbody)
        home_score = parseHomeScore(submissionbody)
        away_score = parseAwayScore(submissionbody)
        down = parseDown(submissionbody)
        yardline = parseYardLine(submissionbody)
        possession = parsePossession(submissionbody)
        #print(time, quarter, '|', home, away_score, away, home_score)
        #print(down, '| Poss:',possession, ' |',yardline)
        #print('')
        #out.append([time + ' ' + quarter + ' ' + '|' + ' ' + home + ' ' + away_score + ' ' + away + ' ' + home_score + '\n' + down + ' '  +  '| Poss:' + ' ' + possession+ ' ' + ' |' + ' ' + yardline])
        out.append(time + ' ' + quarter + ' ' + '|' + ' ' + home + ' ' + away_score + ' ' + away + ' ' + home_score + '||' + down + ' '  +  '| Poss:' + ' ' + possession+ ' ' + ' |' + ' ' + yardline)
        return out


    # In[26]:


    games_found = {
    'Air Force':0,
    'Akron':0,
    'Alabama':0,
    'Appalachian State':0,
    'Arizona':0,
    'Arizona State':0,
    'Arkansas':0,
    'Arkansas State':0,
    'Army':0,
    'Auburn':0,
    'Ball State':0,
    'Baylor':0,
    'Boise State':0,
    'Boston College':0,
    'Bowling Green':0,
    'Buffalo':0,
    'BYU':0,
    'California':0,
    'Central Michigan':0,
    'Charlotte':0,
    'Cincinnati':0,
    'Clemson':0,
    'Coastal Carolina':0,
    'Colorado':0,
    'Colorado State':0,
    'Connecticut':0,
    'Duke':0,
    'East Carolina':0,
    'Eastern Michigan':0,
    'FAU':0,
    'FIU':0,
    'Florida':0,
    'Florida State':0,
    'Fresno State':0,
    'Georgia':0,
    'Georgia Southern':0,
    'Georgia State':0,
    'Georgia Tech':0,
    'Hawaii':0,
    'Houston':0,
    'Illinois':0,
    'Indiana':0,
    'Iowa':0,
    'Iowa State':0,
    'Kansas':0,
    'Kansas State':0,
    'Kent State':0,
    'Kentucky':0,
    'Liberty':0,
    'Louisiana Tech':0,
    'Louisiana':0,
    'Louisiana–Monroe':0,
    'Louisville':0,
    'LSU':0,
    'Marshall':0,
    'Maryland':0,
    'UMass':0,
    'Memphis':0,
    'Miami (FL)':0,
    'Miami (OH)':0,
    'Michigan':0,
    'Michigan State':0,
    'Middle Tennessee':0,
    'Minnesota':0,
    'Mississippi State':0,
    'Missouri':0,
    'Navy':0,
    'NC State':0,
    'Nebraska':0,
    'Nevada':0,
    'New Mexico':0,
    'New Mexico State':0,
    'North Carolina':0,
    'North Texas':0,
    'Northern Illinois':0,
    'Northwestern':0,
    'Notre Dame':0,
    'Ohio':0,
    'Ohio State':0,
    'Oklahoma':0,
    'Oklahoma State':0,
    'Old Dominion':0,
    'Ole Miss':0,
    'Oregon':0,
    'Oregon State':0,
    'Penn State':0,
    'Pittsburgh':0,
    'Purdue':0,
    'Rice':0,
    'Rutgers':0,
    'San Diego State':0,
    'San Jose State':0,
    'SMU':0,
    'South Alabama':0,
    'South Carolina':0,
    'Southern Mississippi':0,
    'Stanford':0,
    'Syracuse':0,
    'TCU':0,
    'Temple':0,
    'Tennessee':0,
    'Texas':0,
    'Texas A&M':0,
    'Texas State':0,
    'Texas Tech':0,
    'Toledo':0,
    'Troy':0,
    'Tulane':0,
    'Tulsa':0,
    'UAB':0,
    'UCF':0,
    'UCLA':0,
    'UNLV':0,
    'USC':0,
    'USF':0,
    'Utah':0,
    'Utah State':0,
    'UTEP':0,
    'UTSA':0,
    'Vanderbilt':0,
    'Virginia':0,
    'Virginia Tech':0,
    'Wake Forest':0,
    'Washington':0,
    'Washington State':0,
    'West Virginia':0,
    'Western Kentucky':0,
    'Western Michigan':0,
    'Wisconsin':0,
    'Wyoming':0
    }


    upload = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    games = []
    out = []
    test = []
    i = 0
    for submission in subreddit.search("[GAME THREAD]", sort='new', limit=300):
        if "[GAME THREAD]" in submission.title:
            
            games.append(submission)
            home = parseHomeTeam(submission.selftext)
            away = parseAwayTeam(submission.selftext)
            if away == 'Texas A&amp;M':
                away = 'Texas A&M'
            if home == 'Texas A&amp;M':
                home = 'Texas A&M'
            if home in fbs_teams:
                if away in fbs_teams:
                    if games_found[home] != 1:
                        upload.loc[i, 'Game'] = test
                        upload.loc[i, 'Home'] = home
                        upload.loc[i, 'Away'] = away
                        upload.loc[i, 'Home Conference'] = find_conference(home)
                        upload.loc[i, 'Away Conference'] = find_conference(away)
                        upload.loc[i, 'Quarter'] = parseQuarter(submission.selftext)
                        upload.loc[i, 'Time'] = parseTime(submission.selftext)
                        upload.loc[i, 'Away Score'] = parseAwayScore(submission.selftext)
                        upload.loc[i, 'Home Score'] = parseHomeScore(submission.selftext)
                        upload.loc[i, 'Down'] = parseDown(submission.selftext)
                        upload.loc[i, 'Yard Line'] = parseYardLine(submission.selftext)
                        upload.loc[i, 'Possession'] = parsePossession(submission.selftext)
                        upload.loc[i, 'Created_UTC'] = submission.created_utc
                        upload.loc[i, 'URL'] = submission.url
                        if upload.loc[i, 'Home Conference'] == upload.loc[i, 'Away Conference']:
                            upload.loc[i, 'InnerConference'] = 'Yes'
                        else:
                            upload.loc[i, 'InnerConference'] = 'No'
                        upload.loc[i, 'ConfConcat'] = upload.loc[i, 'Home Conference'] + upload.loc[i, 'Away Conference']
                        i += 1
                        games_found[home] = 1
                        games_found[away] = 1
                        
    conf = pd.DataFrame(columns = ['Home', 'Conference'])
    j = 0
    for i in range(0, len(upload)):
        if upload.loc[i, 'InnerConference'] == 'Yes':
            conf.loc[j, 'Home'] = upload.loc[i, 'Home']
            conf.loc[j, 'Conference'] = upload.loc[i, 'Home Conference']
            j += 1        
            #print('Yes')
        else:
            conf.loc[j, 'Home'] = upload.loc[i, 'Home']
            conf.loc[j, 'Conference'] = upload.loc[i, 'Home Conference']
            #print(j, conf.loc[j, 'Home'], conf.loc[j, 'Conference'])
            j += 1
            conf.loc[j, 'Home'] = upload.loc[i, 'Home']
            conf.loc[j, 'Conference'] = upload.loc[i, 'Away Conference']
            #print(j, conf.loc[j, 'Home'], conf.loc[j, 'Conference'], upload.loc[i])
            j += 1
            #print('No')
    #print(conf.tail(40), len(conf))



    aac_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    acc_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    b1g_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    big12_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    cusa_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    mac_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    mwc_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    pac_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    sec_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    sun_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])
    ind_games = pd.DataFrame(columns = ['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Home Score', 'Away Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL'])


    j = 0

    # Break games into tables by conference
    for i in range(0, len(conf)):
        if conf.loc[i, 'Conference'] == 'AAC':
            aac_games = aac_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'ACC':
            acc_games = acc_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'B1G':
            b1g_games = b1g_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'BIG XII':
            big12_games = big12_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'C-USA':
            cusa_games = cusa_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'MAC':
            mac_games = mac_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'MWC':
            mwc_games = mwc_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'Pac-12':
            pac_games = pac_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'SEC':
            sec_games = sec_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'Sun Belt':
            sun_games = sun_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
        elif conf.loc[i, 'Conference'] == 'Independent':
            ind_games = ind_games.append(upload.loc[upload['Home'] == conf.loc[i, 'Home']])
    #print(ind_games)
    aac_games = aac_games.reset_index(drop=True)
    acc_games = acc_games.reset_index(drop=True)
    b1g_games = b1g_games.reset_index(drop=True)
    cusa_games = cusa_games.reset_index(drop=True)
    mac_games = mac_games.reset_index(drop=True)
    mwc_games = mwc_games.reset_index(drop=True)
    pac_games = pac_games.reset_index(drop=True)
    sec_games = sec_games.reset_index(drop=True)
    sun_games = sun_games.reset_index(drop=True)
    ind_games = ind_games.reset_index(drop=True)

    #print(sun_games)

    #Sort by game start time
    aac_games['Created_UTC'] = aac_games['Created_UTC'].astype(float)
    aac_games = aac_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    acc_games['Created_UTC'] = acc_games['Created_UTC'].astype(float)
    acc_games = acc_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    b1g_games['Created_UTC'] = b1g_games['Created_UTC'].astype(float)
    b1g_games = b1g_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    big12_games['Created_UTC'] = big12_games['Created_UTC'].astype(float)
    big12_games = big12_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    cusa_games['Created_UTC'] = cusa_games['Created_UTC'].astype(float)
    cusa_games = cusa_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    mac_games['Created_UTC'] = mac_games['Created_UTC'].astype(float)
    mac_games = mac_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    mwc_games['Created_UTC'] = mwc_games['Created_UTC'].astype(float)
    mwc_games = mwc_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    pac_games['Created_UTC'] = pac_games['Created_UTC'].astype(float)
    pac_games = pac_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    sec_games['Created_UTC'] = sec_games['Created_UTC'].astype(float)
    sec_games = sec_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    sun_games['Created_UTC'] = sun_games['Created_UTC'].astype(float)
    sun_games = sun_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    ind_games['Created_UTC'] = ind_games['Created_UTC'].astype(float)
    ind_games = ind_games.groupby('Home', group_keys=False).apply(lambda x: x.loc[x.Created_UTC.idxmax()])

    aac_games = aac_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    acc_games = acc_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    b1g_games = b1g_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    big12_games = big12_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    cusa_games = cusa_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    mac_games = mac_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    mwc_games = mwc_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    pac_games = pac_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    sec_games = sec_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    sun_games = sun_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]
    ind_games = ind_games[['Game', 'ConfConcat', 'Home', 'Away', 'Home Conference', 'Away Conference', 'InnerConference', 'Quarter', 'Time', 'Away Score', 'Home Score', 'Down', 'Yard Line', 'Possession', 'Created_UTC', 'URL']]


    aac_games = aac_games.reset_index(drop=True)
    acc_games = acc_games.reset_index(drop=True)
    b1g_games = b1g_games.reset_index(drop=True)
    big12_games = big12_games.reset_index(drop=True)
    cusa_games = cusa_games.reset_index(drop=True)
    mac_games = mac_games.reset_index(drop=True)
    mwc_games = mwc_games.reset_index(drop=True)
    pac_games = pac_games.reset_index(drop=True)
    sec_games = sec_games.reset_index(drop=True)
    sun_games = sun_games.reset_index(drop=True)
    ind_games = ind_games.reset_index(drop=True)

    aac_dict = []
    acc_dict = []
    b1g_dict = []
    big12_dict = []
    cusa_dict = []
    mac_dict = []
    mwc_dict = []
    pac_dict = []
    sec_dict = []
    sun_dict = []
    ind_dict = []

    for index, game in aac_games.iterrows():
        aac_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in acc_games.iterrows():
        acc_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in b1g_games.iterrows():
        b1g_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in big12_games.iterrows():
        big12_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in cusa_games.iterrows():
        cusa_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in mac_games.iterrows():
        mac_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in mwc_games.iterrows():
        mwc_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in pac_games.iterrows():
        pac_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in sec_games.iterrows():
        sec_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in sun_games.iterrows():
        sun_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})
    for index, game in ind_games.iterrows():
        ind_dict.append({'Home': game['Home'], 'Away': game['Away'], 'Home Conference': game['Home Conference'], 'Away Conference': game['Away Conference'], 'InnerConference': game['InnerConference'], 'Quarter': game['Quarter'], 'Time':game['Time'], 'Away Score': game['Home Score'], 'Home Score':game['Away Score'], 'Down': game['Down'], 'Yard Line': game['Yard Line'], 'Possession':game['Possession'], 'Created_UTC':game['Created_UTC'], 'URL':game['URL']})



    # from datetime import datetime
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    #print("Current Time =%s", utc_timestamp) #, current_time)

    return aac_dict, acc_dict, b1g_dict, big12_dict, cusa_dict, mac_dict, mwc_dict, pac_dict, sec_dict, sun_dict, ind_dict 

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
