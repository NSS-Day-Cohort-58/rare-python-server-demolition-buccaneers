import sqlite3
import json
from models import Reaction

def get_all_reactions():
    #you can delete this array, just adding it so the function has something
    categories = []