# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/xjzx'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopConfig(Config):
    DEBUG = True