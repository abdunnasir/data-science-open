"""
    API to get predicted and real incomes.

    Copyright (C) 2019  Abdunnasir.K.P <abdunnasirkp@gmail.com>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
# Importing the libraries
import numpy as np
from sklearn.externals import joblib
from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import json
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
api = Api(app)
CORS(app)

# Sample api call
# curl -X POST -d "total=2.3&lead=0&manager=0&cert=0"  http://127.0.0.1:5000

class LinearRegressionAPI(Resource):
    def post(self):
        try:
            regressor = joblib.load('model.pkl')
            total = float(request.values.get('total'))
            lead = float(request.values.get('lead'))
            manager = float(request.values.get('manager'))
            cert = float(request.values.get('cert'))
            pred_salary = regressor.predict([[total, lead,manager, cert]])

            # just a single answer, so take 0th element from the list
            response = jsonify({
                "predicted" : pred_salary.tolist()[0]
            })
            return response
        except Exception as e:
            data = {}
            data['message'] = str(e)
            json_data = json.dumps(data)
            # TODO: log the error
            return json_data, 500

api.add_resource(LinearRegressionAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)
