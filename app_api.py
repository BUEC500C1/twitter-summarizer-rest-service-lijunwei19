from flask import Flask, send_from_directory
from flask_restful import Resource, Api
from twitter_API import twitter_video
import os
import time


app = Flask(__name__)
api = Api(app)

class tweets(Resource):
  def get(self, twitter_id):
      twitter_video(twitter_id)   
      path = os.path.join(app.root_path, 'video/')     
      file_path = f'{path}{twitter_id}better.mp4'   
      for _ in range(4):
        if os.path.exists(file_path):
          return 'file is ready, download from http://... /download/twitter_id'
        time.sleep(2)
      return 'response time out'


class download_video(Resource):
  def get(self, twitter_id):
      path = os.path.join(app.root_path, 'video') 
      filename = f'{twitter_id}better.mp4'   
      try :    
        return send_from_directory(directory= path, filename= filename, as_attachment= True)  
      except Exception as e:
        return str(e)


api.add_resource(tweets, '/search/<twitter_id>')
api.add_resource(download_video, '/download/<twitter_id>')

if __name__ == '__main__':
    app.run(debug=True)