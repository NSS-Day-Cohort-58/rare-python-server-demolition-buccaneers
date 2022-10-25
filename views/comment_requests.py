import sqlite3
import json
from models import Comment, Post, User



def get_all_comments():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.post_id,
            m.author_id,
            m.content,
            a.id,
            a.user_id,
            a.category_id,
            a.title,
            a.publication_date,
            a.image_url,
            a.content post_content,
            a.approved,
            u.first_name first_name,
            u.last_name last_name,
            u.email email,
            u.bio bio,
            u.username username,
            u.password password,
            u.profile_image_url profile_image_url,
            u.created_on created_on,
            u.active active
        FROM Comments m
        JOIN Posts a
            ON a.id = m.post_id
        JOIN Users u
            ON u.id = m.author_id
        """)

        # Initialize an empty list to hold all post representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            #Create a Comment Instance from the Current Row
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])

            # Create an post instance from the current row
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['post_content'], row['approved'])
            
            #Create a Users instance from the current row
            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                        row['bio'], row['username'], row['password'], row['profile_image_url'],
                        row['created_on'], row['active'])

            # Add the dictionary representation of the post to the list
            comment.post = post.__dict__
            comment.user = user.__dict__
            comments.append(comment.__dict__)

    return comments