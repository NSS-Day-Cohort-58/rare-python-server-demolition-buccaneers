import sqlite3
import json
from models import Subscription

def get_all_subscriptions():
    #you can delete this array, just adding it so the function has something
    categories = []