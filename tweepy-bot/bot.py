#this is the code for
# importing the module
import tweepy

# personal details
consumer_key ="dKRVYTRotNt0Xe2Cy3oFfhybw"
consumer_secret ="AcRg9XqEe3x2bZO3C2Ce4rpd7KvuTtvj3dtsguU6iNlLY79v11"
access_token ="1311544857941274626-L8zWYVKwL8p4glQhvY1dD4RdHSLG6r"
access_token_secret ="BcdkoB33j0MxSZDiYylW1AE1K5aQaDcp9Rjip4aCBHYpb"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update the status
api.update_status(status ="Happy hacktober Everyone!")
