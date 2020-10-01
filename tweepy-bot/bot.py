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

# creating a MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)

# making GET request to github API
response = requests.get("https://api.github.com/search/issues?q=label:hacktoberfest+is:issue+is:open&sort=updated&order=desc")
print(response.status_code)


all_items = response.json()['items']

def humanize_url(url):
    h_url = url[:8]+"github.com/"+url[29:]
    return h_url


for i in range(0,len(all_items)):
    url = humanize_url(all_items[i]["url"])
    dict = {"url":url}
    print(i+1)
    print(all_items[i]["title"] + "\n" + url)
    print("\n")



# update the status
# api.update_status(status ="Happy hacktober Everyone!")
