from app.ext import db
import datetime


relation = db.Table('role_permission_relation',
                    db.Column('id',db.Integer,primary_key=True),
                    db.Column('per_id',db.Integer,db.ForeignKey('permission.per_id')),
                    db.Column('role_id',db.Integer,db.ForeignKey('role.role_id')))


class Role(db.Model):
    role_id = db.Column(db.Integer,primary_key=True)
    role_name = db.Column(db.String(64), nullable=False,index=True,unique=True)
    desc = db.Column(db.Text)
    permissions = db.relationship('Permission', secondary=relation)
    def __init__(self, role_name, desc):
        self.role_name = role_name
        self.desc = desc


class Permission(db.Model):
    per_id = db.Column(db.Integer,primary_key=True)
    per_name = db.Column(db.String(64),nullable=False,index=True,unique=True)
    desc = db.Column(db.Text)

    def __init__(self, per_name, desc):
        self.per_name = per_name
        self.desc = desc
