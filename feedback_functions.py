import constants
import datetime
import pytz
import db_functions

def get_current_date():
    tz = pytz.timezone(constants.LOCAL_TIME)
    date = datetime.datetime.now(tz).date()
    return str(date)

def update_feedback(data):
    data = dict(data)
    data['date'] = get_current_date()
    result = db_functions.update_feedback(data)
    return result

def get_today():
    date = get_current_date()
    data = db_functions.get_feedback_by_date(date)
    return data

def get_alltime():
    data = db_functions.get_feedback_all_time()
    return data