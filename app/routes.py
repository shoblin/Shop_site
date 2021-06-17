# -*- coding: utf-8 -*-
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    post = {'title': 'Какой-то заголовок',
            'post':''}
    return render_template('index.html', post=post)
