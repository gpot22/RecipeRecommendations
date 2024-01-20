from flask import Flask
from supabase import create_client, Client
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

url = "https://icvzwfgjdjyzvogalfsr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imljdnp3ZmdqZGp5enZvZ2FsZnNyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDUxNjY3MTksImV4cCI6MjAyMDc0MjcxOX0.RaiHts72Fap8jRjr5Lra0RsCsc9WtIm7KBaYAXMMbGY"
supabase: Client = create_client(url, key)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hiheyhellothere'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Recipe
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
        