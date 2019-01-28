import pandas as pd
from nltk.corpus import stopwords
import re
stop_words = set(stopwords.words('english')) 
pd.options.mode.chained_assignment = None

def pp(tweet):
    tweet = re.sub(r'(@\S+)|(http\S+)|[^a-zA-Z]',' ',tweet) #removal of @username,http link, apostrophe, hashtag, digits
    #return tweet
    #print(tweet)
    tweet = tweet.split()
    #print(tweet)
    clean_tweet = []
    for i in tweet:
        if i not in stop_words:
            clean_tweet.append(i)
    #print(clean_tweet)
    clean_tweet = ' '.join(clean_tweet)
    return clean_tweet
    
    
    
#pp("tweet as param")
'''
ds = pd.read_csv('dataset.csv')
tweets = ds.content
for i in range(len(tweets)):
    tweets[i] = pp(tweets[i])
'''
