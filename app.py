import tweepy
import time

auth = tweepy.OAuthHandler('0H1mGcGLyv9s7mf02hlZr9YE1','xLgEXp0aGaJu4oXe5HPjOMduAllxQkvbCqX15OQNfvUWvGyhSF')

auth.set_access_token('3317901392-61aGeChISizViSvxbPWmw8sGZWZ2KVEWNi3DUuD','xMQSALBSQrSSUuCWg6uIrkgMSrGJSdd6Ks3hgi2P4ONC6')

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




