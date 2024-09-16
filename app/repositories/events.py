from .connection import connect
from .sql import events as sql_events


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


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_events.all)

            return cursor.fetchall()
