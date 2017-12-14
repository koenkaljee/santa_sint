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
conn_string = "host='localhost' dbname='koenkaljee' user='koenkaljee' password='pwd' port='5433'"
data_location = 'tweetids.csv'
tweets_table = "koenkaljee"
users_table = "koenkaljee"
################################################################################

    cur.execute("SELECT * FROM test;")
    cur.fetchone()
    (1, 100, "abc'def")