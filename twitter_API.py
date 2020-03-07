import twitter_handling as tw
import image_processing as imagp
import ImageToVideo as ITV
import threading
import time
import queue


def twitter_video(twitter_id):
    twitter = tw.twitter_feed_catching("keys")
    username = twitter_id
    profile_url = twitter.get_user_pic(username)
    tweets = twitter.get_users_tweets(username)
    imagp.create_images(username, profile_url, tweets)
    ITV.imgToVideo(username)




# if __name__ == '__main__':
  

#   twitter_id = input("Twitter ID: ")

#   t1 = threading.Thread(name="twitter_video", target=twitter_video, args=(twitter_id, 2))
#   t1.start()  
#   time.sleep(.1)  
 

