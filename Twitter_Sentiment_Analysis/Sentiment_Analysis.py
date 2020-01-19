from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt
import my_credentials as cred

def prcentage(a,b):
    return 100*float(a)/float(b)

#ConsumerKey = 'K4WQgEg4dWGwKQVzfQ1baoN6L'
#ConsumerToken = 'zom6nfkY4wsQxpKlXSrL5YJCE8Zg4apsA5hiBpl59mT09QNztA'
#AccessToken = '275589155-EgMU7NucJhDlc9PLq0fNZAUgsfy6cGlO3ompRhh6'
#AccessTokenSecret='NnyJ0GttdLSZnDTcNO1jxHZO65j1h6M6J0ETlJk7j95Gb'

auth = tweepy.OAuthHandler(cred.ConsumerKey,cred.ConsumerToken)

auth.set_access_token(cred.AccessToken,cred.AccessTokenSecret)

API = tweepy.API(auth)

SearchWord = input("Enter the Key word to Search:")
NOfSearch = int(input('Enter the number of searches you want to make:'))
tweets  = tweepy.Cursor(API.search,q=SearchWord).items(NOfSearch)

neutral = 0
negative=0
positive = 0
for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment.polarity)
    if (analysis.sentiment.polarity==0):
        neutral+=1
    elif (analysis.sentiment.polarity<0):
        negative += 1
    elif (analysis.sentiment.polarity>0):
        positive += 1

print(neutral,' ',negative,' ',positive)
        