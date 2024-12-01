from flask import Blueprint, request, jsonify

from app.controllers.coffeeControllers import(get_all_coffees,create_coffee)

api_blueprint = Blueprint('/coffees', __name__)

@api_blueprint.route("/coffees/", methods=["GET"])
def get_coffees_route():
    coffees = get_all_coffees()
    return jsonify(coffees),200

@api_blueprint.route("/coffees/add",methods=["POST"])
def create_coffee_route():
    data = request.get_json()
    if not data or 'nama' not in data or 'harga' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_coffee = create_coffee(data)
    return jsonify(new_coffee),200