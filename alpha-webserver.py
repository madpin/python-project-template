#!flask/bin/python
# -​*- coding: utf-8 -*​-

from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cache import Cache

from modules.math import sum, sub
from modules.hello import hello_world
from modules.sql import get_data


app = Flask(__name__, static_url_path="")
cache = Cache(app)


@app.route('/math/<string:method>', methods=['GET'])
@cache.cached(timeout=60)
def do_math(method):
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if method == 'sum':
        return jsonify({'sum': sum(a, b)})
    elif method == 'sub':
        return jsonify({'sub': sub(a, b)})
    else:
        return jsonify({'error': 'No Method'})


@app.route('/sql', methods=['GET'])
@cache.cached(timeout=60)
def do_sql():
    return jsonify({'data': get_data().to_json(orient='index')})


@app.route('/hello', methods=['GET'])
@cache.cached(timeout=60)
def salute():
    return jsonify({'message': hello_world()})


if __name__ == '__main__':
    app.run(debug=True)