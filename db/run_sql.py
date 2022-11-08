# import logging

import psycopg2
import psycopg2.extras as ext

DBNAME = 'music'

# logging.basicConfig(level=5)
# logger = logging.getLogger(__name__)
# logger.debug("Hello World")

def run_sql(sql: str, values: list = None, do_fetchall : bool = True) -> list[dict]:
    conn = None
    cur = None
    results = []

    try:
        # Connect to the DB
        # conn = psycopg2.connect(dsn=f"dbname='{DBNAME}'", connection_factory=ext.LoggingConnection)
        # conn.initialize(logger)
        conn = psycopg2.connect(f"dbname='{DBNAME}'")
        # Define a cursor
        cur = conn.cursor(cursor_factory = ext.DictCursor) # XXX THIS STOPS DEBUGGING WORKING
        # Execute the SQL
        cur.execute(sql, values)
        # Commit
        conn.commit()
        # Fetch the results
        # print(cur.rowcount)
        if do_fetchall:
            results = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        # Print an error
        print(type(error), ': ', error, sep='')
    finally:
        # Close the cursor
        if cur is not None:
            cur.close()
        # Close the connection
        if conn is not None:
            conn.close()

    return results