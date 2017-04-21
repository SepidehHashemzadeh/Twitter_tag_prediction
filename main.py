import preprocess.py
import json

def main():
    print("hello")
    files_name = ['#gohawks','#gopatriots', '#nfl', '#patriots', '#sb49', 'superbowl']

    tweet = []
    for fn in files_name:
        with open('/Users/sepidehhashemzadeh/Desktop/project4/tweets_'+files_name +'.txt') as f:
            for line in f:
                tweet=json.loads(line)
            #data.append(json.loads(line))
            #tweets=json.dumps(data[0], indent=4)
                preprocess.create_new_file(tweet, files_name)