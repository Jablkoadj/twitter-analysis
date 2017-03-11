# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 20:23:25 2017

@author: adeja_000
"""

import tweepy
import time
import csv
import pprint as pp
import re
import pandas as pd
from nltk.collocations import *
from nltk.corpus import stopwords
import sqlite3

ckey = "dyEUd6eufLlQjQI88nV2yK08T"
csecret = "SntWGRiUuiWCHCRPh3CuQZXyeUGnZD4elDV7s7Y4MeE4G0PkEn"
atoken = "822730674671128577-aj28Ykky6KpagwRk6DZe0Yew2ode0o6"
asecret = "u5i6a60yEKsk4WZ2oKqUpyKRZx5KvkwlyiUAhZK8hONO6"



OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
    'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

TweetDb='Tweet2.db'

ColumnName =('query_search',\
        'created_at',\
        'in_reply_to_screen_name',\
        'text',\
        'in_reply_to_user_id_str',\
        'lang', \
        'coordinates',\
        'id_str',\
        'retweeted',\
        'in_reply_to_user_id',\
        'user',\
        'in_reply_to_status_id_str',\
        'is_quote_status',\
        'contributors',\
        'id',\
        'in_reply_to_status_id',\
        'possibly_sensitive',\
        'favorited',\
        'entities',\
        'place',\
        'truncated',\
        'retweet_count',\
        'retweeted_status',\
        'favorite_count',\
        'metadata',\
        'geo',\
        'source')

# Stream the first "xxx" tweets related to "car", then filter out the ones without geo-enabled
# Reference of search (q) operator: https://dev.twitter.com/rest/public/search

def OLDCollect_author_tweet(authorsearch,endUntil,num):
    
    counter2 = 0
    print ("start author collect")
    suffix = str(endUntil)+'.csv'
    
    for tweet in tweepy.Cursor(api.user_timeline,id=authorsearch,until=endUntil).items(num): # changeable here
    
        try:
#            print ("Text:", tweet._json['text'].encode('utf-8'))  
#            print ("Text:", tweet._json['text'])
#            print ("Screen-name:", tweet._json['user']['screen_name'].encode('utf-8'))
#            print ("Tweet created:", tweet._json['created_at'].encode('utf-8'))
    
    
            placeHolder = []
            placeHolder.append(tweet._json['text'])
            placeHolder.append(tweet._json['user']['screen_name'])
            placeHolder.append(tweet._json['created_at'])
            placeHolder.append(list(hashtag['text'] for hashtag in tweet.entities.get('hashtags')))
            placeHolder.append(tweet.user.location)
            placeHolder.append(tweet._json['retweet_count'])

            prefix = 'TweetauthorData'+ authorsearch
            wholeFileName = prefix + suffix     
            with open(wholeFileName, "at",encoding="utf-8") as f: # changeable here
                writeFile = csv.writer(f)
                writeFile.writerow(placeHolder)
    
            counter2 += 1
            
            if counter2 == 4000:
                print('wait for 20 min everytime 4,000 tweets are extracted ',counter2)
                time.sleep(60*20) 
                counter2 = 0
                continue
    
        except tweepy.TweepError:
            print('wait for 20 min  ',counter2)
            time.sleep(60*20)
            continue
    
        except IOError:
            print('wait for 3 min  ',counter2)
            time.sleep(60*2.5)
            continue
    
        except StopIteration:
            break
#        finally:
#            return counter2
#    return counter2


def OLDCollect_tweet(querysearch,endUntil,num):
    counter2 = 0
    print ("start:")
    suffix = str(endUntil)+'.csv'
    
    for tweet in tweepy.Cursor(api.search,q=querysearch,until=endUntil).items(num): # changeable here
    
        try:
#            print ("Text:", tweet._json['text'].encode('utf-8'))  
#            print ("Text:", tweet._json['text'])
#            print ("Screen-name:", tweet._json['user']['screen_name'].encode('utf-8'))
#            print ("Tweet created:", tweet._json['created_at'].encode('utf-8'))
    
    
            placeHolder = []
            placeHolder.append(tweet._json['text'])
            placeHolder.append(tweet._json['user']['screen_name'])
            placeHolder.append(tweet._json['created_at'])
            placeHolder.append(list(hashtag['text'] for hashtag in tweet.entities.get('hashtags')))
            placeHolder.append(tweet.user.location)
            placeHolder.append(tweet._json['retweet_count'])

            prefix = 'TweetData'+ querysearch
            wholeFileName = prefix + suffix     
            with open(wholeFileName, "at",encoding="utf-8") as f: # changeable here
                writeFile = csv.writer(f)
                writeFile.writerow(placeHolder)
    
            counter2 += 1
            
            if counter2 == 4000:
                print('wait for 20 min everytime 4,000 tweets are extracted ',counter2)
                time.sleep(60*20) 
                counter2 = 0
                continue
    
        except tweepy.TweepError:
            print('wait for 20 min  ',counter2)
            time.sleep(60*20)
            continue
    
        except IOError:
            print('wait for 3 min  ',counter2)
            time.sleep(60*2.5)
            continue
    
        except StopIteration:
            break
#        finally:
#            return counter2
#    return counter2

 
 
def read_collected_tweet(wholeFileName):
    counter2 = 0
    print ("start:")
  
    with open(wholeFileName, "rt",encoding="utf-8") as f: # changeable here
                readfile = f.read()
                print(readfile)
            
    
# In[2]:

def test_text_analysis(wholeFileName):
    # Build a JSON array
    data =  open(wholeFileName,'r').readlines()
#    print(data)
    # Create a pandas DataFrame (think: 2-dimensional table) to get a 
    # spreadsheet-like interface into the data
    
#    df = pd.read_json(data, orient='records')
    
    print ("Successfully imported", len(df), "tweets")
    return (data)

# In[3]:


def getstatus():
    i=0
    for status in statuses:
        # process status here
        pp.pprint(status)
        pp.pprint(('NEXT {0}').format(i))
        i+=1
    return status    

# In[8]:

def getuser_mentions():
    i=0      
    for status in statuses:
        # process status here
        pp.pprint(status.user_mentions)
        pp.pprint(('NEXT {0}').format(i))
        i+=1


def Collect_author_tweet(authorsearch,endUntil,num):
    
    print(('opening Tweet DB for {0} {1} {2}').format(authorsearch,endUntil,num))
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()
    
    i=0
  

    SQLQUERY="INSERT INTO TweetCollector "+ str(ColumnName)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 

    
    for tweet in tweepy.Cursor(api.user_timeline,id=authorsearch,until=endUntil).items(num): # changeable here
        try:
            tweetvalue=[]
            z=1
            originalnum=0
            for jsonkey in ColumnName:
                jsonkey=str(jsonkey)
                try:
                    if (jsonkey=='retweeted_status'):
#                       print(jsonkey,' initial id = ',tweet._json[jsonkey]['id'])
                       tweetvalue.append(tweet._json[jsonkey]['id'])
                       originalnum=tweet._json[jsonkey]['id']
#                       print('######################  ', i,' Original Tweet number; ',tweet._json[jsonkey]['id'])    
                    
                    elif (jsonkey=='query_search'):
                       tweetvalue.append(str(authorsearch))
                   
                    elif (type(tweet._json[jsonkey])==dict):
#                       print(z,"  ",jsonkey,' = ',tweet._json[jsonkey])
                       tweetvalue.append(str(tweet._json[jsonkey]))
                       z+=1
                    else:
    #                   print(z,"  ",jsonkey,' = ',type(tweet._json[jsonkey]))
                       tweetvalue.append(tweet._json[jsonkey])
                       z+=1
                except:
#                    print('Value not found ',jsonkey )
                    tweetvalue.append('NULL')
                   
            
    #        print(str(ColumnName))
    #        print(SQLQUERY)
    #        print(tweetvalue[9])
            
            try:
                i+=1
                c.execute(SQLQUERY,tweetvalue)
                conn.commit()
                print('||||||||||| SUCCESSFULL ',i )
                if originalnum > 0: 
                    Get_original_tweet(originalnum,authorsearch)
                    i+=1
                
                
            except :
                print('-----------FAILURE Tweet number;',i, str(ValueError))
                print(str(conn.OperationalError))
                conn.rollback()
           
#            print('###################### Tweet number;',i)
            
            tweetvalue=[]
            z=1
    
        except tweepy.TweepError:
            print('wait for 20 min  ',counter2)
            time.sleep(60*20)
            continue
    
        except IOError:
            print('wait for 3 min  ',counter2)
            time.sleep(60*2.5)
            continue
    
        except StopIteration:
            break             
    
    print('END ||||||||||||||||||  nb Tweet collected;',i, authorsearch)        
    conn.close()    
    

def Collect_tweet(querysearch,endUntil,num):
    
   
       
    print(('opening Tweet DB for {0} {1} {2}').format(querysearch,endUntil,num))
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()
    
    i=0
  

    SQLQUERY="INSERT INTO TweetCollector "+ str(ColumnName)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 



    for tweet in tweepy.Cursor(api.search,q=querysearch,until=endUntil).items(num):  
        try:
            tweetvalue=[]
            z=1
            originalnum=0
            for jsonkey in ColumnName:
                jsonkey=str(jsonkey)
                try:
                    if (jsonkey=='retweeted_status'):
    #                   print(jsonkey,' initial id = ',type(tweet._json[jsonkey]['id'])
                       tweetvalue.append(tweet._json[jsonkey]['id'])
                       originalnum=tweet._json[jsonkey]['id']
#                       print('######################  ', i,' Original Tweet number; ',tweet._json[jsonkey]['id'])    
                    
                    elif (jsonkey=='query_search'):
                       tweetvalue.append(str(querysearch))
                   
                    elif (type(tweet._json[jsonkey])==dict):
    #                   print(z,"  ",jsonkey,' = ',type(tweet._json[jsonkey]))
                       tweetvalue.append(str(tweet._json[jsonkey]))
                       z+=1
                    else:
    #                   print(z,"  ",jsonkey,' = ',type(tweet._json[jsonkey]))
                       tweetvalue.append(tweet._json[jsonkey])
                       z+=1
                except:
#                    print('Value not found ',jsonkey )
                    tweetvalue.append('NULL')
                   
            
    #        print(str(ColumnName))
    #        print(SQLQUERY)
    #        print(tweetvalue[9])
            
            try:
                i+=1
                c.execute(SQLQUERY,tweetvalue)
                conn.commit()
#                print('||||||||||| SUCCESSFULL ',i )
                if originalnum > 0: 
                    Get_original_tweet(originalnum,querysearch)
                    i+=1
                
                
            except :
#                print('-----------FAILURE Tweet number;',i, str(ValueError))
#                print(str(conn.OperationalError))
                conn.rollback()
           
#            print('###################### Tweet number;',i)
            
            tweetvalue=[]
            z=1
    
        except tweepy.TweepError:
            print('wait for 20 min  ',counter2)
            time.sleep(60*20)
            continue
    
        except IOError:
            print('wait for 3 min  ',counter2)
            time.sleep(60*2.5)
            continue
    
        except StopIteration:
            break             
    
    print('END ||||||||||||||||||  nb Tweet collected;',i, querysearch)        
    conn.close()    
    
def  Get_original_tweet(num,querysearch):
    
#    try:
#        conn.close()
#        conn.rollback()
#    
#    except:
##        print('Db is Closed')   
        
#    print(' Tweet for id ', querysearch)   
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()
    
    i=1
    j=0
    
    initialtweet={}
   

    SQLQUERY="INSERT INTO TweetCollector "+ str(ColumnName)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 

## Save (commit) the changes

    tweet = api.get_status(num)
    tweetvalue=[]
    z=1
    for jsonkey in ColumnName:
        jsonkey=str(jsonkey)
        try:
            if (jsonkey=='retweeted_status'):
#                   print(jsonkey,' initial id = ',type(tweet._json[jsonkey]['id'])
               tweetvalue.append(tweet._json[jsonkey]['id'])
               initialtweet[j]=tweet._json[jsonkey]['id']
#               print('######################  ', i,' Original Tweet number; ',tweet._json[jsonkey]['id'])
               j+=1
            
            elif (jsonkey=='query_search'):
               tweetvalue.append(str(querysearch))
               
            elif (type(tweet._json[jsonkey])==dict):
#                   print(z,"  ",jsonkey,' = ',type(tweet._json[jsonkey]))
               tweetvalue.append(str(tweet._json[jsonkey]))
               z+=1
            else:
               tweetvalue.append(tweet._json[jsonkey])
               z+=1
        except:
#            print('Value not found ',jsonkey )
            tweetvalue.append('NULL')
           
        
#        print(str(ColumnName))
#        print(SQLQUERY)
#        print(tweetvalue[9])
        
    try:
        c.execute(SQLQUERY,tweetvalue)
        conn.commit()
#        print('|||||||||||SUCCESSFULL ORIGINAL ',i )
        i+=1
    except:
#        print('-----------FAILURE Tweet number;',i)
#        print(conn.OperationalError)
        conn.rollback()
   
#    print('###################### Tweet number;',i)
        
    conn.close()    

    
def Test3():
    querysearch ='#Fillon'
    # iterate over 50 of tim oreilly's tweets  
    #    , until='2017-01-18'
    i=0
    for tweet in tweepy.Cursor(api.search,q='test',since='2017-02-03 10:01:25',until='2017-02-03 30:15:10').items():  
        print(tweet._json['created_at'],tweet._json['user']['screen_name']," : \n",tweet._json['text'])
        i+=1
    print(i)   
    
    
def Collectall(timedate,num):
   
    print("------------ HAMON ")
    Collect_tweet('Hamon',timedate,num)
    print("------------ FILLON ")
    Collect_tweet('Fillon',timedate,num)
    print("------------ TRUMP ")
    Collect_tweet('Trump',timedate,num)
    print("------------ LEPEN")
    Collect_tweet('Marine Lepen',timedate,num)
    print("------------ MACRON ")
    Collect_tweet('Macron',timedate,num)
    print("------------ LEPEN 2 ")
    Collect_tweet('lepen',timedate,num)
    
def TweetWeekMine():
    
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-02-  21")
#    Collectall("2017-02-21",1000)
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-02-  22")
#    Collectall("2017-02-22",1000)
#    print("2017-02-23")
#    Collectall("2017-02-23",1000)
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-02-  24")
#    Collectall("2017-02-24",1000)
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-02-  25")
#    Collectall("2017-02-25",1000)
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  04")
#    Collectall("2017-03-04",1000)   
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  08")
#    Collectall("2017-03-08",1000)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  09")
    Collectall("2017-03-09",1000)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  10")
    Collectall("2017-03-10",1000)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  11")
    Collectall("2017-03-11",1000)
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  07")
    Collectall("2017-03-07",1000)
    Get_original_tweet(100,'RealDonaldTrump')
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  27")
#    Collectall("2017-02-27",1000)
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA   2017-03-  28")
#    Collectall("2017-02-28",1000)
   