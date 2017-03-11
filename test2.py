# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:13:52 2017

@author: adeja_000
"""
import os
import json
from twitter import Api

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
ckey = "dyEUd6eufLlQjQI88nV2yK08T"
csecret = "SntWGRiUuiWCHCRPh3CuQZXyeUGnZD4elDV7s7Y4MeE4G0PkEn"
atoken = "822730674671128577-aj28Ykky6KpagwRk6DZe0Yew2ode0o6"
asecret = "u5i6a60yEKsk4WZ2oKqUpyKRZx5KvkwlyiUAhZK8hONO6"



OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
    'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)



USERS = ['@twitter',
         '@twitterapi',
         '@support']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']

# Since we're going to be using a streaming endpoint, there is no need to worry
# about rate limits.


#for line in api.GetSearch(track=USERS, languages=LANGUAGES):
#    print(line)
#public_tweets = api.home_timeline()
#
#cat=api.suggested_categories()
#print(len(public_tweets))
#
#for  i in range(len(cat)):
#     print(cat[i].name)
#
#for tweet in public_tweets:
#    print (tweet.text)
#    
#    
#user = api.get_user('DonaldTrump')
#
#print (user.screen_name)
#print ("followers: ", user.followers_count)
##print ("tweets: ", user.usertimeline)
#
#for tweet in public_tweets:
#    print (tweet.text)
#    
#for friend in user.friends():
#   print (friend.screen_name)