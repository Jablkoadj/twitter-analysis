# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:53:12 2017

@author: adeja_000
"""

from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="	dyEUd6eufLlQjQI88nV2yK08T"
consumer_secret="SntWGRiUuiWCHCRPh3CuQZXyeUGnZD4elDV7s7Y4MeE4G0PkEn"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="822730674671128577-xydCzcI3B76pAKfl9ifglryPusUTjA"
access_token_secret="Am7w8BlGxnfOaWxcRXRF0PFW1MyUYcd7TmuMId4b3KFxz"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print("error", status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    print("test1")
    auth.set_access_token(access_token, access_token_secret)
    print("test2")
    stream = Stream(auth, l)
    print("test3")
    stream.sample