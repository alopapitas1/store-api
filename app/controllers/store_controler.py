from flask import Blueprint, jsonify,request
from app.models.store_model import Store
from app.ultis.decorator import jwt_required, roles_required
from app.views.store_view import render_store_detail,render_store_list

store_bp=Blueprint("store",__name__)


@store_bp.route("/products",methods=["GET"])
@jwt_required
@roles_required(roles=["admin","user"])
def get_stores():
    stores=Store.get_all()
    return jsonify(render_store_list(stores))

@store_bp.route("/products/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_Store(id):
    Stores = Store.get_by_id(id)
    if Stores:
        return jsonify(render_store_detail(Stores))
    return jsonify({"error": "Store no encontrado"}), 404


@store_bp.route("/products", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_Store():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock=data.get("stock")

    if name is None or description is None or price is None or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    Stores = Store(name=name, description=description, price=float(price),stock=stock)
    Store.save()

    return jsonify(render_store_detail(Stores)), 201


@store_bp.route("/products/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_Store(id):
    Stores = Store.get_by_id(id)
    if not Stores:
        return jsonify({"error": "Store no encontrado"}), 404
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")

    Stores.update(name=name, description=description, price=price)

    return jsonify(render_store_detail(Stores))


@store_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_Store(id):
    Store = Store.get_by_id(id)

    if not Store:
        return jsonify({"error": "Store no encontrado"}), 404

    Store.delete()

    return "", 204
