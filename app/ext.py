from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_login import LoginManager
from flask_caching import Cache
from flask import Flask, app

db = SQLAlchemy()

migrate = Migrate()

def init_ext(app):

    config_db(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    init_login_config(app=app)
    init_upload_config(app=app)
    # init_cache_config(app=app)


def config_db(app):
    app.config['SECRET_KEY'] = '13131231321'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    migrate.init_app(app, db)


# cache = Cache()
#
#
# # 缓存配置111111111
# def init_cache_config(app):
#     # cache.init_app(app, config={'CACHE_TYPE': 'simple'})
#     cache.init_app(app, config={
#         # 默认的过期时间 单位秒
#         'CACHE_DEFAULT_TIMEOUT': 60,
#         # 缓存类型
#         'CACHE_TYPE': 'redis',
#         # IP地址
#         'CACHE_REDIS_HOST': '127.0.0.1',
#         # 端口
#         'CACHE_REDIS_PORT': 6379,
#         # 密码
#         # 连接数据库的编号
#         'CACHE_REDIS_DB': 1,
#         # 缓存key的前缀
#         'CACHE_KEY_PREFIX': 'view_'
#     })
#
#
# 用户模块插件1
login_manager = LoginManager()


def init_login_config(app):
    # 当用户点击某个需要登录才能访问的界面的时候,
    # 如果没有登录,就会自动跳转相应视图函数
    login_manager.login_view = 'user.login'
    login_manager.login_message = '必须要登录才能访问'
    login_manager.init_app(app)

images = UploadSet(name='images',extensions=IMAGES, default_dest=None)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH = os.path.join(BASE_DIR,'media/upload')

def init_upload_config(app):
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    # app.config['UPLPADS_DEFAULT_URL'] = ''
    configure_uploads(app=app,upload_sets=images)
    patch_request_class(app=app,size=32*1024*1024)
    login_manager.init_app(app)