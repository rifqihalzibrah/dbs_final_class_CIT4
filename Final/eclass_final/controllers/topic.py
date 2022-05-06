from flask import (
    Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
)
import eclass_final.services.topic as svc_topic


bp = Blueprint('topic', __name__, url_prefix='/topic')


@bp.route('/detail/<int:id>', methods=['GET'])
def view(id):
    if not session.get('username'):
        return redirect(url_for('home'))

    topics, error = svc_topic.get_all()
    topic, error = svc_topic.get_by_id(id)
    flash(error)
    return render_template('topic/detail.html', topic=topic, topics=topics)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if session.get('user_id') != 0:
        return redirect(url_for('home'))

    err = ''
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        data = {
            'title': title.strip(),
            'body': body.strip()
        }
        _, error = svc_topic.save(data)
        if not error:
            return redirect(url_for('home'))

        flash(err)

    return render_template('topic/create.html')


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if session.get('user_id') != 0:
        return redirect(url_for('home'))

    err = ''
    topic, error = svc_topic.get_by_id(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        data = {
            'id': int(id),
            'title': title.strip(),
            'body': body.strip()
        }
        _, error = svc_topic.save(data)
        if not error:
            return redirect(url_for('home'))

        flash(err)

    return render_template('topic/edit.html', topic=topic)


@bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if session.get('user_id') != 0:
        return redirect(url_for('home'))

    topic, error = svc_topic.get_by_id(id)
    if request.method == 'POST':
        _, error = svc_topic.delete(id)
        if not error:
            return redirect(url_for('home'))

    flash(error)
    return render_template('topic/delete.html', topic=topic)


@bp.route('/submit/<int:id>', methods=['GET', 'POST'])
def submit(id):
    if not session.get('username'):
        return redirect(url_for('home'))
        
    err = ''
    topic, error = svc_topic.get_by_id(id)

    if request.method == 'POST':
        user_id = session.get('user_id')
        body = request.form['body']
        data = {
            'user_id': int(user_id),
            'topic_id': int(id),
            'body': body.strip()
        }
        _, error = svc_topic.submit(data)
        if not error:
            return redirect(url_for('home'))

        flash(err)

    return render_template('submit/student_submission.html', topic=topic)
