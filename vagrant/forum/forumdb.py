#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Clean up posts

def cleanUp():
    db = psycopg2.connect("dbname=forum")
    c= db.cursor()
    c.execute("DELETE from posts where content like '%spam%'")
    c.execute("DELETE from posts where content like '%pickles%'")
    c.execute("DELETE from posts where content like '%<script>%'")
    db.commit()
    db.close()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.
    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    cleanUp()
    db = psycopg2.connect("dbname=forum")
    c= db.cursor()
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = [{'content': str(row[1]), 'time': str(row[0])}
             for row in c.fetchall()]
    db.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.
    Args:
      content: The text content of the new post.
    '''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    c.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    db.commit()
    db.close()
