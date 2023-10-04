from API import db
from sqlalchemy import func
from .model_devices import *

class Logs(db.Model):
    __tablename__ = "logs"
    log_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    log_activity = db.Column(db.Text, nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    device = db.relationship('Devices', backref='logs')


