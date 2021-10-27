from flask import Blueprint, jsonify
from flask_restful import Resource, Api

api = Blueprint('api', __name__)
modul_api = Api(api)


class Main(Resource):
    """Search endpoint returning number of occurrences across all registered resources"""

    def get(self):
        """
        Basic Get Method
        ---
        tags:
          - Main
        produces:
          - application/json
        responses:
          '200':
            description: Return state of the module
        """
        return jsonify('Status: Running')


modul_api.add_resource(Main, '/api')


