from flask import Flask
from supabase import create_client, Client

url = "https://icvzwfgjdjyzvogalfsr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imljdnp3ZmdqZGp5enZvZ2FsZnNyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDUxNjY3MTksImV4cCI6MjAyMDc0MjcxOX0.RaiHts72Fap8jRjr5Lra0RsCsc9WtIm7KBaYAXMMbGY"
supabase: Client = create_client(url, key)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hiheyhellothere'
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app
