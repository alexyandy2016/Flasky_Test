#!/usr/bin/env python
#coding=utf-8

from app import create_app,db
from app.models import Person
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
#
app = create_app('development')
# manager = Manager(app)
# migrate = Migrate(app,db)
#
# def make_shell_context():
#     return dict(app=app,db=db,Person=Person)
#
# manager.add_command('shell',Shell(make_shell_context))
# manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)