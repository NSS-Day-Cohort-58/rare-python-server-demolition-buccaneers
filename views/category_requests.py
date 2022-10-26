import sqlite3
import json
from models import Category


def get_all_categories():
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row['id'], row['label'])
            categories.append(category.__dict__)

        return categories


def get_single_category(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        category = Category(data['id'], data['label'])

        return category.__dict__

# getting the error ProgrammingError: Incorrect number of bindings supplied.
# The current statement uses 1, and there are 10 supplied.
# def create_category(new_category):
#     with sqlite3.connect("./db.sqlite3") as conn:
#         db_cursor = conn.cursor()

#         db_cursor.execute(
#             """
#         INSERT INTO Categories
#             ( label )
#         VALUES
#             (?);
#         """,
#             (
#                 new_category["label"]
#             )
#         )
#         # The `lastrowid` property on the cursor will return
#         # the primary key of the last thing that got added to
#         # the database.
#         id = db_cursor.lastrowid

#         # Add the `id` property to the post dictionary that
#         # was sent by the client so that the client sees the
#         # primary key in the response.
#         new_category["id"] = id

#     return new_category


def delete_category(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Categories
        WHERE id = ?
        """, (id, ))


def update_category(id, new_category):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET
                label = ?
        WHERE id = ?
        """, (new_category['label'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
