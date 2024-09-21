from .connection import connect
from .sql import events as sql_events

from psycopg.rows import class_row, dict_row


def create(start_date, end_date, name, url=None, comment=None):
    if not url:
        url = ""

    if not comment:
        comment = ""

    with connect() as conn:
        with conn.cursor() as cursor:
            params = {
                "start_date": start_date,
                "end_date": end_date,
                "name": name,
                "url": url,
                "comment": comment,
            }

            cursor.execute(sql_events.create, params)


def all(model=None):
    with connect() as conn:
        row_factory = class_row(model) if model else dict_row
        with conn.cursor(row_factory=row_factory) as cursor:
            cursor.execute(sql_events.all)

            return cursor.fetchall()


def future(model=None):
    with connect() as conn:
        row_factory = class_row(model) if model else dict_row
        with conn.cursor(row_factory=row_factory) as cursor:
            cursor.execute(sql_events.future)

            return cursor.fetchall()
