# controllers/drone_controller.py
# Controller for handling drone-related routes and requests

from flask import render_template, request, redirect, Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository


drone_blueprint = Blueprint("drone", __name__)


# Route to display the inventory page
@drone_blueprint.route("/inventory")
def inventory():
    products = product_repository.select_all()
    return render_template("inventory/index.html", products=products)


# Route to display the form for adding a new product
@drone_blueprint.route("/inventory/new", methods=["GET"])
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/new.html", manufacturers=manufacturers)


# Route to handle the creation of a new product
@drone_blueprint.route("/inventory", methods=["POST"])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = int(request.form["stock_quantity"])
    buying_cost = float(request.form["buying_cost"])
    selling_price = float(request.form["selling_price"])
    manufacturer_id = int(request.form["manufacturer_id"])
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer)
    product_repository.save(product)
    return redirect("/inventory")


# Route to display the details of a specific product
@drone_blueprint.route("/inventory/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select(id)
    return render_template("inventory/show.html", product=product)


# Route to display the form for editing a product
@drone_blueprint.route("/inventory/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/edit.html", product=product, manufacturers=manufacturers)


# Route to handle the update of a product
@drone_blueprint.route("/inventory/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = int(request.form["stock_quantity"])
    buying_cost = float(request.form["buying_cost"])
    selling_price = float(request.form["selling_price"])
    manufacturer_id = int(request.form["manufacturer_id"])
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer, id)
    product_repository.update(product)
    return redirect("/inventory")


# Route to handle the deletion of a product
@drone_blueprint.route("/inventory/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/inventory")

