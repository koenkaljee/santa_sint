import collections
import json
from datetime import datetime
import psycopg2
import logging
import sys

from query import query_tweets



# This string represents the parameters of the Postgres database in which to store the tweets. Any parameter (e.g. database name or password) 
# should be changed according to the employed database configuration
conn_string = "host='localhost' dbname='test_db' user='postgres' password='pwd'"



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



# Saving batches of tweets
def main():
    limit = 1000 # this parameter defines the number of tweets to retrieve before storing them
    pos = None
    iter = 1

    query = "zwartepiet near:\"Amsterdam, The Netherlands\" within:3mi since:2017-12-04 until:2017-12-06"  # Define here the any query to perform as a string

    while True:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
        print("Iteration number: " + str(iter))
        iter += 1        

        try:            
            tweets, pos = query_tweets(query, pos, limit) 

            # To make it simple, the results could be stored in a JSON file instead of setting up a database. However, this solution is not advisable for
            # storing large amount of data.
            with open("tweets.json", "w") as output:
                json.dump(tweets, output, cls=JSONEncoder)

            tweets_json = json.loads(JSONEncoder().encode(tweets))
        except KeyboardInterrupt:
            logging.info("Program interrupted by user. Quitting...")
        
    
        tweetid_str = "-1"
        tweet_created_at = "0000-00-00 00:00:00+00"
        text = ""
        in_reply_to_status_ids_str = -1
        in_reply_to_user_id = None
        in_reply_to_screen_name = None
        retweet_count_str = -1
        favorite_count_str = -1    
        lang = ""
        latitude = None
        longitude = None
        country_code = None
        city_name = None
        hashtags = None
        urls = None
        user_mentions = None
        replies_count_str = -1
        userid_str = -1
        screen_name = ""
        fullname = ""

main()