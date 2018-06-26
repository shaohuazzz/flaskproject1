import datetime
import json
import time

from flask import Blueprint, render_template, jsonify ,request,redirect

from app.ext import db
from .models import Shop ,Cate

main = Blueprint('main', __name__)

@main.route('/all/')
def all_1():
    return redirect('/main/all/1/10/')


@main.route('/all/<int:page>/<int:size>/',methods=['GET','POST'])
def all(page,size):
    # shops = Shop.query.all()
    paginate = Shop.query.order_by(Shop.shop_id).paginate(page=page,per_page=size,error_out=False)
    shops = paginate.items
    return render_template('main.html',shops=shops,paginate=paginate)


# 增
@main.route('/add/')
def add():
    return render_template('add.html')

@main.route('/index/',methods = ['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        sub_title = request.form.get('sub_title')
        original_price = request.form.get('original_price')
        promote_price = request.form.get('promote_price')
        stock = request.form.get('stock')
        cate_id = request.form.get('cate_id')
        shop = Shop(name=name,
                   sub_title=sub_title,
                   original_price=original_price,
                   promote_price=promote_price,
                    stock=stock,
                    cate_id=cate_id,
                   )
        db.session.add(shop)
        db.session.commit()
        return render_template('index.html')

@main.route('/save/')
def save_all():
    objects = []
    for i in range(151,201):
        objects.append(Shop(name='test'+str(i),
               sub_title='test_1'+str(i),
               original_price=100+i,
               promote_price=50+i,
               stock=4,
               cate_id=4,))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return '批量保存'

@main.route('/savecate/')
def savecate():
    objects = []
    for i in range(1,5):
        objects.append(Cate(
            cname='TEXT'+str(i)
        ))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return '批量保存'

# 删
@main.route('/delate/<int:id>/')
def delate(id):
    shop = Shop.query.filter(Shop.shop_id==id).first()
    db.session.delete(shop)
    db.session.commit()
    return render_template('delate.html',shop=shop)


# 改
@main.route('/update/<int:id>')
def update(id):
    return render_template('update.html',id=id)

@main.route('/index1/',methods = ['POST','GET'])
def index1():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        sub_title = request.form.get('sub_title')
        original_price = request.form.get('original_price')
        promote_price = request.form.get('promote_price')
        stock = request.form.get('stock')
        cate_id = request.form.get('cate_id')
        shop_id = request.form.get('shop_id')
        Shop.query.filter(Shop.shop_id==shop_id).update({Shop.name:name,
                                                         Shop.sub_title:sub_title,
                                                         Shop.original_price:original_price,
                                                         Shop.promote_price:promote_price,
                                                         Shop.stock:stock,
                                                         Shop.cate_id:cate_id})
        db.session.commit()
        return render_template('index.html')



# 查
import logging
@main.route('/find/',methods= ['GET','POST'])
def find():
    if request.method == 'GET':
        return render_template('find.html')
    if request.method == 'POST':
        text = request.form.get('text')
        shops= Shop.query.filter(Shop.name.ilike('%'+text+'%')).all()
        return render_template('find_end.html',shops=shops)
    # cates =Cate.query.all()
    # for shop in cates[0].shops:
    #     logging.debug(shop.name)
    #     # print(shop.name)
    #
    # shop = Shop.query.get(1)
    # print(shop.name)
    # print(shop.cate.cname)
    # shops = Cate.query.get(1).shops
    # for shop in shops:
    #     print(shop.name)
    # print(shops)
    # return '111'11111

@main.route('/cate/')
def cate():
    cates = Cate.query.all()
    return render_template('cate.html',cates=cates)

@main.route('/cate/<int:cid>/')
def cateshop(cid):
    print(cid)
    shops = Cate.query.get(cid==cid).shops
    return render_template('cateshop.html',shops=shops)