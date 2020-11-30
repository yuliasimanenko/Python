from flask import Flask, send_from_directory, request
from SQL import SQL
from UpdateData import UpdateData

app = Flask(__name__)

POSTS_PER_PAGE = 5


@app.route('/')
def index1():
    return index('index.html')


@app.route('/<path>')
def index(path):
    return send_from_directory('content', path)


@app.route('/load')
def load():
    site = request.args.get('site', default='ecowars', type=str)
    db = SQL(site)
    updater = UpdateData(db)
    updater.update_fetch(site)
    return '200'


@app.route('/view')
def view():
    site = request.args.get('site', default='ecowars', type=str)
    page = request.args.get('page', default=1, type=int)
    db = SQL(site)
    limit = POSTS_PER_PAGE
    skip = limit * (page - 1)
    entries = db.get(skip, limit)
    return {
        'entries': entries
    }


@app.route('/add')
def add():
    url = request.args.get('url', default='ecowars', type=str)

    ret_name = UpdateData.add_url(url)
    if not isinstance(ret_name, str):
        return {'site': ""}, 500
    else:
        return {'site': ret_name}


if __name__ == '__main__':
    app.run(debug=True)
