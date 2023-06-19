# models/manufacturer.py
# Model class for representing a manufacturer

class Manufacturer:
    def __init__(self, name, country, website, contact_person, email, phone_number, address, id=None):
        self.name = name
        self.country = country
        self.website = website
        self.contact_person = contact_person
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.id = id



