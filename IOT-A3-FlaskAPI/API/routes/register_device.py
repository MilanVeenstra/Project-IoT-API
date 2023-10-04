from flask_restful import Resource, reqparse
from API.models.model_devices import *
from API.helpers.generate_key import generate_token

parser = reqparse.RequestParser()


class KeyRegister(Resource):
    def post(self):
        parser.add_argument('device_name', type=str, required=True, location='form')
        args = parser.parse_args()
        key = generate_token(32)
        device = Devices(device_name=args['device_name'], device_key=key)
        db.session.add(device)
        db.session.commit()

        return (f'Your key is {key}')