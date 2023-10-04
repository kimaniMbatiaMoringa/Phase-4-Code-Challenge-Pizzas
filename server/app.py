from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)

db.init_app(app)

@app.route('/')
def index():
    return "This is the base, go to /items to see items"

@app.route('/restaurants')
def restuarnts():
    restaurantList =[]
    queryForItems = Restaurant.query.all()
    
    if not queryForItems:
        return 'No Restaurants in the table!'
    
    for item in Restaurant.query.all():
        restaurant_dict ={
            "name": item.name,
            "address": item.address
        }
        restaurantList.append(restaurant_dict)

    response = make_response(
        restaurantList,
        200
    )
    return response

@app.route('/restaurants/<int:id>')
def individual_restaurants():
    restuarant = Restaurant.query.filter(Restaurant.id==id).first()

    if not restuarant:
        error_object={
            "error":"Restaurant not found"
        }
        response = make_response(
            jsonify(error_object),
            200
        )
        return response

    restuarnt_object={
        "id": restuarant.id,
        "name":restuarant.name,
        "address": restuarant.address
    }

    response = make_response(
        jsonify(restuarnt_object),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response   


if __name__ == '__main__':
    app.run(port=6000, debug=True)
