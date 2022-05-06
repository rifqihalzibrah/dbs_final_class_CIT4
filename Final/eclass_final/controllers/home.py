from flask import (
    Blueprint, render_template, jsonify, request, redirect, url_for, flash, session
)
import eclass_final.services.topic as svc_topic

bp = Blueprint('', __name__)


@bp.route('/', methods=['GET'])
def home():
    topics, error = svc_topic.get_all()
    flash(error)
    return render_template('index.html', topics=topics)
