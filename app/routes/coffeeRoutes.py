from flask import Blueprint, request, jsonify

from app.controllers.coffeeControllers import *

api_blueprint = Blueprint('/coffees', __name__)

@api_blueprint.route("/coffee/<int:coffee_id>", methods=["GET"])
def get_coffees_by_id_route(coffee_id):
    coffee = get_coffee_by_id(coffee_id)
    print("coffee di routes : ",coffee)
    if coffee:
        return coffee,200
    if coffee==None:
        return jsonify({"error" : "coffee not found"}),400
    else:
        return jsonify({"error" : "error fetching coffee"}), 500

@api_blueprint.route("/coffees/", methods=["GET"])
def get_coffees_route():
    coffees = get_all_coffees()
    if len(coffees)==0:
        return jsonify({"error" : "no coffee is available"})
    return jsonify(coffees),200

@api_blueprint.route("/coffees/add",methods=["POST"])
def create_coffee_route():
    data = request.get_json()
    if not data or 'nama' not in data or 'harga' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_coffee = create_coffee(data)
    return jsonify(new_coffee),200

@api_blueprint.route("/coffee/edit/<int:coffee_id>",methods=["PUT"])
def update_coffee_route(coffee_id):
    data = request.get_json()
    updated_coffee = update_coffee(coffee_id,data)
    if updated_coffee:
        return jsonify(updated_coffee),200
    return jsonify({"error" : "error updating coffee"}),404

@api_blueprint.route("/coffee/delete/<int:coffee_id>",methods=["DELETE"])
def delete_coffee_route(coffee_id):
    deleted_coffee = delete_coffee(coffee_id)
    if deleted_coffee:
        return jsonify({"message" : "coffee sucessfully deleted"}),200
    return jsonify({"error" : "error deleting coffee"}),404