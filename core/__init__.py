from flask import Flask
from .config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# blueprint for non-authentication parts of the app
from .task import task as task_blueprint
app.register_blueprint(task_blueprint)

from core import views
