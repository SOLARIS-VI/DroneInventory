# repositories/product_repository.py
# Repository for handling database operations related to products

from db.run_sql import run_sql
from models.product import Product
from repositories.manufacturer_repository import select as select_manufacturer


# Save a product to the database
def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [
        product.name,
        product.description,
        product.stock_quantity,
        product.buying_cost,
        product.selling_price,
        product.manufacturer.id,
    ]
    results = run_sql(sql, values)
    product.id = results[0]["id"]
    return product


# Retrieve all products from the database
def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for row in results:
        manufacturer = select_manufacturer(row["manufacturer_id"])
        product = Product(
            row["name"],
            row["description"],
            row["stock_quantity"],
            row["buying_cost"],
            row["selling_price"],
            manufacturer,
            row["id"],
        )
        products.append(product)
    return products


# Retrieve a specific product by ID from the database
def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        row = result[0]
        manufacturer = select_manufacturer(row["manufacturer_id"])
        product = Product(
            row["name"],
            row["description"],
            row["stock_quantity"],
            row["buying_cost"],
            row["selling_price"],
            manufacturer,
            row["id"],
        )
        return product


# Update a product in the database
def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [
        product.name,
        product.description,
        product.stock_quantity,
        product.buying_cost,
        product.selling_price,
        product.manufacturer.id,
        product.id,
    ]
    run_sql(sql, values)


# Delete a product from the database
def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Delete all products
def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)






