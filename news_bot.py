
import requests as r
from bs4 import BeautifulSoup
import time
import praw

username="10724748"
password="123456"

sub="worldnews"

used_articles=[]

print "Initializing..."

user_agent = ("Reddit News Publication Machine v1.3 by /u/patsoldier") #Every reddit bot has to have this to identify itself

def post(i,link):
    #suggested links: http://www.bbc.com/news and http://www.bbc.co.uk/news/world/middle_east

    localtime = time.asctime( time.localtime(time.time()) )
    print "Local current time :", localtime
    
    i=str(i)
    i=GetStory() 

    
    all_contents=i.get_all()

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



def post_news(subreddit,title,article_link):
    r = praw.Reddit(user_agent=user_agent)
    r.login(username,password)
    r.submit(subreddit,title,text=None,url=article_link)



class GetStory:


    def get_clickbait_line(self):

        raw=soup.find_all(id="top-story")[0]
        #This gets the subsection with the information of the "top story".
        #The find all command finds all the sections with the top story id in the soup.
        clickbait_line.span.decompose()
        #The line above deletes the contents of the <span> tag, which we will need for later.
        return clickbait_line.p.get_text()
        #this then gets us the contents of the <p> tag which has the clickbait line.
        #Within p was the span tag, which is why we had to delete it.
        #Get_text returns the text as a string.

    def get_headline(self):
        
        article_headline=soup.find_all(id="top-story")[0]
        return article_headline.find("a").get_text()
        #find only gets the first tag with the tag <a> (in this case).

    def get_link(self):
        
        article_link=soup.find_all(id="top-story")[0]
        return "http://www.bbc.com" + article_link.find("a")["href"]
        #The href command like this, like the rel below, gets us the contents of a tag.

    def get_id(self):
        article_id=soup.find_all(id="top-story")[0]
        return article_id.a["rel"]

    def get_all(self):
        all_contents=[]
        
        raw=soup.find_all(id="top-story")[0]

        raw.span.decompose()
        all_contents.append(raw.p.get_text(strip=True))

        
        all_contents.append(raw.find("a").get_text(strip=True))

        
        all_contents.append("http://www.bbc.com" + raw.find("a")["href"])

    
        all_contents.append(raw.a["rel"][0])

        return all_contents




for i in range(1000):
    time.sleep(500)
    link1="http://www.bbc.com/news"
    link2="http://www.bbc.co.uk/news/world/middle_east"
    link3="http://www.bbc.co.uk/news/world/europe/"

    print "Retrieving Link1..."
    page=r.get(link1).text #This gets the page that you will be scraping.
    soup=BeautifulSoup(page) #Prepares the "soup" that well be working on in a format bs4 can work with.
    post(i,link1)

    print "Retrieving Link2..."
    page=r.get(link2).text #This gets the page that you will be scraping.
    soup=BeautifulSoup(page) #Prepares the "soup" that well be working on in a format bs4 can work with.
    post(i+1, link2)

    print "Retrieving Link3..."
    page=r.get(link2).text #This gets the page that you will be scraping.
    soup=BeautifulSoup(page) #Prepares the "soup" that well be working on in a format bs4 can work with.
    post(i+1, link2)


    
    




    
