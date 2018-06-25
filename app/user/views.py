from .models import Permission,Role
from flask import Blueprint
from app.ext import db
from operator import and_, or_
user = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user.route('/add/role/')
def add_role():
    role =Role('admin','超级管理员')
    db.session.add(role)
    db.session.add_all([Permission('delete','删除操作'),
                        Permission('update','更新操作'),
                        Permission('insert','添加操作'),
                        Permission('select','查看操作')])
    db.session.commit()
    return 'success'

@user.route('/add/role/per/')
def add_role_per():
    admin = Role.query.get(1)
    admin.permissions = Permission.query.all()
    db.session.commit()
    return 'success'

@user.route('/del/msg/')
def del_msg():
    if has_per():
        return '删除成功'
    else:
        return '删除失败'

def has_per():
    role = Role.query.get(1)
    for per in role.permissions:
        print(per.per_name)
        if per.per_name == 'delete':
            return True
    return False