from flask import (
    Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
)
import eclass_final.services.user as svc_user

bp = Blueprint('user', __name__, url_prefix='/')


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        data = {
            'name': name.strip(),
            'username': username.strip(),
            'password': password.strip(),
        }
        _, error = svc_user.signup(data)
        if not error:
            return redirect(url_for('home'))

        flash(error)

    return render_template('user/signup.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data = {
            'username': username.strip(),
            'password': password.strip(),
        }
        _, error = svc_user.login(data)
        if not error and username == 'admin':
            return redirect(url_for('user.admin'))
        if not error and not username == 'admin':
            return redirect(url_for('home'))

        flash(error)

    return render_template('user/login.html')


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    """ function to do logout """
    session.clear()  # clear all sessions
    return redirect(url_for('home'))


@bp.route('/people_list', methods=['GET', 'POST'])
def get_all_users():
    if session.get('user_id') != 0:
        return redirect(url_for('home'))

    users, error = svc_user.get_all_users()
    flash(error)
    return render_template('user/list.html', users=users)


@bp.route('/classworks', methods=['GET', 'POST'])
def get_all_works():
    if session.get('user_id') != 0:
        return redirect(url_for('home'))
        
    works, error = svc_user.get_all_works()
    flash(error)
    return render_template('submit/student_work.html', works=works)