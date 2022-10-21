import sqlite3
import json
from models import Post

def get_all_posts():
    #you can delete this array, just adding it so the function has something
    categories = []