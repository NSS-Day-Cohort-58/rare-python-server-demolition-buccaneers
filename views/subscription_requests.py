import sqlite3
import json
from models import Subscription

SUBSCRIPTIONS = [
    # ? Test data for subscription
    {"id": 1, "follower_id": 1, "author_id": 1, "created_on": 1666627368, "user": 1}
]


def get_all_subscriptions():
    # Open a connection to the database
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            s.publication_date,
            s.user,
        FROM subscription s
        """
        )

        # Initialize an empty list to hold all subscription representations
        subscriptions = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an subscription instance from the current row
            subscription = Subscription(
                row["id"],
                row["follower_id"],
                row["author_id"],
                row["created_on"],
            )

            # Add the dictionary representation of the subscription to the list
            subscriptions.append(subscription.__dict__)

    return subscriptions


def get_single_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute(
            """
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            s.user,
        FROM subscription s
        WHERE s.id = ?
        """,
            (id,),
        )

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an subscription instance from the current row
        subscription = Subscription(
            data["id"],
            data["follower_id"],
            data["author_id"],
            data["created_on"],
        )

        return subscription.__dict__


def create_subscription(new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO subscription
            ( user_id, follower_id, author_id, created_on, user )
        VALUES
            ( ?, ?, ?, ?, ?);
        """,
            (
                new_subscription["user_id"],
                new_subscription["follower_id"],
                new_subscription["author_id"],
                new_subscription["created_on"],
                new_subscription["user"],
            ),
        )

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the subscription dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_subscription["id"] = id

    return new_subscription


def delete_subscription(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        DELETE FROM subscription
        WHERE id = ?
        """,
            (id,),
        )


def update_subscription(id, new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE subscription
            SET
                follower_id = ?,
                author_id = ?,
                created_on = ?,
                user = ?,
        WHERE id = ?
        """,
            (
                new_subscription["follower_id"],
                new_subscription["author_id"],
                new_subscription["created_on"],
                new_subscription["user"],
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
