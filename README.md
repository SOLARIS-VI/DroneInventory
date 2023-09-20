# Drone Inventory Management System

The **Drone Inventory Management System** is a powerful tool designed specifically for drone shop administrators to efficiently and effectively manage their stock inventory. Unlike customer-facing applications, this system is tailored exclusively for internal use by shop workers, providing them with a comprehensive suite of features to streamline inventory tracking and management.

## Key Features

### Product Inventory Management

Our system enables the meticulous tracking of individual products within your inventory. Each product is managed with the following details:

- **Name:** Easily identify and search for products by name.
- **Description:** Provide detailed information about each product to ensure accurate inventory management.
- **Stock Quantity:** Keep a real-time record of the quantity of each product in stock.
- **Buying Cost:** Track the cost at which each product is purchased.
- **Selling Price:** Set and adjust selling prices to optimize your business's profitability.

### Manufacturer Management

Effortlessly manage the manufacturers of your drone products, facilitating efficient communication and coordination. Manufacturer details include:

- **Name:** Keep a comprehensive list of manufacturers for your products.
- **Country Location:** Track the geographical location of each manufacturer.
- **Contact Details:** Store essential contact information for manufacturers to enhance communication and collaboration.

### Streamlined Data Entry and Editing

Our system simplifies the process of creating and editing both manufacturers and products. Whether you need to add a new manufacturer or update product details, our intuitive interface ensures a seamless experience.

## Technologies Used

- **Python 3:** The core programming language used to develop this system, providing robust and flexible functionality.
- **PostgreSQL:** A powerful open-source relational database management system for storing and managing your inventory data.
- **CRUD Operations:** Utilizing Create, Read, Update, and Delete operations to manipulate data, ensuring complete control over your inventory.
- **Flask:** A micro web framework in Python that facilitates the creation of a user-friendly and responsive web interface for the system.

## How to Run the Project

To run the **Drone Inventory Management System** on your local machine, follow these steps:

## Step 1
Clone the Repository:
git clone https://github.com/your-username/drone-inventory.git

## Step 2
Navigate to the Project Directory:
cd DroneInventory

## Step 3
Install Dependencies:
pip install -r requirements.txt

## Step 4
Set Up the Database:
Create a PostgreSQL database for the project.
Update the database configuration in the project settings to connect to your database.

## Step 5
Initialize the Database:
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

## Step 6
Run the Application:
python3 app.py

## Step 7
Access the Application:

Select the command key on mac or ctrl+L, then hover and select with mouse cursor the local host that should be running on: http://127.0.0.1:5000

With these steps completed, you will have the Drone Inventory Management System up and running on your local machine. 








