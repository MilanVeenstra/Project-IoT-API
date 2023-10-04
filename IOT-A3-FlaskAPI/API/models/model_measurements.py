from API import db
from sqlalchemy import func


class Measurements(db.Model):
    __tablename__ = 'measurements'
    measurement_id = db.Column(db.Integer, primary_key=True)
    depth_id = db.Column(db.Integer, db.ForeignKey('depth.depth_id', ondelete="CASCADE"))
    temp_id = db.Column(db.Integer, db.ForeignKey('temperature.temp_id', ondelete="CASCADE"))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Depth(db.Model):
    __tablename__ = 'depth'
    depth_id = db.Column(db.Integer, primary_key=True)
    front_depth = db.Column(db.Integer(), nullable=False)
    back_depth = db.Column(db.Integer(), nullable=False)
    measurements = db.relationship('Measurements', backref='depth')


class Temperature(db.Model):
    __tablename__ = 'temperature'
    temp_id = db.Column(db.Integer, primary_key=True)
    outside_temp = db.Column(db.Integer(), nullable=False)
    engine_temp = db.Column(db.Integer(), nullable=False)
    measurements = db.relationship('Measurements', backref='temperature')
