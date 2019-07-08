from flask_restful import Api
from .textapi import TextApi
def init_api(app):
    api=Api()
    api.add_resource(TextApi,"/api/text")
    api.init_app(app)