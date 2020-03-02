from flask import Flask, request
from flask_restful import Resource, Api
import time

app = Flask(__name__)
api = Api(app)

user_list = {
    'Nick' :{
                'user_id': 'Nick',
                'create_time':'Tue Aug  2 07:47:02 2016',
                'search_history':{},
                'twitter_id': { 'twitter_texts':[],
                                'twitter_images':[],
                                'twitter_videos':[]
                                }
                },
    'Jason': {
                'user_id': 'Jason',
                'create_time':'Tue Aug  5 07:47:02 2016',
                'search_history':{},
                'twitter_id': { 'twitter_texts':[],
                                'twitter_images':[],
                                'twitter_videos':[]
                                }
                }
}

def initial_user(user_id):
    if user_id not in user_list:
            user_list[user_id]={
                                'user_id': user_id,
                                'create_time':time.ctime(),
                                'search_history':{},
                                'twitter_id': { 'twitter_texts':[],
                                                'twitter_images':[],
                                                'twitter_videos':[]
                                                }
                                 }


class UserList(Resource):
    def get(self):
        return user_list
    def put (self):
        user_id = request.form['user_id']
        initial_user(user_id)      
        return user_list[user_id]

    def delete(self):
        user_id = request.form['user_id']
        try:
            del user_list[user_id]
            return f'successfully delete {user_id}'
        except KeyError:
            return f"user_id {user_id} not found"

class tweets(Resource):
    def get(self, user_id):
        try:
            return user_list[user_id]
        except KeyError:
            return 'invalid user_id'
    def put (self, user_id):
        initial_user(user_id)
        twitter_id = request.form['twitter_id']
        ###
        ##
        # insert twitter api here do some action
        user_list[user_id]['search_history'][twitter_id] = time.ctime()
        return 'done'


api.add_resource(UserList, '/users')
api.add_resource(tweets, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)