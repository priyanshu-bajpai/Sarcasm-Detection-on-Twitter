import sys 
from string import ascii_lowercase 
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')
import string
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk import FreqDist
from sklearn import svm
import os
import csv


def delimitedtweet(file, delimiter='\n', bufsize=4096):
    buf = ''
    while True:
        newbuf = file.read(bufsize)
        if not newbuf:
            yield buf
            return
        buf += newbuf
        lines = buf.split(delimiter)
        for line in lines[:-1]:
            yield line
        buf = lines[-1]


def preprocess(tweet,stopwords):
    #print "ok"
    tweet = tweet.replace("#sarcasm","")
    tweet = tweet.replace("#sarcastic","")
    tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet)
    tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    table = string.maketrans("","")
    tweet=tweet.translate(table, "?/:^&*()!@$%:;',<.>-+*\{\}[]\"")
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    tokens = tweet.split()
    tokens = [ w for w in tokens if w not in stopwords]
    tokens = [item for item in tokens if item.isalpha()]
    tokens = [ stemmer.stem(w) for w in tokens ]
    return tokens
