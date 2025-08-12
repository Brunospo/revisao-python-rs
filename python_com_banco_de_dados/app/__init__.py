from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = "OGNRDÇIDEG8ERGEHGPIER8EU"

  db.init_app(app)
  login_manager.init_app(app)

  #view login
  # login_manager.login_view = 'login' # é usado melhor com renderização de templates, ele redireciona para essa página

  from models.user import User

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))
  
  @login_manager.unauthorized_handler
  def unauthorized():
    return {"message": "Autenticação necessária"}, 401

  from .routes import register_routes
  register_routes(app)

  with app.app_context():
    db.create_all()

  return app