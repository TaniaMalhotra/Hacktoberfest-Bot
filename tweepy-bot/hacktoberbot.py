import tweepy
import requests
import json
import logging
import time
from config import create_api
from database import insert_data, del_last_data, get_last_data
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
        twt = get_last_data()
        try:
            api.update_status(status = twt)
            logger.info("Tweet Posted!")
            del_last_data()
        except tweepy.TweepError as error:
            if error.api_code == 187:
                # Do something special
                logger.info("Dublicate tweet, Issue Deleted From database")
                del_last_data()
            else:
                raise error

def main():
    api = create_api()
    while True:
        tweet(api)
        logger.info("Waiting...")
        time.sleep(60)
    

if __name__ == "__main__":
    main()
