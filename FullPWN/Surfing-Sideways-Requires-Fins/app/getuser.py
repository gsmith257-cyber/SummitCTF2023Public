import os
import sqlite3

DATABASE_PATH = os.path.join('/src/', 'db.sqlite')

def get_flag(username, password):
    
    # Connect to the database
    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()
    try: 
        cur.execute("SELECT flag FROM user WHERE username='%s' AND password='%s'" %(username,password))
        row = cur.fetchone()
        result= row[0] if row is not None else "Error"

    except Exception as e:
           result={ 'Exception: {}'.format(e)}
           #result= "Exception Error"

    finally:
           conn.commit()
           conn.close()
           return result