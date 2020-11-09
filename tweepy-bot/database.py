import sqlite3
import logging
import json
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

''' 
    todo
        -Delete old tweets
        -cache tweets before sending

Connects with the database and if it is not present creates one named issue.db
'''
try:
    conn = sqlite3.connect('issue.db')
except Exception as e:
    logger.error("Error Connecting to Database", exc_info=True)
    raise e
    
c = conn.cursor()

def data_count():
    '''
    Returns the number of rows in the database
    '''
    x = c.execute("SELECT * FROM issue")
    conn.commit()
    count = len(c.fetchall())
    return count


def convertTuple(tup):
    '''
    convert a tuple to string
    '''
    stri =  ''.join(tup) 
    return stri




def create_schema():
    '''
    creates a table named issue, columns as ID, issue_text, url,
    to avoid tweets being repeted, the url column is set to unique so no two link is same
    '''
    
    c.execute("""CREATE TABLE IF NOT EXISTS issue (
            ID INTEGER PRIMARY KEY,
            issue_text TEXT,
            url TEXT NOT NULL UNIQUE,
            tweeted INTEGER NOT NULL DEFAULT 0
            )""")
    conn.commit()
    logger.info("Database Created!")

def insert_data(issue_title,issue_url):
    '''
    takes the issue title and issue url and inserts into the database
    '''
    try:
        c.execute("INSERT INTO issue (issue_text,url) VALUES (?,?)", (issue_title,issue_url))
        conn.commit()
        logger.info("Database Updated, New issue inserted!")
    except sqlite3.IntegrityError:
        pass
        logger.info("Dublicate Data, not inserted")

def get_issue():
    '''
    Gets the latest issue from the database where the tweeted colume is 0
    and updates the issue's tweeted colume to 1 
    '''
    try:
        c.execute("SELECT * FROM issue WHERE tweeted = 0 ORDER BY ID ASC LIMIT 1")

        conn.commit()
        data = c.fetchone()
        row_id = data[0]
        update_tweeted(row_id)
        txt = convertTuple(data[1:2]) + "\n" + convertTuple(data[2:3])
        return txt
    except:
        pass
        logger.info("No new data, Waiting for new data")



def clear_database():
    '''
    Clears the database
    '''
    try:
        c.execute("DELETE FROM issue WHERE tweeted = 1")
        conn.commit()
        logger.info("Database Cleared!")
    except:
        pass
        logger.info("No Data to Delete")

def update_tweeted(rid):
    '''
    changes the value of tweeted to 1
    '''
    c.execute("UPDATE issue SET tweeted = 1 WHERE ROWID = :id",{"id":rid})
    conn.commit()

create_schema()