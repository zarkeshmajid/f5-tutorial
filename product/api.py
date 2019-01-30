# Product Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api
import redis

# Instantiate the app
app = Flask(__name__)
api = Api(app)
redis = redis(host='redis', port=6379)


class Product(Resource):
    def get(self):
        return {
            'products': ['Majid', 'John', 'David', 'Emily']
        }


# Create routes
api.add_resource(Product, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
