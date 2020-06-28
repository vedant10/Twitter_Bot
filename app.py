import tweepy
import time

auth = tweepy.OAuthHandler('Add your API Key','Add your secret API key')

auth.set_access_token('Add your access token','Add your access secret token')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

'''print(user.screen_name)

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)'''

search = 'Technology'
noTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(noTweets):
    try:
        print('Tweet Retweeted')
        '''tweet.favorite()'''
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break




