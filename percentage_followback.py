import tweepy
import time 
import math

def main(w_time=1, n=0, check=False):
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('', '')
    api = tweepy.API(auth)
    friends = []
    followers = []
    count = 0
    for status in tweepy.Cursor(api.followers).items():
        followers.append(status.id)
        count += 1
        if check == True:
            print(count)
        time.sleep(w_time)
    for status in tweepy.Cursor(api.friends).items():
        friends.append(status.id)
        count += 1
        if check == True:
            print(count)
        time.sleep(w_time)

    s = len(followers)
    num = 0
        
    for i in followers:
        for k in friends:
            if i == k:
                num += 1
            else:
                pass
                
    percentage = (num/s)*100
    percentage = math.floor(percentage * 10 ** n) / (10 ** n)
    return percentage
