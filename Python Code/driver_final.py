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

from preproc import *
from feature1 import *
from feature3 import *
from feature4 import *
from feature5 import *

stopwords = set(stopwords.words('english'))
affectdict ={}
sentidict={}
bidict={}
tridict={}
 
#X = [[0,0] , [1,1] ]
#Y = [0,1]


def init_dicts():
	global affectdict
	global sentidict
	global bidict
	global tridict
	with open('affectscores.txt','r') as file1:
		for line in file1:
			temp = line.split()
			affectdict[temp[0]]=float(temp[1])
	with open('senti.txt','r') as file2:
		for line in file2:
			temp = line.split()
			sentidict[temp[0]]=float(temp[1])
#	with open('bigramscore.txt','r') as file2:
#			for line in file2:
#				temp = line.split()
#				bidict[temp[0]]=float(temp[1])
#	with open('trigramscore.txt','r') as file2:
#		for line in file2:
#			temp = line.split()
#			tridict[temp[0]]=float(temp[1])
	print 'initialised dictionaries!'


def getFeatureHelper(tweet ,past_data):
	features = []
	try:
		features.extend(contrastingFeatures(tweet,affectdict,sentidict,bidict,tridict))
	except:
		print "line 58"
	try:
		features.extend(affectSentiment(tweet,affectdict,sentidict))
	except:
		print "error in feature3"
	try:
		features.extend(familiarityLanguage(tweet,past_data))
	except:
		print "error in feature4"
	try:
		features.extend(structuralVariations(tweet,affectdict,sentidict))
	except:
		print "error in feature5"
	#features.extend(bigrmF(tweet))
	#features.extend(trigrmF(tweet))
	#add other functions
	print features
	return features
	#call the list of features
	# the list of feature will be written into a file directly 
	


def main():

	init_dicts()  #initialize the dictionaries 
	
	trainingFile = open("output.csv",'a')
	wr = csv.writer(trainingFile, quoting=csv.QUOTE_ALL)
	
	path_sarcastic = os.path.abspath(__file__ + "/../../") + "/sarcastic_with_past"
	fileListSarcastic = os.listdir(path_sarcastic)
	for i in fileListSarcastic:
		list_tweets = []
		features = []
		with open(path_sarcastic+'/'+i) as tweet_file:
			file_reader = csv.DictReader(tweet_file)
			for row in file_reader:
					try:
						words = preprocess(row['tweet'],stopwords)
						list_tweets.append(words)
					except:
						print "problem"
		words = list_tweets[0]
		past = list_tweets[1:]
		features = getFeatureHelper(words , past)
		features.append(1)
		wr.writerow(features) 
		
	
#	path_normal = os.path.abspath(__file__ + "/../../") + "/normal_with_past"
#	fileListNormal  = os.listdir(path_normal)
#	for i in fileListNormal:
#		list_tweets = []
#		features = []
#		with open(path_normal+'/'+i) as tweet_file:
#			file_reader = csv.DictReader(tweet_file)
#			for row in file_reader:
#					try:
#						words = preprocess(row['tweet'])
#						list_tweets.append(words)
#					except:
#						print "problem"
#		words = list_tweets[0]
#		past = list_tweets[1:]
#		features = getFeatureHelper(words , past)
#		features.append(0)
#		wr.writerow(features) 


if __name__=="__main__":
	main()
	# main function for the whole project 
	# command line argument format 
	# positivetweets negativetweets
