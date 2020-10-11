# this is the code for importing the module
import tweepy
import requests
import json
import pymongo
# personal details
consumer_key ="dKRVYTRotNt0Xe2Cy3oFfhybw"
consumer_secret ="AcRg9XqEe3x2bZO3C2Ce4rpd7KvuTtvj3dtsguU6iNlLY79v11"
access_token ="1311544857941274626-L8zWYVKwL8p4glQhvY1dD4RdHSLG6r"
access_token_secret ="BcdkoB33j0MxSZDiYylW1AE1K5aQaDcp9Rjip4aCBHYpb"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)

# making GET request to github API
response = requests.get("https://api.github.com/search/issues?q=label:hacktoberfest+is:issue+is:open&sort=updated&order=desc")
print(response.status_code)

prev_issues = []
new_issues = response.json()['items']

#because I need to index a blank list later
for i in range(0,len(new_issues)):
    prev_issues.append("")

def humanize_url(url):
    h_url = url[:8]+"github.com/"+url[29:]
    return h_url


for i in range(0,3):
    current_issues = []
    match = False
    for i in range(0,len(new_issues)):
        url = humanize_url(new_issues[i]["url"])
        for j in range(0,len(prev_issues)):
            if prev_issues[j] == url:
                match = True
        if not match:
            current_issues.append(url)
            print(i+1)
            print(new_issues[i]["title"] + "\n" + url)
            print("\n")



    for i in range(0,len(current_issues)):
        prev_issues[i] = current_issues[i]



# update the status
# api.update_status(status ="Happy hacktober Everyone!")
