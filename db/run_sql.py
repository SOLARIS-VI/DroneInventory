# db/run_sql.py
# Utility functions for running SQL queries

import psycopg2
import psycopg2.extras as ext


# Function for running SQL queries
def run_sql(sql, values=None):
    conn = None
    results = []
    
    try:
        conn = psycopg2.connect("dbname='drone_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        if cur.description:
            results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    return results









