from flask import Flask
from flask_restful import Api
from resources.hotels import * # importing class Hoteis from resources/hotels.py


app = Flask(__name__)
api = Api(app)

# O REST API criado será com base em um hotel

# Adding the path which will be used to consult in postman

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')


# This code for run my app variable with debug function
if __name__ == '__main__':
    app.run(debug=True)
