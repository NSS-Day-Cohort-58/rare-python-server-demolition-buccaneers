import sqlite3
import json
from models import Subscription, User

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
            u.first_name follower_first_name,
            u.last_name follower_last_name,
            u.email follower_email,
            u.bio follower_bio,
            u.username follower_username,
            u.password follower_password,
            u.profile_image_url follower_profile_image_url,
            u.created_on follower_created_on,
            u.active follower_active,
            us.first_name author_first_name,
            us.last_name author_last_name,
            us.email author_email,
            us.bio author_bio,
            us.username author_username,
            us.password author_password,
            us.profile_image_url author_profile_image_url,
            us.created_on author_created_on,
            us.active author_active
        FROM Subscriptions s
        JOIN Users u
            ON u.id = s.follower_id
        JOIN Users us
            ON us.id = s.author_id
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
            follower = User(
                row["follower_id"],
                row["follower_first_name"],
                row["follower_last_name"],
                row["follower_email"],
                row["follower_bio"],
                row["follower_username"],
                row["follower_password"],
                row["follower_profile_image_url"],
                row["follower_created_on"],
                row["follower_active"],
            )
            author = User(
                row["author_id"],
                row["author_first_name"],
                row["author_last_name"],
                row["author_email"],
                row["author_bio"],
                row["author_username"],
                row["author_password"],
                row["author_profile_image_url"],
                row["author_created_on"],
                row["author_active"],
            )

            # Add the dictionary representation of the subscription to the list
            subscription.follower = follower.__dict__
            subscription.author = author.__dict__
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
            u.first_name follower_first_name,
            u.last_name follower_last_name,
            u.email follower_email,
            u.bio follower_bio,
            u.username follower_username,
            u.password follower_password,
            u.profile_image_url follower_profile_image_url,
            u.created_on follower_created_on,
            u.active follower_active,
            us.first_name author_first_name,
            us.last_name author_last_name,
            us.email author_email,
            us.bio author_bio,
            us.username author_username,
            us.password author_password,
            us.profile_image_url author_profile_image_url,
            us.created_on author_created_on,
            us.active author_active
        FROM Subscriptions s
        JOIN Users u
            ON u.id = s.follower_id
        JOIN Users us
            ON us.id = s.author_id
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
            data["created_on"]
        )
        follower = User(
            data["follower_id"],
            data["follower_first_name"],
            data["follower_last_name"],
            data["follower_email"],
            data["follower_bio"],
            data["follower_username"],
            data["follower_password"],
            data["follower_profile_image_url"],
            data["follower_created_on"],
            data["follower_active"],
        )
        author = User(
            data["author_id"],
            data["author_first_name"],
            data["author_last_name"],
            data["author_email"],
            data["author_bio"],
            data["author_username"],
            data["author_password"],
            data["author_profile_image_url"],
            data["author_created_on"],
            data["author_active"],
        )
        subscription.follower = follower.__dict__
        subscription.author = author.__dict__
        return subscription.__dict__


def create_subscription(new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        INSERT INTO Subscriptions
            (follower_id, author_id, created_on)
        VALUES
            ( ?, ?, ?);
        """,
            (
                new_subscription["follower_id"],
                new_subscription["author_id"],
                new_subscription["created_on"],
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
        DELETE FROM Subscriptions
        WHERE id = ?
        """,
            (id,),
        )


def update_subscription(id, new_subscription):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
        UPDATE Subscriptions
            SET
                follower_id = ?,
                author_id = ?,
                created_on = ?
        WHERE id = ?
        """,
            (
                new_subscription["follower_id"],
                new_subscription["author_id"],
                new_subscription["created_on"],
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
