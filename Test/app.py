from flask import Flask, send_from_directory, request
from flask import render_template
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    users = [{
        "name": 'AAAAAAA',
        "age": 23
    },
        {
            "name": 'AAAываAAAA',
            "age": 343
        },
        {
            "name": 'AAAAAAA',
            "age": 23
        },
        {
            "name": 'AAAываAAAA',
            "age": 343
        }
    ]
    pagination = Pagination(page=1, total=users.count(), search=True, record_name='users')
    user = {'nickname': 'Miguel'}  # выдуманный пользователь
    return render_template("index.html",
                           title='Home',
                           user=user)


if __name__ == '__main__':
    app.run(debug=True)
