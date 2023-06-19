# console.py
# Code for populating the database with initial data

import pdb
from models.manufacturer import Manufacturer
from models.product import Product
from repositories.manufacturer_repository import save as save_manufacturer
from repositories.product_repository import save as save_product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


# Create and save manufacturer objects
manufacturer1 = Manufacturer(
    "DJI", 
    "China", 
    "https://www.dji.com/", 
    "Mark Walberg", 
    "mark.walberg@dji.com", 
    "0234567890", 
    "123 Main Street, Beijing")

save_manufacturer(manufacturer1)

manufacturer2 = Manufacturer(
    "Autel Robotics", 
    "USA", 
    "https://www.autelrobotics.com/", 
    "Margot Robbie", 
    "margot.robbie@autel.com", 
    "9876543210", 
    "456 Elm Avenue, Los Angeles")

save_manufacturer(manufacturer2)

manufacturer3 = Manufacturer(
    "Parrot", 
    "France", 
    "https://www.parrot.com/", 
    "Robert Downey Junior", 
    "robert.downey.junior@parrot.com", 
    "05757585555", 
    "789 Oak Lane, Paris")

save_manufacturer(manufacturer3)

manufacturer4 = Manufacturer(
    "Yuneec", 
    "China", 
    "https://www.yuneec.com/", 
    "Jet Li", "jet.li@yuneec.com", 
    "07772737477", 
    "567 Pine Street, Shanghai")

save_manufacturer(manufacturer4)


# Create and save product objects
product1 = Product(
    "DJI Mavic 2 Zoom",
    "Professional, powerful, portable drone",
    400,
    850.0,
    1500.0,
    manufacturer1)

save_product(product1)

product2 = Product(
    "DJI Phantom 4 Pro",
    "Advanced aerial camera drone",
    100,
    1200.0,
    2800.0,
    manufacturer1)

save_product(product2)

product3 = Product(
    "DJI Mini 2",
    "Compact lightweight drone",
    350,
    800.0,
    1200.0,
    manufacturer1)

save_product(product3)

product4 = Product(
    "Autel Robotics EVO II",
    "Versatile feature-packed drone",
    25,
    1000.0,
    2100.0,
    manufacturer2)

save_product(product4)

product5 = Product(
    "Parrot Anafi",
    "Innovative 4K HDR drone",
    10,
    700.0,
    1000.0,
    manufacturer3)

save_product(product5)

product6 = Product(
    "Yuneec Typhoon H Pro",
    "Stable reliable hexacopter drone",
    15,
    1200.0,
    1800.0,
    manufacturer4)

save_product(product6)

product7 = Product(
    "DJI Air 2S",
    "Powerful compact drone",
    200,
    999.0,
    1499.0,
    manufacturer1)

save_product(product7)

product8 = Product(
    "DJI FPV",
    "Immersive high-speed acrobatic drone",
    50,
    1299.0,
    1999.0,
    manufacturer1)

save_product(product8)

product9 = Product(
    "DJI Inspire 2",
    "Professional-grade filmmaker drone",
    80,
    2999.0,
    5999.0,
    manufacturer1)

save_product(product9)

product10 = Product(
    "DJI Matrice 300 RTK",
    "Industrial-grade AI drone",
    10,
    7499.0,
    10999.0,
    manufacturer1)

save_product(product10)

product11 = Product(
    "Autel Robotics EVO",
    "Compact foldable intelligent drone",
    100,
    899.0,
    1199.0,
    manufacturer2)

save_product(product11)

product12 = Product(
    "Autel Robotics EVO Lite",
    "Entry-level stable camera drone",
    150,
    499.0,
    799.0,
    manufacturer2)

save_product(product12)

product13 = Product(
    "DJI Phantom 5",
    "Flagship camera drone",
    0,
    2499.0,
    3499.0,
    manufacturer1)

save_product(product13)

product14 = Product(
    "DJI Ronin-S",
    "Handheld gimbal stabilizer",
    300,
    649.0,
    899.0,
    manufacturer1)

save_product(product14)

product15 = Product(
    "DJI Mavic Air 2",
    "Compact intelligent camera drone",
    300,
    799.0,
    1299.0,
    manufacturer1)

save_product(product15)

product16 = Product(
    "Autel Robotics EVO II Pro",
    "Professional 6K camera drone",
    50,
    1999.0,
    2499.0,
    manufacturer2)

save_product(product16)

product17 = Product(
    "Autel Robotics Dragonfish",
    "Underwater imaging drone",
    20,
    1499.0,
    1999.0,
    manufacturer2)

save_product(product17)

product18 = Product(
    "DJI Spark",
    "Mini intelligent camera drone",
    150,
    299.0,
    499.0,
    manufacturer1)

save_product(product18)

product19 = Product(
    "DJI Phantom 4",
    "Classic 4K camera drone",
    50,
    999.0,
    1399.0,
    manufacturer1)

save_product(product19)

product20 = Product(
    "DJI Agras T20",
    "Advanced crop spraying drone",
    5,
    15999.0,
    19999.0,
    manufacturer1)

save_product(product20)


pdb.set_trace()









