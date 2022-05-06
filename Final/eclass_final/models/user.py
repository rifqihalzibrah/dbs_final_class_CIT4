from flask import session
from eclass_final.db import get_db

def signup(data):
    """ function to signup based on data dict """
    error = ''
    db = get_db()
    cur = db.cursor()
    try:
        sql = """
            INSERT INTO users (name, username, password) VALUES ('%s', '%s', '%s')
        """ % (data.get('name'), data.get('username'), data.get('password'))
        cur.execute(sql)
        db.commit()
    except db.IntegrityError as e:
        error = e
    cur.close()
    return None, error


def login(data):
    """ function to get user by data for login"""
    error = ''
    db = get_db()
    cur = db.cursor()
    sql = """
        SELECT id, username FROM users WHERE username = '%s' AND password = '%s'
    """ % (data.get('username'), data.get('password'))
    cur.execute(sql)
    user = cur.fetchone()
    cur.close()

    if user is None:
        error = 'Wrong credentials. No user found'
    else:
        session.clear()
        session['user_id'] = user[0]
        session['username'] = user[1]

    return user, error


def get_all_users():
    """ function to get all users in database """
    error = ''
    db = get_db()
    cur = db.cursor()
    sql = """
        SELECT id, username, name, password FROM users ORDER BY id
    """
    cur.execute(sql)
    users = cur.fetchall()
    cur.close()

    return users, error


def get_all_works():
    """ function to get all student works in database """
    error = ''
    db = get_db()
    cur = db.cursor()
    sql = """
        SELECT submissions.id, users.name, submissions.topic_id, submissions.body FROM submissions 
        JOIN users ON users.id = submissions.user_id
        ORDER BY submissions.user_id
    """
    cur.execute(sql)
    works = cur.fetchall()
    cur.close()

    return works, error