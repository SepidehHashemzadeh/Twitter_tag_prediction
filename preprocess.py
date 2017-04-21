import preprocess_part2
import json
import time
import matplotlib.pyplot as plt
import numpy as np

hours_data=[] * 24
def extract_needed_info_plot(tweet):
    hour  = time.gmtime(tweet['send time'])[3]

def extract_needed_info(tweet):
    #follow_cnt = tweet['tweet']['user']['followers_count']
    #tweet['tweet']['retweet_count']

    time = tweet['firstpost_date']
    follow_cnt = tweet['author']['followers']
    retweet_cnt = tweet['metrics']['citations']['total']
    ]

    return {'time' : time, 'folower_count':follow_cnt, 'retweet_count':retweet_cnt
        , 'favorite_cnt':favorite_cnt, 'influence_level': influence_level, 'ranking_score':ranking_score}

# for all data in a file, creates a new file containing the required dictionary
def create_new_file(data, name):
    res = []
    for d in data:
        new_dict = extract_needed_info(d)
        res.append(new_dict)
    #f=open (name +'_newData.txt','w')
    #json.dumps(res,f)
    with open ( name +"_newData.txt","w") as outputfile:
        json.dump(res,outputfile,indent=4)



#given new file name returns averages.
def create_features(file_name):
    with open(file_name) as input_file:
        tweets = json.load(input_file)
    retweets_num = 0
    time_min = 1458169115
    time_max = 0
    followers_cnt = 0
    tweet_num = len(tweets)
    for t in tweets:
        retweets_num = retweets_num + t['retweet_count']
        if t['time'] < time_min:
            time_min = t['time']
        if t['time'] >= time_max:
            time_max = t['time']
        followers_cnt = followers_cnt + t['folower_count']
    avg_retweets = retweets_num / tweet_num
    avg_followers_cnt = followers_cnt / tweet_num
    avg_tweet_hour = (tweet_num/(time.gmtime(time_max)[3] - time.gmtime(time_min)[3]))

    return avg_retweets,avg_followers_cnt,avg_tweet_hour

def plot():
    allinfo=[]
    sumH=[]
    count=[]
    aveT=[]
    for i in xrange(24):
        sumH.append(0)
        count.append(0)
        aveT.append(0)
    allinfo=preprocess_part2.create_matrix('/Users/sepidehhashemzadeh/Desktop/final/#superbowl_newData.txt')

    #allinfo=preprocess_part2new.create_matrix('/Users/sepidehhashemzadeh/Desktop/project4/#superbowl_newData.txt')
    for i in range(len(allinfo)):
        sumH[allinfo[i][3]] = allinfo[i][4] +  sumH[allinfo[i][3]]
        count[allinfo[i][3]] = 1 + count[allinfo[i][3]]

    print(sumH)
    print(count)
    for k in xrange(24):
        aveT[k]=sumH[k]/count[k]

    print(aveT)
    bins = np.arange(0, 24, 1)
    #plt.hist(sumH, bins, color='blue')

    pos = np.arange(len(aveT))
    width = 1.0
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(bins)

    plt.bar(pos, aveT, width, color='r')
    # fig, ax = plt.subplots()
    # rects1 = ax.bar([1,2], [x,y],width=0.1,  color='r')
    # plt.show()
    # plt.hist(y,x)
    # plt.title("Number of Tweets")
    # plt.xlabel("Value")
    # plt.ylabel("Time")
    plt.show()

if __name__ == "__main__":
    print("hello")
    #files_name = ['#gohawks','#gopatriots', '#nfl', '#patriots', '#sb49', '#superbowl']
    files_name = ['#gohawks']

    tweets = []
    for fn in files_name:
        with open('/Users/sepidehhashemzadeh/Desktop/project4/tweets_'+fn +'.txt') as f:
            for line in f:
                tweets.append(json.loads(line))
                create_new_file(tweets,fn)
        # [avg_retweets,avg_followers_cnt,avg_tweet_hour]=create_features('/Users/sepidehhashemzadeh/Desktop/project4/'+fn+'_newData.txt')
        # print("avg_retweets"+fn,avg_retweets,"\n")
        # print("avg_followers_cnt"+fn,avg_followers_cnt,"\n")
        # print("avg_tweet_hour"+fn,avg_tweet_hour,"\n" ,"\n")
            #data.append(json.loads(line))
            #tweets=json.dumps(data[0], indent=4)
    plot()