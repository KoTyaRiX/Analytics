import json
import random
from flask import Flask, request
from flask_cors import CORS, cross_origin

from models.Column import Column

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

months = ["Jan", "Feb", "Mar", "Apl", "May", "Jan", "Jul", "Aut", "Sep", "Oct", "Nov", "Dec"]


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


@app.route('/filter', methods=['GET'])
@cross_origin()
def filter_table():
    # send args to parser server

    category = request.args.get('category')
    region = request.args.get('region')
    filed = request.args.get('filed')
    duration = request.args.get('timeDuration')

    n = 10  # creating for about a million points is too slow

    points = list(map(lambda x: x.to_json(), generate_random_columns(n,
                                                                     ["price", "count"],
                                                                     [10000, 1000]
                                                                     )
                      )
                  )
    return json.dumps(json.dumps(points))  # to make `{ json.dumps(...) }`


def generate_random_columns(n: int, names: list[str], max_values: list[int]):
    return [Column(months[i % 12],
                   {names[j]: random.randint(0, max_values[j]) for j in range(len(names))})
            for i in range(n)]


if __name__ == '__main__':
    app.run()
