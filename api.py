import json
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
from flask import request
from ScrapeCodechef import *

app = Flask(__name__)
api = Api(app)

@app.route('/codechef')
def data():
    # here we want to get the value of user (i.e. ?username=some-value)
    user = request.args.get('username')
    data = FindProfile(user)
    return json.loads(data)




if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app