import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# Get data from auth.csv
log = pd.read_csv('auth.csv')

# Twitter API credentials
consumerKey = log['consumerKey'][0]
consumerSecret = log['consumerSecret'][0]
accessToken = log['accessToken'][0]
accessTokenSecret = log['accessTokenSecret'][0]

# authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# setting the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# API object to pass in th auth info
api = tweepy.API(authenticate, wait_on_rate_limit=True)

# Extract 100 tweets from the twitter user
posts = api.user_timeline(screen_name="billgates", count=100, lang="en", tweet_mode="extended")
print("Show the 5 recent tweets: \n")
i = 1
for tweet in posts[0:5]:
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i + 1

df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
print(df.head())


# clean data function
def cleanData(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove @mentions
    text = re.sub(r'#', '', text)  # remove # symbol
    text = re.sub(r'RT[\s]+', '', text)  # remove RT
    text = re.sub(r'https?:\/\/\S+', '', text)  # remove the links

    return text


df['Tweets'] = df['Tweets'].apply(cleanData)


# get the subjectivity function
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity


# get the polarity function
def getPolarity(text):
    return TextBlob(text).sentiment.polarity


# create 2 new columns
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)

print(df)
