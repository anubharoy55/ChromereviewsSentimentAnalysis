# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:49:57 2022

@author: Anubha
"""

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import csv
lemmatizer = WordNetLemmatizer()

class ChromeReviewsSentimentAnalysisCopyy:
        
    def fileOperations(df1):
        
        def review_to_words( raw_review ):

            #. Remove non letters
            current=remove_emoji(raw_review)
            letters_only = re.sub("[^a-zA-Z]", " ", current)

            words = letters_only.lower().split()
            stops = set(stopwords.words("english"))
            stops.remove('no')
            stops.remove('not')

            meaningful_words = []
            for token in words:
                if token not in stops:
                    token= lemmatizer.lemmatize(token)
                    meaningful_words.append(token)
                        #print('\nNext Token : ',token)
            #print('In reviews to words')
            return " ".join(meaningful_words)
        
        def remove_emoji(string):
            emoji_pattern = re.compile("["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       u"\U00002500-\U00002BEF"  # chinese char
                                       u"\U00002702-\U000027B0"
                                       u"\U00002702-\U000027B0"
                                       u"\U000024C2-\U0001F251"
                                       u"\U0001f926-\U0001f937"
                                       u"\U00010000-\U0010ffff"
                                       u"\u2640-\u2642"
                                       u"\u2600-\u2B55"
                                       u"\u200d"
                                       u"\u23cf"
                                       u"\u23e9"
                                       u"\u231a"
                                       u"\ufe0f"  # dingbats
                                       u"\u3030"
                                       "]+", flags=re.UNICODE)
            #print('In emoji remover')
            return emoji_pattern.sub(r'', string)
        
        def analyzerFunc(df):
            sia = SentimentIntensityAnalyzer()
            with open('GoodReviewsBadRating.csv','w',encoding="utf-8") as f:
                writer=csv.writer(f)
                writer.writerow(df.columns)
                for i in range(0,df['Text'].size):
                    if (sia.polarity_scores(df['Cleaned Reviews'][i])['compound']>0.3 and sia.polarity_scores(df['Cleaned Reviews'][i])['neu']<0.3 and sia.polarity_scores(df['Cleaned Reviews'][i])['pos']>0.68 and df['Star'][i]==1):#in positiveWords and df['Star'][i]<2:
                        #print('\n',df.iloc[i],'\n')
                        writer.writerow(df.iloc[i])
                        #print(sia.polarity_scores(df['Cleaned Reviews'][i]))

            df.drop('Cleaned Reviews',axis=1,inplace=True)
            result=[]
            df2 = pd.read_csv("GoodReviewsBadRating.csv")
            #for i in range(0,df2['Text'].size):
                #result.append(df2.iloc[i])
            #print(output)
            #print('In analyzaer')
            df2.drop('Cleaned Reviews',axis=1,inplace=True)
            return df2

        df1 = pd.read_csv("chrome_reviews.csv")

        df=df1.dropna(subset=['Text'], inplace=False)
        df=df.reset_index()

    # Get the number of reviews based on the df cloumn size
        num_reviews = df['Text'].size

    # Initialise an empty list to hold the clean reviews
        cleaned_reviews = []

    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list
        for i in range(0, num_reviews):
        # call our function for each one, and add the result to the list of
        # clean reviews
        #print(df['Text'][i])
            cleaned_reviews.append(review_to_words(df['Text'][i]))

        df['Cleaned Reviews']=cleaned_reviews
        #print('In file operations')
        output=analyzerFunc(df)
        return output
                               #df2=pd.read_csv('GoodReviewsBadRating.csv')
        
import pickle
pickle_out = open("classifier.pkl", mode = "wb")
pickle.dump(ChromeReviewsSentimentAnalysisCopyy
, pickle_out)
pickle_out.close()
