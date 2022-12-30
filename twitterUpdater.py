from youtubesearchpython import *
import random
import tweepy
import schedule
import time
import os
import re
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

# Replace these with your own Twitter API credentials
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Authenticate with the Twitter API using your API credentials
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set the time when the tweet should be sent
tweet_time = datetime(year=2022, month=12, day=28, hour=10, minute=28, second=0)

tweeted_new_vids = [] 

def check_for_new_vid():
    print('checking')
    channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
    id=channelsSearch.result()['result'][0]["id"] 
    playlist = Playlist(playlist_from_channel_id(id))
    pl=playlist.info["info"]["link"]
    videos=Playlist.getVideos(pl)
    vid_link = videos["videos"][0]["link"]
    skinny_link = vid_link.split('&list')[0]
    vid_title = videos["videos"][0]["accessibility"]["title"]
    skinny_title = vid_title.split(' by Sanjin Dedic ')[0]
    result=re.search("\d+ hours",vid_title)
    github_link = 'https://github.com/Sanjin84/socialAPI/blob/main/twitterUpdater.py'
    if result != None:
        if int(result.group().split(" ")[0])<24 and skinny_link not in tweeted_new_vids:
            tweeted_new_vids.append(skinny_link)
            status = '''Sanjin's bot here, with exciting news, seconds ago my master got up off his and made a video (see below)
check out how I do these notifications GitHub link:{}
{}
            '''.format(github_link,skinny_link)
            print(status, len(status))
            #api.update_status(status)
    else:
        print('no new vid yet')

def friday_tweet():
    global tweet_time
    channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
    id=channelsSearch.result()['result'][0]["id"]
    playlist = Playlist(playlist_from_channel_id(id))
    pl=playlist.info["info"]["link"]
    videos=Playlist.getVideos(pl)
    ch=random.randint(0,9)
    vid_link = videos["videos"][ch]["link"]
    skinny_link = vid_link.split('&list')[0]
    github_link = 'https://github.com/Sanjin84/socialAPI/blob/main/twitterUpdater.py'
    my_tweet = '''Sanjin's Bot here wishing you a happy Friday morning with a recent video from my master's channel: {}
Help me get better, take a look at my code and suggest improvements:{}
'''.format(skinny_link,github_link)
    print(my_tweet,len(my_tweet))

        # Check the current time
    current_time = datetime.now()
    print(current_time)
    # If the current time is equal to the tweet time, send the tweet
    if current_time > tweet_time and vid_link not in tweeted_new_vids:
        #api.update_status("Hello World My Bot is Alive!")
        print(my_tweet)
        # Set the tweet time to the next day at 8AM
        tweet_time = tweet_time + timedelta(days=7)
    else:
        print("Not time to tweet yet")
    # Sleep for 1 minute before checking the time again
    

schedule.every(1).seconds.do(friday_tweet)
schedule.every(1).seconds.do(check_for_new_vid)

while 1:
    schedule.run_pending()
    time.sleep(1)
