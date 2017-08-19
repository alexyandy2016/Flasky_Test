#!/usr/bin/env python
#coding=utf-8

from . import db

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.Integer,nullable=False)
    mailAdd = db.Column(db.String(20))
    note = db.Column(db.Text)

    def repr(self):
        return '<Person %d> %s' % (self.id,self.name)
