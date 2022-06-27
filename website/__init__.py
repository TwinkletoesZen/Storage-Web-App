from flask import Flask

def create_thing():
  web_app = Flask(__name__)

  from .views import main_views
  web_app.register_blueprint(main_views, url_prefix = "/")

  return web_app

