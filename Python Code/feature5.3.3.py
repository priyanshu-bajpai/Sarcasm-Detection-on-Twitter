import pandas
import pylab
import re
from pandas import *
from pylab import *
from datetime import datetime
from dateutil import relativedelta



#used to check if the tweet to be tested contains the swear words
def swearWord(tweet):
    feature3=False
    Swearwords =["shit","fuck","damn","bitch","crap","piss","dick","darn","cock","pussy","asshole","fag","bastard","slut","douche","bloody","cunt","bugger","bollocks","arsehole"]
    for item in Swearwords:
        if item in tweet:
            feature3=True
    return feature3


def TimeDifference(curTweet, prevTweet):
    date_1 = prevTweet
    date_2 = curTweet
    #This will find the difference between the two dates
    difference = relativedelta.relativedelta(date_2, date_1)
    details = []
    #details.append(difference.years)
    #details.append(difference.months)
    details.append(difference.days)
    details.append(difference.hours)
    details.append(difference.minutes)
    details.append(difference.seconds)
    #print "Difference is %s year, %s months, %s days, %s hours, %s minutes %s seconds" %(difference.years, difference.months, difference.days, difference.hours, difference.minutes,difference.seconds)

    #return a list containing details [years,months,days, hours, min, sec]
    return details


# Aims at deriving the probability distribution of tweeting pattern of the user, and other two features
def frustration(tweets,TestTweet):
    features = []
    '''feature1 : input for this feature would be last 2 months tweets with timestamps'''
    totalCount = len(tweets)

    times = tweets['time']
    intervals = {}
    for t in times:
        hr = t.hour#[11:13]
        if hr not in intervals:
            intervals[hr] = 0
        intervals[hr]+=1

    # print intervals
    # for k in sorted(intervals.keys()):
    #     print "%s:00-%s:00  %s" % (k,int(k)+1,intervals[k])

    testInterval = TestTweet.time.iloc[0].hour
    features.append(double(intervals[testInterval])/double(totalCount))

    '''feature2 : Input for this feature would be current tweet timestamp and previous tweet timesatmp'''
    details = TimeDifference(TestTweet.iloc[0].time, tweets.iloc[0].time)
    for values in details:
        features.append(values)

    '''Feature 3 checks if the tweet contain a swearword: boolean'''
    features.append(swearWord(TestTweet['tweet']))
    return features


# Tweet at the top that data[0] is considered as the tweet for testing
if __name__ == '__main__':
    tweets = read_csv('user821.csv')   # creating a dataframe from a csv file
    data1 = tweets.ix[0:,['time','tweet']]
    #remove retweets from the dateset
    data2 = data1[~data1['tweet'].str.contains('RT @')]
    data2.time = to_datetime(data2.time)
    tweets = data2[1:]
    TestTweet = data2.ix[0:1,['time','tweet']]

    features = frustration(tweets,TestTweet)
    print features
