# this is the code for importing the module
import tweepy
import requests
import logging
import time
from config import create_api
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# making GET request to github API
def make_req():
    response = requests.get("https://api.github.com/search/issues?q=label:"
                            "hacktoberfest+is:issue+is:open&"
                            "sort=updated&order=desc")
    return response


prev_issues = []

# because I need to index a blank list later
for i in range(0, 30):
    prev_issues.append("")


def humanize_url(url):
    h_url = url[:8]+"github.com/"+url[29:]
    return h_url


def tweet(api):
    print("next call")
    new_issues = make_req().json()['items']
    current_issues = []
    match = False
    for i in range(0, len(new_issues)):
        url = humanize_url(new_issues[i]["url"])
        for j in range(0, len(prev_issues)):
            if prev_issues[j] == url:
                match = True
                # print("match is found for " + url + "in prev_issues array "
                #                                    "at position "+str(j))
        if not match:
            twt = new_issues[i]["title"] + "\n" + url
            try:
                api.update_status(status=twt)
            except tweepy.TweepError as error:
                if error.api_code == 187:
                    # Do something special
                    print('duplicate message')
                else:
                    raise error
            print(i+1)
            print(twt)
            print("\n")

        current_issues.append(url)

    for i in range(0, len(current_issues)):
        prev_issues[i] = current_issues[i]

    # print("previous issues array")
    # for i in range(0,len(prev_issues)):
    #     print(prev_issues[i])


def main():
    api = create_api()
    while True:
        tweet(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()

# update the status
# api.update_status(status ="Happy hacktober Everyone!")
