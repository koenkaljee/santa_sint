from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# consumer key, consumer secret, access token, access secret.
ckey = "izDaFJ0t9U2wHetZ1xr48WCgX"
csecret = "WfNC3AYqV6IDj57QGkqJclJ6SXBdQ8DyAFu6r50nydSw0pYDIf"
atoken = "795582525582221313-mECTEWQpMNrHD6eJcTUpwVpK8wMFGPa"
asecret = "qVpwSGCFgABcElgcuhlpxvXtrf69p77GneIjc2QClemJB"


class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print
        status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["sinterklaas"])