# -*- coding: utf-8 -*-
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = 'Какой-то заголовок'
    categories = [{'id': 1, 'name': 'Хачапури'}, {'id': 2, 'name': 'Сладкие Хачапури'}, {'id': 3, 'name': 'Торты'}]
    posts = [{'id_categ': 1, 'title': 'Хачапури1', 'image': r'/static/img/2.jpg',
              'description': ['Ням-Ням.', 'Вкуснота... Беги покупай']},
             {'id_categ': 2, 'title': 'Хачапури2', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням2. Вкуснота2...', 'Беги покупай']},
             {'id_categ': 1, 'title': 'Хачапури3', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням3.', 'Вкуснота3... Беги покупай.', 'Варенье']},
             {'id_categ': 2, 'title': 'Хачапури4', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням2. Вкуснота2... Беги покупай']},
             {'id_categ': 1, 'title': 'Хачапури5', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням3.', 'Вкуснота3...', 'Беги покупай']},
             {'id_categ': 1, 'title': 'Хачапури2', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням2. Вкуснота2...', 'Беги покупай']},
             {'id_categ': 3, 'title': 'Хачапури3', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням3.', 'Вкуснота3... Беги покупай.', 'Варенье']},
             {'id_categ': 3, 'title': 'Хачапури4', 'image': r'/static/img/logo.jpg',
              'description': ['Ням-Ням2. Вкуснота2... Беги покупай']},
             {'id_categ': 3, 'title': 'Хачапури5', 'image': r'/static/img/1.jpg',
              'description': ['Ням-Ням3.', 'Вкуснота3...', 'Беги покупай']}
             ]
    return render_template('index.html', title=title, posts=posts, categories=categories)


@app.route('/shop_window')
def shop_window():
    return render_template('shop_windows.html')
