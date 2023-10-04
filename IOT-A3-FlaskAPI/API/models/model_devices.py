from API import db
from sqlalchemy import func


class Devices(db.Model):
    __tablename__ = "devices"
    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(128), unique=True)
    device_key = db.Column(db.String(120), unique=True)

