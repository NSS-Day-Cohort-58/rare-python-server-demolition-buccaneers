import sqlite3
import json
from models import Comment

def get_all_comments():
    #you can delete this array, just adding it so the function has something
    categories = []