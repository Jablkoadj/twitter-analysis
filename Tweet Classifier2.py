
# coding: utf-8

# In[224]:

import pandas as pd
from pandas import Series,DataFrame
import encodings
import numpy as np
import nltk
from collections import Counter
import pprint as pp
#from scipy.misc import imread
import re
import string
from nltk.corpus import stopwords
from nltk import ngrams
from nltk.collocations import *
import matplotlib.pyplot as plt
import matplotlib.image as image
#import random
import json
#from wordcloud import WordCloud
import ast
import sqlite3
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


TweetDb='Tweet2.db'

# In[2]:

#data read
#df=pd.read_csv('TweetDataFillon2017-02-02.csv',names=["Text", "Name", "Date"],encoding='utf-8')



# In[4]: LDA test

def LDA_Tweet(df,tweet_language,keyword):
    
    tokenizer = RegexpTokenizer(r'\w+')
    tweetlist=df['text'].values 
    # create English stop words list

    la_stop=  get_stop_words(tweet_language[:2])
    la_stop.append('rt')
    la_stop.append('brt')
    la_stop.append('»')
    la_stop.append('«')
    la_stop.append('les')
    la_stop.append('nai')
    la_stop.append('ai')
    la_stop.append('a')
    la_stop.append('donc')
    la_stop.append('quoi')
    la_stop.append('est')
    la_stop.append('cest')
    la_stop.append('c')
    la_stop.append('via')
    la_stop.append('francois')
    la_stop.append('cest')
    la_stop.append('ca')
    la_stop.append('comme')
    la_stop.append('si')
    la_stop.append(keyword)
    la_stop.append(keyword+' \'')
    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()
    texts = []
    
    print('# loop through document list')
    for i in tweetlist:
        
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)
    
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in la_stop]
        
        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        
        
        texts.append(stemmed_tokens)
    
    print('# turn our tokenized documents into a id <-> term dictionary')
    dictionary = corpora.Dictionary(texts)
        
    print('# convert tokenized documents into a document-term matrix')
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    print('# generate LDA model')
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20)
    
    return(ldamodel)

# In[5]: tokenize without stop words by word in lower case
def  Tokenize_tweet(df,tweet_language,keyword):
     
    tweetlist=df['text'].values    
    collect_hashtag=df['entities']    
    pattern_hashtag=[]
    
   
    for hashtag in collect_hashtag:
        hashtag=ast.literal_eval(hashtag)
        hashtag=str(hashtag['hashtags'])
        hashtag=hashtag.replace('[{', '{')
        hashtag=hashtag.replace('}]', '}')
        hashtag=ast.literal_eval(hashtag)
        hashtag=list(hashtag)
        for word in hashtag:
            try:
                word=dict(word)
#                print(word['text'])
                pattern_hashtag.append(word['text'])
            except:
                i=0
#                print('No hashtag FOUND')           
    
#        print('q')
    pattern_hashtag = list(set(pattern_hashtag))
#    pattern_hashtag.remove('')
        
#    except:
#        print('Hashtag not recognized')
        
#    print('HASHTAG LIST', pattern_hashtag)
    pd.value_counts(df['text'].values)
    word_list = [word.lower() for line in tweetlist for word in line.split()]        
    regex = re.compile('[%s]' % re.escape(string.punctuation))
     
    
    tokenized_reports = []
    cachedstopwords = stopwords.words(tweet_language)
    cachedstopwords.append('rt')
    cachedstopwords.append('brt')
    cachedstopwords.append('»')
    cachedstopwords.append('«')
    cachedstopwords.append('les')
    cachedstopwords.append('nai')
    cachedstopwords.append('ai')
    cachedstopwords.append('a')
    cachedstopwords.append('donc')
    cachedstopwords.append('quoi')
    cachedstopwords.append('est')
    cachedstopwords.append('cest')
    cachedstopwords.append('c')
    cachedstopwords.append('via')
    cachedstopwords.append('francois')
    cachedstopwords.append('cest')
    cachedstopwords.append('ca')
    cachedstopwords.append('comme')
    cachedstopwords.append('http')
    cachedstopwords.append('si')
    cachedstopwords.append('quand')
    cachedstopwords.append(keyword)
    cachedstopwords.append(keyword+'s')
    cachedstopwords.append(keyword+' \'')
    
    pattern_hashtag.append('https')
   
#    hash_list = list(hashtaglist for hashtaglist in patternhash )
#    #    type(hash_list)
#    for hashtag in hash_list:
#        print(tag for tag in list(hashtag))
       
    
    for review in word_list:
            new_review = regex.sub(u'', review)
            
            if not new_review == u'':
                if new_review not in cachedstopwords:
#                    print(set(re.match(tweet,new_review) for tweet in pattern_hashtag))
                    if len(set(re.match(tweet,new_review) for tweet in pattern_hashtag))<2:
                        tokenized_reports.append(new_review)
             
    return(tokenized_reports)

def  Tokenize_hashtag(df,tweet_language,keyword):
    
#    Tweetlist=pd.DataFrame(df.groupby('hashtag').size().rename('counts')).sort_values('counts', ascending=False)
    
    pattern_hashtag=[]
    collect_hashtag=list(df['entities'].values)
    for hashtag in collect_hashtag:
        hashtag=ast.literal_eval(hashtag)
        hashtag=str(hashtag['hashtags'])
        hashtag=hashtag.replace('[{', '{')
        hashtag=hashtag.replace('}]', '}')
        hashtag=ast.literal_eval(hashtag)
        hashtag=list(hashtag)
        for word in hashtag:
            try:
                word=dict(word)
#                print(word['text'])
                pattern_hashtag.append(word['text'])
            except:
                i=0
#                print('No hashtag FOUND')      
    
    
    
    pattern_hashtag = list(set(pattern_hashtag))
    
    word_list = [word.lower() for line in pattern_hashtag for word in line.split()]
    
      
    regex = re.compile('[%s]' % re.escape(string.punctuation))
        
    
    tokenized_reports = []
    cachedstopwords = stopwords.words(tweet_language)
    cachedstopwords.append('rt')
    cachedstopwords.append('brt')
    cachedstopwords.append('»')
    cachedstopwords.append('«')
    cachedstopwords.append('les')
    cachedstopwords.append('nai')
    cachedstopwords.append('ai')
    cachedstopwords.append('a')
    cachedstopwords.append('donc')
    cachedstopwords.append('quoi')
    cachedstopwords.append('est')
    cachedstopwords.append('cest')
    cachedstopwords.append('ca')
    cachedstopwords.append('comme')
    cachedstopwords.append('si')
    cachedstopwords.append('via')
    cachedstopwords.append('francois')
    cachedstopwords.append('quand')
    cachedstopwords.append('https')
    cachedstopwords.append('c')
    cachedstopwords.append('via')
    cachedstopwords.append('francois')
    cachedstopwords.append(keyword)
    cachedstopwords.append(keyword+'s')
   
    for review in word_list:
            new_review = regex.sub(u'', review)
            if not new_review == u'':
                if new_review not in cachedstopwords:
                    tokenized_reports.append(new_review)

    return(tokenized_reports)

# 

def SummaryTweetdb(tweetdate,Lang,keyword):
    
    print(('TWEET ANALYSIS for {0}  from {1}').format(keyword,tweetdate))
    SQLQUERY="SELECT  * from TweetCollector WHERE substr(created_at,5,6)='"+ tweetdate +"' AND substr(created_at,27,4)='2017' AND query_search='" + keyword+ "';"
    
    
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()
    df= pd.read_sql_query(SQLQUERY,conn)
    conn.close()
    
    tokenized_reports=Tokenize_tweet(df,Lang,keyword)
#    print(tokenized_reports) 
    counts3=Counter(ngrams(tokenized_reports, 3))
    pp.pprint(list(counts3)[:15])
    counts2=Counter(ngrams(tokenized_reports, 2))
    pp.pprint(list(counts2)[:15])
#    show_cloudmask(str(list(ngrams(tokenized_reports, 2))),'twitter_mask.png')
#    show_cloud(str(list(tokenized_reports)))
    Summaryhashtag(df,Lang,keyword)
    conn.close()

def SummaryTopicTweetdb(tweetdate,Lang,keyword):
    
    print(('TWEET ANALYSIS for {0}  from {1}').format(keyword,tweetdate))
    SQLQUERY="SELECT  * from TweetCollector WHERE substr(created_at,5,6)='"+ tweetdate +"' AND substr(created_at,27,4)='2017' AND query_search='" + keyword+ "';"
    
    
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()
    df= pd.read_sql_query(SQLQUERY,conn)
    conn.close()
    
    ldamodel=LDA_Tweet(df,Lang,keyword)
    print(ldamodel.print_topics(num_topics=2, num_words=20))
    print(ldamodel.print_topics(num_topics=3, num_words=20))
    print(ldamodel.print_topics(num_topics=4, num_words=20))
    print(ldamodel.print_topics(num_topics=6, num_words=20))
#    counts3=Counter(ngrams(tokenized_reports, 3))
#    pp.pprint(list(counts3)[:15])
#    counts2=Counter(ngrams(tokenized_reports, 2))
#    pp.pprint(list(counts2)[:15])
##    show_cloudmask(str(list(ngrams(tokenized_reports, 2))),'twitter_mask.png')
##    show_cloud(str(list(tokenized_reports)))
#    Summaryhashtag(df,Lang,keyword)
    return(ldamodel)   
   
def Summaryhashtag(df,Lang,keyword):
#    print(('HASHTAG ANALYSIS for {0}  ').format(keyword)
    
    tokenized_reports=Tokenize_hashtag(df,Lang,keyword)
    counts=Counter(tokenized_reports)
    pp.pprint(list(counts)[:15])
#    show_cloud(str(tokenized_reports))
#    show_cloud(counts)
#    show_cloudmask(str(tokenized_reports),'twitter_mask.png')
    return(tokenized_reports)
    
#def show_cloud(counts):
#    wordcloud = WordCloud(relative_scaling = 0.1).generate(counts)
#    # Open a plot of the generated image.
#    plt.imshow(wordcloud)
#    plt.axis("off")
#    plt.show()

#def show_cloudmask(counts,picturemask):
#    twitter_mask = image.imread('twitter_mask.png')
#    wordcloud = WordCloud(relative_scaling = 0.5,mask=twitter_mask).generate(counts)
#    # Open a plot of the generated image.
#    
#    plt.imshow(wordcloud)
#    plt.axis("off")
#    
#    plt.show()


    

def Summarizetrend(keyword,lang,tweetdate,numday):
#   

    print(('HASHTAG  ANALYSIS for {0} FROM {1} TILL {2} ').format(keyword,tweetdate, tweetdate[5:-2]+str(int(tweetdate[-2:])+numday)))
        
    conn = sqlite3.connect(TweetDb,timeout=5)
    c = conn.cursor()

    for i in range(numday):       
        
        SQLQUERY=\
            "SELECT  * from TweetCollector WHERE substr(created_at,5,6)='"\
            + tweetdate[5:] +"' AND substr(created_at,27,4)='"+tweetdate[:4] +\
            "' AND query_search='" + keyword+ "';"
        df= pd.read_sql_query(SQLQUERY,conn)
        print(SQLQUERY)
        print(('HASHTAG  ANALYSIS for {0} ON : {1} ').format(keyword,tweetdate))
        Summaryhashtag(df,lang,keyword)
        tweetdate=tweetdate[:-2]+str(int(tweetdate[-2:])+1)
        

    conn.close()
        
        
 
   
#def Summarizeall(timedate):
#   
#    SummaryTweet('TweetDataHamon'+timedate+'.csv','French','Hamon')
#    SummaryTweet('TweetDataMacron'+timedate+'.csv','French','Macron')
#    SummaryTweet('TweetDataFillon'+timedate+'.csv','French','Fillon')
#   
#    SummaryTweet('TweetDataTrump'+timedate+'.csv','English','Trump')
#    SummaryTweet('TweetDataMarine Lepen'+timedate+'.csv','French','Marine Lepen')
#    SummaryTweet('TweetDatalepen'+timedate+'.csv','French','lepen')    