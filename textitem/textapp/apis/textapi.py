from flask_restful import Resource

class TextApi(Resource):
    def get(self):
        return {"hello":"world"}