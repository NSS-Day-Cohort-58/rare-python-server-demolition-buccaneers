import sqlite3
import json
from models import Demotion_Queue

def get_all_demotion_queues():
    #you can delete this array, just adding it so the function has something
    categories = []