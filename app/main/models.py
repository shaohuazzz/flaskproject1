from app.ext import db

class Shop(db.Model):
    shop_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(512),index=True)
    sub_title = db.Column(db.String(512),index=True)
    original_price = db.Column(db.Integer)
    promote_price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    cate_id = db.Column(db.Integer,db.ForeignKey('cate.cid'))
    create_date = db.Column(db.DateTime)
    cate = db.relationship('Cate', back_populates='shops')

class Cate(db.Model):
    cid = db.Column(db.Integer,primary_key=True)
    cname = db.Column(db.String(64),index=True,nullable=True,unique=True)
    shops = db.relationship('Shop',lazy='dynamic',back_populates='cate')

