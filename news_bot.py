###################################################
################### Modules #######################
###################################################

import requests as r
from bs4 import BeautifulSoup
import time
import praw

###################################################
################### Configuration #################
###################################################

username="10724748"
password="password"

sub="worldnews"

r = praw.Reddit(user_agent=user_agent)

used_articles=[]
links=["http://www.bbc.com/news","http://www.bbc.co.uk/news/world/middle_east","http://www.bbc.co.uk/news/world/europe/"]

user_agent = ("Reddit News Publication Machine v1.3 by /u/patsoldier") #Every reddit bot has to have this to identify itself

###################################################
################### Functions #####################
###################################################


def login(username,password):
    r.login(username,password)

def post_news(subreddit,title,article_link):
    r.submit(subreddit,title,text=None,url=article_link)


    
def get_all(link):
    all_contents=[]
    
    page=r.get(link).text #This gets the page that you will be scraping.
    soup=BeautifulSoup(page) #Prepares the "soup" that well be working on in a format bs4 can work with.
    raw=soup.find_all(id="top-story")[0].span.decompose()
    
    all_contents.append(raw.p.get_text(strip=True))
    all_contents.append(raw.find("a").get_text(strip=True))
    all_contents.append("http://www.bbc.com" + raw.find("a")["href"])
    all_contents.append(raw.a["rel"][0])
    return all_contents



    
def post(link):
    
    all_contents=get_all(link)

    if all_contents[3] not in used_articles:

        try:

            title=all_contents[0]
            link=all_contents[2]
            
            post_news(sub,title,link)
            used_articles.append(all_contents[3])

            print "Succesfully posted: " +title

        except praw.errors.AlreadySubmitted:
            print "Article " + str(all_contents[3])+" has already been posted to reddit and reddit told us this."
            used_articles.append(all_contents[3])

    else:
        print "Article " + str(all_contents[3])+" has already been posted to reddit."
    time.sleep(600)
    
    
###################################################
################### Main Loop #####################
###################################################

login(username,password)

while True:
    for i in links:
        post(i)
        
    
    




    
