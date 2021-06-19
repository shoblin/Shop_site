# -*- coding: utf-8 -*-
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = 'Какой-то заголовок'
    posts = [{'title': 'Хачапури1', 'image': r'/static/img/2.jpg',
              'description': ['Ням-Ням.', 'Вкуснота... Беги покупай']},
             {'title': 'Хачапури2', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням2. Вкуснота2...', 'Беги покупай']},
             {'title': 'Хачапури3', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням3.', 'Вкуснота3... Беги покупай.', 'Варенье']},
             {'title': 'Хачапури2', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням2. Вкуснота2... Беги покупай']},
             {'title': 'Хачапури3', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням3.','Вкуснота3...', 'Беги покупай']}]
    return render_template('index.html', title=title, posts=posts)


@app.route('/shop_window')
def shop_window():
    return render_template('shop_windows.html')
