from flask import abort, jsonify
from flask_restful import Resource, reqparse
from API import db
from API.models.model_measurements import *
from API.models.model_logs import *

parser = reqparse.RequestParser()


class DataPost(Resource):
    def post(self):
        parser.add_argument('outside_temperature', type=float, required=True, location='form')
        parser.add_argument('front_depth', type=float, required=True, location='form')
        parser.add_argument('engine_temperature', type=float, required=True, location='form')
        parser.add_argument('back_depth', type=float, required=True, location='form')
        args = parser.parse_args()

        new_depth = Depth(front_depth=args['front_depth'], back_depth=args['back_depth'])
        db.session.add(new_depth)

        new_temperature = Temperature(outside_temp=args['outside_temperature'], engine_temp=args['engine_temperature'])
        db.session.add(new_temperature)

        new_measurement = Measurements(depth=new_depth, temperature=new_temperature)
        db.session.add(new_measurement)
        db.session.commit()

        new_meting = {'engine_temperature': args['engine_temperature'],
                      'outside_temperature': args['outside_temperature'], 'front_depth': args['front_depth'],
                      'back_depth': args['back_depth']}
        return new_meting, 201
