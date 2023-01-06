import csv
from flask import Flask, request, jsonify, Response
import json
from boto3.dynamodb.conditions import Key
from flask_cors import CORS

from datetime import datetime


app = Flask(__name__)  # creating the Flask class object
CORS(app)


@app.route('/')
def home():
    file = open('data.csv')
    type(file)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
            rows.append(row)
    print(rows)
    response = jsonify(data=rows)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8089)

    # app.run(debug = True)
