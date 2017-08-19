#!/usr/bin/env python
#coding=utf-8

from flask import render_template,session,request,flash

from . import main
from . import forms
from .. import db
from ..models import Person

@main.route('/',methods=['GET'])
def index():
    return render_template('index.html',name=session.get('name'))

@main.route('/form',methods=['GET','POST'])
def form():
    form = forms.InfoForm()
    if form.validate_on_submit():
        res = request.form.to_dict()
        # print res
        name = res.get('name')
        age = res.get('age')
        gender = res.get('gender')
        mailAdd = res.get('mailAdd')
        note = res.get('note')
        person = Person(name=name,age=age,gender=gender,mailAdd=mailAdd,note=note)
        db.session.add(person)
        db.session.commit()
        session['name'] = name
        return render_template('success.html')
    elif request.method != 'GET':
        flash(u'验证未通过')

    return render_template('form.html',form=form)


@main.before_app_first_request
######stackoverflow真是个牛逼的网站。。这个地方注意了！
def init_database():
    db.create_all()