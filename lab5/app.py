from flask import Flask, send_from_directory, request
import functions as f

app = Flask(__name__)


@app.route('/')
def index1():
    return index('index.html')


@app.route('/<path>')
def index(path):
    return send_from_directory('content', path)


@app.route('/img/<path>')
def img(path):
    return send_from_directory('content/img', path)


@app.route('/get_options')
def get_options():
    mapping = {
        1: 10,
        2: 50,
        3: 100
    }
    level = request.args.get('level', default=1, type=int)
    count = mapping[level]
    variants = f.get_names(count)
    person = f.choose_name(variants)
    url = f.get_img_link(person)
    return {
        'names': variants,
        'url': url,
        'person': person
    }


if __name__ == '__main__':
    app.run(debug=True)
