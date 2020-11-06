#-*- coding: utf8 -*-

from flask import Flask, request, render_template
from des import des

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'error': False, 'message': None, 'data': None, 'action': None}
    if request.method == 'GET':
        return render_template('index.html', name='index', result=result)
    else:
        key = request.form['key']
        text = request.form['text']
        d = des()
        try:
            result['action'] = request.form['action']
            if request.form['action'] == 'encrypt':
                result['data'] = d.encrypt(key, text, True)
            else:
                result['data'] = d.decrypt(key, text, True)
        except Exception as e:
            result['error'] = True
            result['message'] = e
        print(result['message'])
        return render_template('index.html', name='index', result=result)