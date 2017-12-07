from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import simplejson as json
#from pymongo import MongoClient

#auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")

# Construct the API instance
#api = tweepy.API(auth)

consumer_key= 'GdjPzCdcuRrUM62XMPLSRtv0x'
consumer_secret = '1qCg8rf2fXj7ZU8PYN78PihjGwGdV7kuwBebBjztqE8jodhC5l'

access_token = '931093265067266048-SR8syXRf2QajzJvRkf7SMR7kyrqCR3O'
access_token_secret = '	hoD5QNanDFh7YEa4BT0bCvjfxJ4Vh0NuxBxv87187ujVm'


#Anne's tip
class StdOutListener(StreamListener):
    def on_data(self, data):

        with open('Tweets1.1.csv', 'a') as outfile:
            json.dump(data, outfile)
        return True

    def on_error(self,status):
        print ('An error has occured: ' + str(status))


##Tutorial 2 outline
    
#class StdOutListener(StreamListener):
#    def on_data(self, data):
#        #print(data)
#        json_load = json.loads(data)
#        #print(json_load)
#        myFile = open('Tweets1.2.csv', 'a')

#        try:
#            texts = json_load['Sinterklaas']
            #texts=json_load['user']['location']
            #texts=json_load['user']['profile_image_url']
            #texts = json_load['user']['description']
            #texts = json_load['place']['bounding_box']['coordinates']
#           coded = texts.encode('utf-8')
            
#            s = str(coded)
            #print(s[2:-1])
            #myFile.write(s[2:-1])
#            myFile.write(s)
#            myFile.write('\n')  # adds a line between tweets
#        except:
#            pass
#        myFile.close()
#        return True

#    def on_error(self,status):
#        print ('An error has occured: ' + str(status))

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, StdOutListener())
    stream.filter(locations=[52.428316, 4.738178, 52.304989, 5.012917])
