from flask import abort, jsonify, request
from flask_restful import Resource
from API import db
from API.models.model_measurements import *
from API.models.model_logs import *
from API.auth.validate_key import *
from sqlalchemy import desc


class DataGet(Resource):
    def get(self, command):
        api_key = request.args.get('api_key')
        try:
            device = validate_key(api_key)
        except InvalidAPIKeyError:
            abort(401, 'Invalid API key.')
        else:
            data = []

            new_log = Logs(log_activity=f'{device.device_name} heeft request gedaan om data in te zien',
                           device_id=device.device_id)
            db.session.add(new_log)
            db.session.commit()

            if command == 'all':
                query = db.session.query(Measurements.measurement_id, Measurements.date,
                                         Temperature.outside_temp,
                                         Temperature.engine_temp,
                                         Depth.front_depth,
                                         Depth.back_depth).join(Depth).join(Temperature).order_by(
                    desc(Measurements.date)).limit(20).all()

                query.reverse()
                for x in query:
                    measurements = {
                        'time': x[1],
                        'temperature_outside': x[2],
                        'temperature_engine': x[3],
                        'front_depth': x[4],
                        'back_depth': x[5]
                    }

                    data.append({
                        'id_' + str(x[0]): measurements
                    })

                return jsonify(data)
            elif command == 'recent':
                query = db.session.query(Measurements.measurement_id, Measurements.date,
                                         Temperature.outside_temp,
                                         Temperature.engine_temp,
                                         Depth.front_depth,
                                         Depth.back_depth).join(Depth).join(Temperature).order_by(
                    desc(Measurements.date)).first()

                if query:
                    measurements = {
                        'time': query[1],
                        'temperature_outside': query[2],
                        'temperature_engine': query[3],
                        'front_depth': query[4],
                        'back_depth': query[5]
                    }

                    data.append({
                        'id_' + str(query[0]): measurements
                    })
                return jsonify(data)

            else:
                abort(404, f'Command {command} not valid.')
