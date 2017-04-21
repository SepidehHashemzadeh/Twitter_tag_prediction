import json
import time

print("hello")
#files_name = ['#gohawks','#gopatriots', '#nfl', '#patriots', '#sb49', 'superbowl']
files_name = ['#gohawks']
tweet = []
res = []
a=[]
#a=""
    #for fn in files_name:

with open('/Users/sepidehhashemzadeh/Desktop/project4/tweets_'+ '#gohawks'+'.txt') as f:
    for line in f:
        a.append(json.loads(line))
    tweets=json.dumps(a[2], indent=4)
    print(tweets)
#f.write(a)
#with open('/Users/sepidehhashemzadeh/Desktop/project4/newData') as input_file:
   # tweets = json.load(input_file)
#retweets_num = 0
#time_min = 1458169115
#time_max = 0
#followers_cnt = 0
#tweet_num = len(tweets)
#for t in tweets:
    #retweets_num = retweets_num + t['retweet_count']
    #if t['time'] < time_min:
        #time_min = t['time']
    #if t['time'] >= time_max:
        #time_max = t['time']
    #followers_cnt = followers_cnt + t['folower_count']
#avg_retweets = retweets_num / tweet_num
#avg_followers_cnt = followers_cnt / tweet_num
#avg_tweet_hour = (tweet_num/(time.gmtime(time_max)[3] - time.gmtime(time_min)[3]))
#print(avg_retweets,avg_followers_cnt,avg_tweet_hour)
#outputfile.write(line+'\n')

