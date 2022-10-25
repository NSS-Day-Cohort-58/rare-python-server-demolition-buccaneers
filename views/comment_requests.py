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

def get_comments_by_post(post):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.post_id,
            m.author_id,
            m.content
        FROM Comments m
        WHERE m.post_id = ?
        """, (post, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            comments.append(comment.__dict__)
    return comments

def create_comment(new_comment):
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments ( 
            'post_id', 
            'author_id', 
            'content')
        VALUES (?, ?, ?)
        """, (new_comment['post_id'], new_comment['author_id'], new_comment['content'],))
        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the post dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return new_comment

def get_single_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
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
        WHERE m.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        comment = Comment(data['id'], data['post_id'], data['author_id'], data['content'])

        post = Post(data['id'], data['user_id'], data['category_id'], data['title'],
                    data['publication_date'], data['image_url'], data['post_content'], data['approved'])
            
        user = User(data['id'], data['first_name'], data['last_name'], data['email'],
                    data['bio'], data['username'], data['password'], data['profile_image_url'],
                    data['created_on'], data['active'])

        # Add the dictionary representation of the comment to the list
        comment.post = post.__dict__
        comment.user = user.__dict__        
        return comment.__dict__
        
def delete_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM Comments
        WHERE id = ?
        """,
            (id,),
        )

def update_comment(id, new_comment):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Comments
            SET
                post_id = ?,
                author_id = ?,
                content = ?
        WHERE id = ?
        """,
            (
                new_comment["post_id"],
                new_comment["author_id"],
                new_comment["content"],
                id,
            ),
        )

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True