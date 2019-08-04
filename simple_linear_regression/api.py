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

app = Flask(__name__)
api = Api(app)
CORS(app)

# Sample api call
#  curl -X POST http://127.0.0.1:5000

class LinearRegressionAPI(Resource):
    def post(self):
        try:

            lr = joblib.load('model.pkl')
            dataset = joblib.load('dataset.pkl')

            # Get the years in 1D format
            years_list = dataset['Years'].tolist()

            # Convert 1D to 2D
            years = list(np.reshape(years_list, (-1, 1)))
            # Get the predicted salaries uisng simple linear regression
            salaries = lr.predict(years)

            index = 0
            predicted = []
            real = []

            for year in years_list:
                predicted.append(
                    {
                        "x": year,
                        "y": salaries[index]
                    }
                )
                real.append(
                    {
                        "x": year,
                        # Get the salary of a year using index of the year.
                        "y": dataset.loc[index, 'Income']
                    }
                )
                index = index + 1
                # End of for loop

            response = jsonify({
                "predicted" : predicted,
                "real" : real
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
