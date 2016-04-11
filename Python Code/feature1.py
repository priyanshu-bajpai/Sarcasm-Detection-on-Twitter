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

def getSentiStrength(w,sentidict):
	if w in sentidict:
		return sentidict[w]
	else:
		for key,value in sentidict.iteritems():
			if key.startswith(w):
				return value
		#print w
		return 0 
		
def getBigrams(tokens):
	bigrams=[]
	c=0
	while c<=len(tokens)-2:
		bigrams.append(tokens[c]+tokens[c+1])
		c=c+1
	return bigrams
def getTrigrams(tokens):
	trigrams=[]
	c=0
	while c<len(tokens)-2:
		trigrams.append(tokens[c]+tokens[c+1]+tokens[c+2])
		c=c+1
	return trigrams
def getAffect(w,affectdict):
	if w in affectdict:
		return affectdict[w]
	else:
		for key,value in affectdict.iteritems():
			if key.startswith(w):
				return value
		#print w
		return 4.5
def contrastingFeatures(words,affectdict,sentidict,bidict,tridict):
	affectscores=[]
	sentiscores=[]
	for w in words:
		affectscores.append(getAffect(w,affectdict))
		sentiscores.append(getSentiStrength(w,sentidict))
	bigrams = getBigrams(words)
	trigrams=getTrigrams(words)
	poscount=0
	possum=0
	negcount=0
	negsum=0
	for bi in bigrams:
		if bi in bidict:
			if bidict[bi]>0:
				possum+= bidict[bi]
				poscount = poscount+1
			else:
				negsum+=bidict[bi]
				negcount+=1
	for tri in trigrams:
		if tri in tridict:
			if tridict[tri]>0:
				possum+= tridict[tri]
				poscount = poscount+1
			else:
				negsum+=tridict[tri]
				negcount+=1
	

	return [(max(affectscores) - min(affectscores)), (max(sentiscores)-min(sentiscores)),poscount,possum, negcount,negsum]
