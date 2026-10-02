from flask import Flask
import os
from flask import render_template
import yaml
import string
import re


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reading/')
def reading():
    books_dict = yaml.safe_load(open('knowledge/books.yml', 'r'))
    recomendations = books_dict['Recommend']
    return render_template('reading.html',
                           title='Reading',
                           year_only=True,
                           block_to_books={'I recommend': recomendations})


@app.route('/reading_history/')
def reading_history():
    books_dict = yaml.safe_load(open('knowledge/books.yml', 'r'))
    all_books = books_dict['Reading History']
    return render_template('reading.html',
                           title='Books I Have Read',
                           block_to_books={
                              'Reading History (2015-present)': all_books})


@app.route('/photos/')
def photos():
    return render_template('photos.html',
                           title='Photos',
                           photos={})


@app.route('/ml_afternoon/')
def ml_afternoon():
    path = os.path.join(app.root_path, 'templates/ml_afternoon/')
    files = next(os.walk(path))[2]
    lectures, slides, homeworks, practicals = {}, {}, {}, {}
    for _file in files:
        if _file.endswith('.html'):
            without_ext = os.path.splitext(_file)[0]
            name = string.capwords(re.sub('_', ' ', without_ext))
            name = re.sub(r'(\d+) ', r'\1. ', name)
            if name.endswith('.slides'):
                slides[name] = '../ml_afternoon/{}/'.format(without_ext)
            elif name.lower().startswith('homework'):
                homeworks[name] = '../ml_afternoon/{}/'.format(without_ext)
            elif name.lower().startswith('practical'):
                practicals[re.sub('ractical', '', name)] = '../ml_afternoon/{}/'.format(without_ext)
            else:
                lectures[name] = '../ml_afternoon/{}/'.format(without_ext)
    return render_template('ml_afternoon.html',
                           title='Machine Learning Course',
                           lectures=sorted(lectures.items()),
                           homeworks=sorted(homeworks.items()),
                           practicals=sorted(practicals.items()),
                           slides=sorted(slides.items()))


@app.route('/ml_evening/')
def ml_evening():
    path = os.path.join(app.root_path, 'templates/ml_evening/')
    files = next(os.walk(path))[2]
    lectures, slides, homeworks, practicals = {}, {}, {}, {}
    for _file in files:
        if _file.endswith('.html'):
            without_ext = os.path.splitext(_file)[0]
            name = string.capwords(re.sub('_', ' ', without_ext))
            name = re.sub(r'(\d+) ', r'\1. ', name)
            if name.endswith('.slides'):
                slides[name] = '../ml_evening/{}/'.format(without_ext)
            elif name.lower().startswith('homework'):
                print(_file)
                homeworks[name] = '../ml_evening/{}/'.format(without_ext)
            elif name.lower().startswith('practical'):
                practicals[re.sub('ractical', '', name)] = '../ml_evening/{}/'.format(without_ext)
            else:
                lectures[name] = '../ml_evening/{}/'.format(without_ext)
    return render_template('ml_evening.html',
                           title='Machine Learning Course',
                           lectures=sorted(lectures.items()),
                           homeworks=sorted(homeworks.items()),
                           practicals=sorted(practicals.items()),
                           slides=sorted(slides.items()))


@app.route('/ml_afternoon/<string:lecture_name>/')
def ml_afternoon_lectures(lecture_name):
    return render_template('ml_afternoon/%s.html' % lecture_name)


@app.route('/ml_evening/<string:lecture_name>/')
def ml_evening_lectures(lecture_name):
    return render_template('ml_evening/%s.html' % lecture_name)
