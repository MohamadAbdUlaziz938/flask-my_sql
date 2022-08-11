from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import app_config
import os

ROOT_DIR = os.path.dirname(os.path.abspath("config.py"))
app = Flask(__name__)
app.config.from_object(app_config['development'])
app.config.from_pyfile(ROOT_DIR + '/config.py')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app.models import user
