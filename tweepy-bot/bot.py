# this is the code for importing the module
import tweepy
import requests
import logging
import time
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def make_req():                                      # makes get request for issues and returns it
    response = requests.get("https://api.github.com/search/issues?q=label:"
                            "hacktoberfest+is:issue+is:open&"
                            "sort=updated&order=desc")
    return response


prev_issues = []

# because I need to index a blank list later
for i in range(0, 30):                               # add 30 blank indexes to previous issues
    prev_issues.append("")


def humanize_url(url):                               # reformat url
    h_url = url[:8] + "github.com/" + url[29:]
    return h_url


def tweet(api):
    print("next call")
    new_issues = make_req().json()['items']          # stores new issues array into variable
    current_issues = []
    match = False
    for i in range(0, len(new_issues)):              # checks for issues previously included within the last set
        url = humanize_url(new_issues[i]["url"])     # gets usable url
        for j in range(0, len(prev_issues)):         # compares previous issues with the new issue using url
            if prev_issues[j] == url:
                match = True
                # print("match is found for " + url + "in prev_issues array "
                #                                    "at position "+str(j))
        if not match:                                # if issue was not previously included, then tweet the new issue.
            twt = new_issues[i]["title"] + "\n" + url    # stores issue into string 'twt'
            try:
                api.update_status(status=twt)        # sends the tweet with variable 'twt'
            except tweepy.TweepError as error:       # catch error when tweeting
                if error.api_code == 187:            # assume error as duplicate message, then prints
                    # Do something special
                    print('duplicate message')
                else:
                    raise error
            print(i + 1)
            print(twt)
            print("\n")

        current_issues.append(url)                   # add the issue into current issues

    for i in range(0, len(current_issues)):          # replace previous issues with current issues
        prev_issues[i] = current_issues[i]

    # print("previous issues array")
    # for i in range(0,len(prev_issues)):
    #     print(prev_issues[i])


def main():
    api = create_api()
    while True:                                      # run tweet loop, runs every 30 seconds, indefinitely
        tweet(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()                                           # run main method

# update the status
# api.update_status(status ="Happy hacktober Everyone!")
