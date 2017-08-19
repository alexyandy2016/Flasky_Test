#!/usr/bin/env python
#coding=utf-8
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'franknihao'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://weiyz:123456@192.168.1.105:3306/flask_DB?charset=utf8'

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}
