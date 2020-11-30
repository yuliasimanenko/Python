from flask import Flask, send_from_directory, request
from SQL import SQL
from UpdateData import UpdateData

app = Flask(__name__)
# db = SQL('rss.db')
# updater = UpdateData(db)
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
    limit = 5
    skip = limit * (page - 1)
    entries = db.get(skip, limit)
    print("view worked")
    return {
        'entries': entries
    }


if __name__ == '__main__':
    app.run(debug=True)
