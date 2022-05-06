from flask import session
from eclass_final.db import get_db


def get_all_topics():
    """ function to get all of the topics in database """
    error = ''
    db = get_db()
    cur = db.cursor()
    sql = """
        SELECT id, title, body FROM topics ORDER BY id
    """
    cur.execute(sql)
    topics = cur.fetchall()
    cur.close()

    return topics, error


def get_topic_by_id(id):
    """ function to get topic by id """
    error = ''
    db = get_db()
    cur = db.cursor()
    sql = """
        SELECT id, title, body FROM topics WHERE id = %d
    """ % (int(id))
    cur.execute(sql)
    topic = cur.fetchone()
    cur.close()

    if not topic:
        error = 'Invalid topic with id: %d' % id

    return topic, error


def create_topic(data):
    """ function to create topic based on data dict """
    # trust that data is already complete
    error = ''
    db = get_db()
    cur = db.cursor()
    try:
        sql = """
            INSERT INTO topics (title, body) VALUES ('%s', '%s')
        """ % (data.get('title'), data.get('body'))
        cur.execute(sql)
        db.commit()
    except db.IntegrityError as e:
        error = e
    cur.close()
    return None, error


def update_topic(data):
    """ function to update topic based on data dict """
    # trust that data is already complete
    error = ''
    db = get_db()
    cur = db.cursor()
    try:
        sql = """
            UPDATE topics SET title = '%s', body = '%s' WHERE id = %d
        """ % (data.get('title'), data.get('body'), data.get('id'))
        cur.execute(sql)
        db.commit()
    except db.IntegrityError as e:
        error = e
    cur.close()
    return None, error


def delete_topic(id):
    """ function to delete topic based on id """
    error = ''
    db = get_db()
    cur = db.cursor()
    try:
        sql = """
            DELETE FROM topics WHERE id = %d
        """ % (int(id))
        cur.execute(sql)
        db.commit()
    except db.IntegrityError as e:
        error = 'The topic have submission of students, it cannot be deleted.'
    except db.DatabaseError as e:
        error = e

    cur.close()
    return None, error


def topic_submission(data):
    """ function to submiy topic for student based on data dict """
    # trust that data is already complete
    error = ''
    db = get_db()
    cur = db.cursor()
    try:
        sql = """
            INSERT INTO submissions (user_id, topic_id, body) VALUES (%d, %d, '%s')
        """ % (session.get('user_id'), data.get('topic_id'), data.get('body'))
        cur.execute(sql)
        db.commit()
    except db.IntegrityError as e:
        error = e
    cur.close()
    return None, error