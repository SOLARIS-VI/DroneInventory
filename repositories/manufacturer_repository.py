# repositories/manufacturer_repository.py
# Repository for handling database operations related to manufacturers

from db.run_sql import run_sql
from models.manufacturer import Manufacturer

# Save a manufacturer to the database
def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, country, website, contact_person, email, phone_number, address) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [manufacturer.name, 
              manufacturer.country, 
              manufacturer.website, 
              manufacturer.contact_person, 
              manufacturer.email, 
              manufacturer.phone_number,
              manufacturer.address
    ]
    
    results = run_sql(sql, values)
    manufacturer.id = results[0]["id"]
    return manufacturer


# Retrieve all manufacturers from the database
def select_all():
    manufacturers = []
    sql = "SELECT * FROM manufacturers ORDER BY name"
    results = run_sql(sql)
    for row in results:
        manufacturer = Manufacturer(
            row["name"], 
            row["country"], 
            row["website"], 
            row["contact_person"], 
            row["email"], 
            row["phone_number"], 
            row["address"], 
            row["id"]
        )
        manufacturers.append(manufacturer)
    return manufacturers


# Retrieve a specific manufacturer by ID from the database
def select(id):
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result:
        row = result[0]
        manufacturer = Manufacturer(
            row["name"], 
            row["country"], 
            row["website"], 
            row["contact_person"], 
            row["email"], 
            row["phone_number"], 
            row["address"], 
            row["id"]
        )
        return manufacturer


# Delete all manufacturers from the database
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)


# Delete a specific manufacturer by ID from the database
def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# Save a manufacturer to the database, checking for duplicates
def save_manufacturer(manufacturer):
    existing_manufacturer = select(manufacturer.id)
    if existing_manufacturer:
        # Manufacturer with the same name already exists
        return existing_manufacturer
    
    return save(manufacturer)











