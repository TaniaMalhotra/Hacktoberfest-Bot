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


def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def insert_data(issue_title,issue_url):
    '''
    takes the issue title and issue url and inserts into the database
    '''
    try:
        c.execute("INSERT INTO issue (issue_text,url) VALUES (?,?)", (issue_title,issue_url))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
        logger.info("Database Updated!")


def create_schema():
    '''
    creates a table named issue, columns as ID, issue_text, url,
    to avoid tweets being repeted, the url column is set to unique so no two link is same
    '''
    
    c.execute("""CREATE TABLE IF NOT EXISTS issue (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            issue_text TEXT,
            url TEXT NOT NULL UNIQUE
            )""")
    conn.commit()
    logger.info("Database Created!")

def get_last_data():
    '''
    Gets the latest issue from the database
    '''
    c.execute("SELECT * FROM issue ORDER BY ID DESC LIMIT 1")
    conn.commit()
    data = c.fetchone()
    txt = convertTuple(data[1:2]) + "\n" + convertTuple(data[2:])
    return txt

def del_last_data():
    '''
    Deletes the latest row in the database
    '''
    x = c.execute("SELECT * FROM issue")
    count = len(c.fetchall())
    try:
        c.execute("DELETE FROM issue WHERE rowid = (?)", (count,))
        print("Data deleted")
    except:
        pass
        print("No more data in database")
    conn.commit()


