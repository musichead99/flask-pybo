from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy() #create_app() 함수에서 db객체 생성시 다른 모듈에서 불러올 수 없음
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # Blueprint
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app

