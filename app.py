from flask import Flask, render_template
from controllers.drone_controller import drone_blueprint
from repositories import manufacturer_repository

app = Flask(__name__)
app.register_blueprint(drone_blueprint)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/manufacturers')
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/manufacturers.html', manufacturers=manufacturers)

@app.route('/manufacturer/<int:manufacturer_id>')
def manufacturer(manufacturer_id):
    manufacturer = manufacturer_repository.select(manufacturer_id)
    return render_template('manufacturers/manufacturers_details.html', manufacturer=manufacturer)

if __name__ == "__main__":
    app.run(debug=True)
