from flask_restful import Resource

from api.app import api


class DefaultResource(Resource):
    def get(self):
        return {"status":"success", "data":{"msg":"Hello World"}}

    def post(self):
        return {"status":"success", "data":{"msg":"Hello World from post"}} 

api.add_resource(DefaultResource, "/", endpoint="home")
