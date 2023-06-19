-- Create manufacturers table
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  country VARCHAR(255),
  website VARCHAR(255),
  contact_person VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(255),
  address VARCHAR(255)
);


-- Create products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  stock_quantity INTEGER,
  buying_cost DECIMAL(10, 2),
  selling_price DECIMAL(10, 2),
  manufacturer_id INTEGER REFERENCES manufacturers(id) ON DELETE CASCADE
);


