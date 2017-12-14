import psycopg2
import csv
import json




#################### EDIT THESE PARAMETERS AS YOU WISH #########################
conn_string = "host='localhost' dbname='test_db' user='postgres' password='pwd'"
table = "tweets"
data_location = 'tweetids.csv'      # path to which to save the CSV file with all the tweet IDs
json_data_location = 'tweets_metadata.json'     # path from which to read the JSON file with the tweets if the tweets were stored in a JSON file
################################################################################



# read from JSON file
with open("tweets.json", encoding='utf8', mode='r') as tweets_json:
     json_load = json.load(tweets_json)
     tweets = list(json_load)
     tweetids = []
     for tweet in tweets:
         tweetids.append(tweet['id'])

     csv_writer = csv.writer(open(data_location, 'w'))
     for tweetid in tweetids:
         csv_writer.writerow([tweetid])


# read from database
# try:
#    conn = psycopg2.connect(conn_string)
 #   conn.autocommit = True
  #  cur = conn.cursor()
#
 #   cur.execute("select tweetid from " + table)
  #  rows = cur.fetchall()
   # print("Number of results: ", cur.rowcount)
    
    #csv_writer = csv.writer(open(data_location, 'w'))
#    for row in rows:
 #       csv_writer.writerow(row)
#
 #   cur.close()
#except (Exception, psycopg2.DatabaseError) as error:
#    print(error)
#finally:
#    if conn is not None:
#        conn.close()