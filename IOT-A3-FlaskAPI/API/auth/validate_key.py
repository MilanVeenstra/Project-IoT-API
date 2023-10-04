from API import db
from API.models.model_devices import *


def validate_key(key):
    device = Devices.query.filter_by(device_key=key).first()

    if device is None:
        raise InvalidAPIKeyError('Invalid API key.')
    else:
        return device


class InvalidAPIKeyError(Exception):
    pass
