from flask import Flask

from app.ext import init_ext
from app.main.views import main
from app.user.views import user
from app.upload.views import upload_blue

# 实例化flask对象
app = Flask(__name__)
app.debug = True


def get_app():
    register_blue()
    init_ext(app=app)
    return app


# 奥克米
# 统一注册所有的蓝图对象
def register_blue():
    app.register_blueprint(main, url_prefix='/main')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(upload_blue, url_prefix='/upload')
    # app.register_blueprint(user, url_prefix='/cache01')