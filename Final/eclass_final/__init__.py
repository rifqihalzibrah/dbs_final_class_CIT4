from flask import Flask


def create_app():
    """ special function in Flask to use the Factory pattern """
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='THISISASECRETKEY'
    )

    from . import db
    db.init_app(app)  # connect the db to app to use teardown_appcontext

    from eclass_final.controllers import home, user, topic
    app.register_blueprint(home.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(topic.bp)

    return app