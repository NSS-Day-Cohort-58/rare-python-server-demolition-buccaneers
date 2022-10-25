import sqlite3
import json
from models import Post_Tag


import sqlite3
import json
from models import PostTag


def get_all_posttags():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
                      SELECT
                        pt.id,
                        pt.post_id,
                        pt.tag_id
                        
                       

                    FROM PostTag pt
                   
                        """
        )

        # Initialize an empty list to hold all posttag representations
        posttags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an tag instance from the current row
            posttag = PostTag(row["id"], row["post_id"], row["tag_id"])

            # Add the dictionary representation of the tag to the list
            posttags.append(posttag.__dict__)

    return json.dumps(posttags)


def get_single_posttag(id):
    with sqlite3.connect(".db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
                    SELECT
                        pt.id,
                        pt.post_id,
                        pt.tag_id
                       
                    FROM PostTag pt
                    WHERE pt.id = ?
                    """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an posttag instance from the current row
        posttag = PostTag(data["id"], data["post_id"], data["tag_id"])

        return posttag.__dict__


def create_posttag(new_posttag):
    with sqlite3.connect(".db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                 SELECT * FROM PostTag ORDER BY id DESC;
        """,
            (new_posttag["label"]),
        )

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the post dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_posttag["id"] = id

    return new_posttag


def delete_posttag(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM post
        WHERE id = ?
        """,
            (id,),
        )


def update_posttag(id, new_posttag):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Tag
            SET
                label = ?
        WHERE id = ?
        """,
            (
                new_posttag["label"],
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
