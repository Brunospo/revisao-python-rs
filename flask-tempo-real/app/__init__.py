from flask import Flask
from .extensions import db
from .config import Config
from .controllers import payment_controller

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)

  # Register blueprints
  app.register_blueprint(payment_controller.bp)

  # Criar o banco, se não existir
  with app.app_context():
    db.create_all()

  return app
