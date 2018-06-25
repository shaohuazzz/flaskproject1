from flask import Flask, Blueprint
from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import get_app

app = get_app()
manager = Manager(app=app)
manager.add_command('start', Server(host='127.0.0.1', port=9000))
# 添加迁移的脚本
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()