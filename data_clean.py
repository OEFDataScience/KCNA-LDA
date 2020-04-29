# -*- coding: utf-8 -*-
"""
Initial Data Cleaning Script

Created on Wed Apr 29 10:47:33 2020

@author: Claytonious
"""
#modules
import pandas as pd
from langdetect import detect
from langdetect import detect_langs
import re

###################################################################
#This script sets up the text data for analysis:
#1. Gets rid of observations that are missing text data
#2. Uses a trained language classifier to determine story language
#3. Drop non-en stories for now
#4. Do basic pre-processing of text getting rid of non-alphabet symbols
###################################################################
#import data and munge df

stories = pd.read_csv('dprk_text.csv', encoding = 'utf-8')
#some missing row data, so drop rows that are missing text
stories = stories.dropna()
#reset index
stories = stories.reset_index().copy()
#create new date object
stories['Date2'] = stories['Date']
stories['Date2'] = pd.to_datetime(stories['Date2'],
       format = '%m/%d/%Y')
stories['Date2'] = pd.to_datetime(stories['Date2']).dt.to_period('M')

#classify story language
stories['lang'] = ''
for i in range(0, (len(stories['Text'])-1)):
    print("Classifying document " + str(i))
    stories['lang'][i] = detect(stories['Text'][i])
    print("Finished document " + str(i))
#subset out non-en stories
#langs represented: en, es, fr, de, tl, id, ''
eng_filter = stories['lang']=='en'
df = stories[eng_filter]


#basic clean of text data
df['text_processed1'] = df['Text'].map(lambda x:
    re.sub(r'.*-- ', '', str(x)))
df['text_processed2'] = df['text_processed1'].map(lambda x:
    re.sub('[,\.!?]', '', str(x)))
df['text_processed2'] = df['text_processed2'].map(lambda x:
    x.lower())

    #quick check
df['text_processed2'].head()    


#SAVE FOR ANALYSIS
df.to_pickle("dprk_cleaned.pkl")
df.to_csv("dprk_cleaned.csv")