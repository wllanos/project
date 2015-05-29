
 # -*- coding:utf-8 -*-  
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

ckey = '8a2Pq2KTPJJVzjGeaNjoV7cYg'
csecret = 'k2PHUZDX4mB7EzmknW3mX7EIzvX1vrJmw2AJlj6v83xFqh6KfJ'
atoken = '80905400-31gxOVa9X0ztmbXd32azC2Nk0C8aD00xi94JhCClf'
asecret = '3BdjiTBFBbhdrNxFeQcYpzCYsDxxSh28keukvyvTqJcGv'

class listener(StreamListener):

	def on_data(self, data):
		try:
			
			decoded = json.loads(data)
		        
        	#print decoded['user']['screen_name']    
            #source = decoded['source'].encode('ascii', 'ignore'))
    		#print decoded
			#tweet = data.split(',"text":"')[1].split('","source')[0].encode('ascii', 'ignore')
			tweetText = decoded['text'].encode('utf-8', 'ignore')
			tweetId = str(decoded['id'])
			tweetInReplyStatusId = str(decoded['in_reply_to_status_id'])
			tweetFavoriteCount = str(decoded['favorite_count'])
			tweetRetweeted = str(decoded['retweeted'])
			tweetCoordinates = str(decoded['coordinates'])
			tweetTimestamp_ms = str(decoded['timestamp_ms'])

			tweetGeo = str(decoded['geo'])
			tweetLang = str(decoded['lang'])
			tweetDate = str(decoded['created_at'])

			tweetUserScreen_name = decoded['user']['screen_name'].encode('utf-8', 'ignore')
			tweetUserProfile_image_url_https = str(decoded['user']['profile_image_url_https'])
			tweetUserFollowers_count = str(decoded['user']['followers_count'])
			tweetUserListed_count = str(decoded['user']['listed_count'])
			tweetUserFollowing_count = str(decoded['user']['friends_count'])
			tweetUserLocation = str(decoded['user']['location'])
			tweetUserGeo_enabled = str(decoded['user']['geo_enabled']).encode('utf-8', 'ignore')
			tweetUserName = decoded['user']['name'].encode('utf-8', 'ignore')
			tweetUserLang = str(decoded['user']['lang'])
			tweetUserUrl = str(decoded['user']['url'])
			tweetUserCreated_at = str(decoded['user']['created_at'])
			tweetUserTime_zone = str(decoded['user']['time_zone'])
			tweetUserIs_translator = str(decoded['user']['is_translator'])

			print tweetText
			print tweetId
			print tweetInReplyStatusId
			print tweetFavoriteCount
			print tweetRetweeted
			print tweetCoordinates
			print tweetTimestamp_ms
			print tweetGeo
			print tweetLang
			print tweetDate
			print tweetUserScreen_name
			print tweetUserProfile_image_url_https
			print tweetUserFollowers_count
			print tweetUserListed_count
			print tweetUserFollowing_count
			print tweetUserLocation
			print tweetUserGeo_enabled
			print tweetUserName
			print tweetUserLang
			print tweetUserUrl
			print tweetUserCreated_at
			print tweetUserTime_zone
			print tweetUserIs_translator
			print '\n'
			print '###############'						
			
			saveThis = str(time.time()) + '::' + tweetText  + '::' + tweetId + '::' + tweetInReplyStatusId  + '::' + tweetFavoriteCount  + '::' + tweetRetweeted  + '::' + tweetCoordinates  + '::' + tweetTimestamp_ms  + '::' + tweetGeo  + '::' + tweetLang  + '::' + tweetDate  + '::' + tweetUserScreen_name  + '::' + tweetUserProfile_image_url_https  + '::' + tweetUserFollowers_count  + '::' + tweetUserListed_count  + '::' + tweetUserFollowing_count  + '::' + tweetUserLocation  + '::' + tweetUserGeo_enabled  + '::' + tweetUserName  + '::' + tweetUserLang  + '::' + tweetUserUrl  + '::' + tweetUserCreated_at  + '::' + tweetUserTime_zone  + '::' + tweetUserIs_translator  
			saveFile = open('TwitterMentions.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)

	def on_error(self, status):
		print status



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)


twitterStream = Stream(auth,listener())
#twitterStream.filter(track=["@el_BID",'el bid','bid','Banco Interamericano de Desarrollo','Banco Mundial','@BancoMundial','BancoMundial','el Banco Mundial','CAF','@AgendaCAF','AgendaCAF','banco de desarrollo de América Latina','CAF-Banco de Desarrollo de América Latina'])
twitterStream.filter(track=["@el_BID",'el bid','Banco Interamericano de Desarrollo','Banco Mundial','@BancoMundial','BancoMundial','el Banco Mundial','@AgendaCAF','AgendaCAF','banco de desarrollo de América Latina','CAF-Banco de Desarrollo de América Latina'])
