create = """
INSERT INTO events (
    start_date,
    end_date,
    name,
    url,
    comment
) VALUES (
    %(start_date)s,
    %(end_date)s,
    %(name)s,
    %(url)s,
    %(comment)s
)"""

all = """
SELECT *
FROM events
ORDER BY end_date, start_date"""

future = """
SELECT *
FROM events
WHERE end_date >= CURRENT_DATE
ORDER BY end_date, start_date"""
