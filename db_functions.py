import pymongo
import json
import app_config
from datetime import datetime 

mongo_client = pymongo.MongoClient(app_config.MONGO_DB_CONNECTION_STRING)

db = mongo_client["feedback_wall"]
collection_feedback = db["feedback"]
collection_feedback_daily = db["feedback_daily"]

def update_feedback(data):
    date = data["date"]
    old_data = get_feedback_by_date(date)
    new_data = None
    
    if old_data is not None:
        new_data = old_data
        update_query =  {
                            '$set': {
                                
                                'like' : new_data['like'] + data['like'],
                                'dislike' : new_data['dislike'] + data['dislike'],
                                'neutral' : new_data['neutral'] + data['neutral']
                            }

                        }

        query = {"date": date}
        collection_feedback_daily.update_one(query, update_query, upsert=True)
    else:
        new_data = data
        collection_feedback_daily.insert_one(new_data)

    return new_data

def get_feedback_by_date(date):
    query = {"date":date}
    data = collection_feedback_daily.find(query,projection={'_id':False})
    return None if data.count() == 0 else dict(data[0])

def get_feedback_all_time():
    query = [{
        "$group": 
            {
                '_id': '',
                'like': {'$sum' : '$like'},
                'dislike': {'$sum' : '$dislike'},
                'neutral': {'$sum' : '$neutral'}

        }
    }]

    data = collection_feedback_daily.aggregate(query)
    return data