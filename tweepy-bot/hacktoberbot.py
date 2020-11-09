import tweepy
import requests
import json
import logging
import time
import schedule
from config import create_api
from database import get_issue,insert_data,clear_database
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# making GET request to github API
def make_req():
    response = requests.get("https://api.github.com/search/issues?q=label:hacktoberfest+is:issue+is:open&sort=updated&order=desc")
    return response



def humanize_url(url):
    h_url = url[:8]+"github.com/"+url[29:]
    return h_url


def tweet(api):
    new_issues = make_req().json()['items']
    for i in range(0,len(new_issues)):
        url = humanize_url(new_issues[i]["url"])
        title = new_issues[i]["title"]
        insert_data(title,url)
        twt = get_issue()
        try:
            api.update_status(status = twt)
            logger.info("Tweet Posted!")
        except tweepy.TweepError as error:
            if error.api_code == 187:
                logger.error("Dublicate tweet!")
            else:
                raise error

def database_del():
    '''
    i seriously have no idea why schedule wants it like this :(
    '''
    clear_database()


schedule.every(15).days.do(database_del) # runs the clean database module evey 30 days

def main():
    api = create_api()
    while True:
        tweet(api)
        logger.info("Waiting...")
        schedule.run_pending() # Checks whether a scheduled task is pending to run or not 
        time.sleep(60)

        
         
    

if __name__ == "__main__":
    main()
