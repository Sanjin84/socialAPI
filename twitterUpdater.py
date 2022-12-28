from youtubesearchpython import *
import random
import tweepy
import schedule
import time
import os
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
tweet_time = datetime(year=2022, month=12, day=28, hour=9, minute=55, second=0)

def check_for_new_vid():
    channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
    id=channelsSearch.result()['result'][0]["id"] 
    playlist = Playlist(playlist_from_channel_id(id))
    pl=playlist.info["info"]["link"]
    videos=Playlist.getVideos(pl)
    vid_link = videos["videos"][0]["link"]
    skinny_link = vid_link.split('&list')[0]
    vid_title = videos["videos"][0]["accessibility"]["title"]
    result=re.search("\d+ hours",vid_title)
    github_link = ''
    if int(result.group().split(" ")[0])<24:
        status = '''Sanjin's bot here, with exciting news, seconds ago my master got up off his lazy butt and auploaded a video titled: {}
        check out how I do these notifications GitHub link:{}
        video: {}
        '''.format(vid_title,github_link,vid_link)
        print(status)
        #api.update_status(status)

def friday_tweet():
    global tweet_time
    channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
    id=channelsSearch.result()['result'][0]["id"]

    playlist = Playlist(playlist_from_channel_id(id))
    pl=playlist.info["info"]["link"]
    videos=Playlist.getVideos(pl)
    ch=random.randint(0,9)
    vid_link = videos["videos"][ch]["link"]
    github_link = 'https://github.com/Sanjin84/pylinux/blob/main/logic_bombs/auto_tweet.py'
    my_tweet = ''' Sanjin's Bot here wishing you a happy Friday morning with a recent video from my master's channel: {}

    Help me grow and improve, take a look at my code and suggest improvements:{}
    '''.format(vid_link,github_link)

        # Check the current time
    current_time = datetime.now()
    print(current_time)
    # If the current time is equal to the tweet time, send the tweet
    if current_time > tweet_time:
        #api.update_status("Hello World My Bot is Alive!")
        print(my_tweet)
        # Set the tweet time to the next day at 8AM
        tweet_time = tweet_time + timedelta(minutes=3)
    else:
        print("Not time to tweet yet")
    # Sleep for 1 minute before checking the time again
    

schedule.every(1).minutes.do(tweet_things)
schedule.every(1).minutes.do(check_for_new_vid)

while 1:
    schedule.run_pending()
    time.sleep(1)
