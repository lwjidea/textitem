import os

from flask import Flask

from textapp.apis import init_api
from textapp.models import init_db
from .textblue import init_blue
from .sets import init_set
def create_app(version='text'):
    template_floder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"templates")
    static_floder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"static")
    print(template_floder)
    app = Flask(__name__,template_folder=template_floder,static_folder=static_floder,static_url_path="/static")
    init_set(version, app=app)
    init_db(app)
    init_api(app)
    init_blue(app)

    return app