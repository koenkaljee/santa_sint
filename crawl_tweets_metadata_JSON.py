# coding=utf-8
import collections
from datetime import datetime
import tweepy
import json
import psycopg2
import sys
import csv
from math import ceil

from tweepy import TweepError
from tweepy import RateLimitError




#################### EDIT THESE PARAMETERS AS YOU WISH #########################
conn_string = "host='localhost' dbname='test_db' user='postgres' password='pwd'"
data_location = 'tweetids.csv'
tweets_table = "tweets_metadata"
users_table = "users_metadata"
################################################################################



# EDIT THE STRINGS TO USE YOUR API KEYS OBTAINED FROM ('https://apps.twitter.com/')
CONSUMER_KEY = 'plXeUm1TA4Jf0ACL18YMQkqOz'
CONSUMER_SECRET =  'PkUos3Oaelap3UgEcRU0WnIyTqiNxRKdZLrvqhFtELEUWhUO1c'
ACCESS_TOKEN = '937671310901239809-7P8GkXaPdPki4rYhUdSchvk16J0GiVb'
ACCESS_TOKEN_SECRET =  'f7VaP3PgjoblEmRHZE0SNg1kMQktLK2GlWgjLJiLYjPws'

CONSUMER_KEY2 = 'dbuPBzcYttW0rRtoRfSeXUULT'
CONSUMER_SECRET2 = 'Llff8nyRgKSW2OR2XH7W8x5Rbt4ialRyV0as1mfAxJaa8WxTqD'
ACCESS_TOKEN2 = '937671310901239809-ZTaPi8FvhTLywgsjeCNJnJIAuhMJuEp'
ACCESS_TOKEN_SECRET2 = 'RDV4PWZZ377dzCoxi4hQ5evM0o7uPmnze4DfY1AvVmYzu'
################################################################################


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth2 = tweepy.OAuthHandler(CONSUMER_KEY2, CONSUMER_SECRET2)
auth2.set_access_token(ACCESS_TOKEN2, ACCESS_TOKEN_SECRET2)


apis = []
apis_len = 2

apis.append(tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True))
apis.append(tweepy.API(auth2, wait_on_rate_limit=True, wait_on_rate_limit_notify=True))



class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, collections.Iterable):
            return list(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
            return dict(obj)
        elif hasattr(obj, '__dict__'):
            return {member: getattr(obj, member)
                    for member in dir(obj)
                    if not member.startswith('_') and
                    not hasattr(getattr(obj, member), '__call__')}

        return json.JSONEncoder.default(self, obj)



tweetid = -1
tweet_created_at = None
text = None
in_reply_to_status_id = -1
in_reply_to_user_id = -1
in_reply_to_screen_name = None
is_quote_status = None
retweeted_status = None
retweet_count = -1
favorite_count = -1
lang = None
quoted_status_id = -1
quote_count = -1
reply_count = -1
source = None
possibly_sensitive = None

# the following attributes are the ones extracted from complex attributes
latitude = None
longitude = None
hashtags = None
urls = None
user_mentions = None
media = None
place = None
coordinates = None
entities = None
user = None
quoted_status = None

userid = -1
name = None
screen_name = None
location = None
description = None
verified = None
followers_count = -1
friends_count = -1
listed_count = -1
favorites_count = -1
statuses_count = -1
user_created_at = None
time_zone = None
geo_enabled = None
user_lang = None

utc_offset = -1
profile_image_url = None
url = None
protected = None





with open(data_location, encoding='utf8', mode='r') as tweetids_csv:
	reader = csv.reader(tweetids_csv)
	tweetids_list = list(reader)

tweetids = [int(tweetid[0]) for tweetid in tweetids_list]

iterations = ceil(len(tweetids) / 100)
json_string = []
c = 0
apikey_iter = 0
saved_i = 0



for i in range(c, iterations):
	try:
		# Get the metadata for 100 tweets at a time
		statuses = apis[apikey_iter].statuses_lookup(tweetids[saved_i:saved_i+100], include_entities=True)
		saved_i += 100			
		c += 1		
		print(str(c))
		
		if c % 300 == 0:
			apikey_iter = (apikey_iter + 1) % apis_len

		# To make it simple, the results could be stored in a JSON file instead of setting up a database. However, this solution is not advisable for
		# storing large amount of data.
		with open("tweets_metadata.json", "a") as output:
			json.dump(statuses, output, cls=JSONEncoder)

	except TweepError as e:
		print('Error string: ' + e.response.text)
		pass
	except RateLimitError:
		apikey_iter = (apikey_iter + 1) % apis_len
		pass