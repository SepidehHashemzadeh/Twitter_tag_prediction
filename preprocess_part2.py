__author__ = 'ana'
import time
import json

def extract_needed_info(tweet):
    time = tweet['firstpost_date']
    follow_cnt = tweet['tweet']['user']['followers_count']
    retweet_cnt = tweet['tweet']['retweet_count']
    return {'time' : time, 'folower_count':follow_cnt, 'retweet_count':retweet_cnt}

def get_req_info(dict):
    tot_retweet_cnt = 0
    tot_follower_num = 0
    max_follower = 0
    for tweet in dict:
        tot_retweet_cnt = tot_retweet_cnt + tweet['retweet_count']
        tot_follower_num  = tot_follower_num  + tweet['folower_count']
        max_follower = max(tweet['folower_count'], max_follower)
    return [tot_retweet_cnt, tot_follower_num, max_follower]


def create_matrix(path):
    with open(path,'r') as file:
        data = json.load(file)
    years = {}
    for tweet in data:
        xx = time.gmtime(tweet['time'])
        hour  = xx[3]
        day = xx[7]
        year = xx[0]

        #if year not exist create
        if str(year) not in years.keys():
            years[str(year)] = {}
        year = years[str(year)]

        if str(day) not in year.keys(): #each year dictionary has some days as keys
            year[str(day)] = [[] for i in range(24)]
        hours = year[str(day)]


        hours[hour].append(tweet.copy())
        ###################


    #create matrix
    #retweet_cnt, follower_cnt, max_follower, hour , tweet_cnt
    features = []
    #predictant = []
    for year in years.items():
        for day in year[1].items():
            for ind, hour_info in enumerate (day[1]): # each day has exactly 24 hour_info(list)
                if len(hour_info )== 0:
                    continue
                res = []
                res.extend(get_req_info(hour_info))
                res.append(ind)
                res.append(len(hour_info))
                features.append(res)
                try:
                    #predictant.append(features[-1])
                    features[-1].append(features[-2][4])
                except:
                    print("excepted making label for first sample")
    print(features)

    return (features)
