#this is the code for importing the module
import tweepy
import requests
import json
# personal details
consumer_key ="dKRVYTRotNt0Xe2Cy3oFfhybw"
consumer_secret ="AcRg9XqEe3x2bZO3C2Ce4rpd7KvuTtvj3dtsguU6iNlLY79v11"
access_token ="1311544857941274626-L8zWYVKwL8p4glQhvY1dD4RdHSLG6r"
access_token_secret ="BcdkoB33j0MxSZDiYylW1AE1K5aQaDcp9Rjip4aCBHYpb"


# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)

#making GET request to github API
response = requests.get("https://api.github.com/search/issues?q=label:hacktoberfest+is:issue+is:open&sort=updated&order=desc")
print(response.status_code)
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json()['items'][0]["title"])
jprint(response.json()['items'][0]["url"])

api = tweepy.API(auth)

# update the status
# api.update_status(status ="Happy hacktober Everyone!")
