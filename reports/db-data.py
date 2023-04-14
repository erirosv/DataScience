#! usr/bin/python3

# *** Libraries ***
import sqlite3
import datetime
import random

# *** creating tables: SQL-foramt ***
# This is the same as rrunning an SQL script in
# the DB. It is simpler to do I all from one 
# language...

# sales table
sales_table = '''CREATE TABLE sales (
                sales_id INTERGER PRIMARY KEY,
                sales_date DATE,
                quantity INTEGER,
                cost_per_unit DECIMAL,
                total_price DECIMAL,
                customer_id INTEGER,
                product_id INTERGER,
                FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
                FOREIGN KEY (product_id) REFERENCES customer(product_id),
                )'''

# customers table
customers_table = '''CREATE TABLE customers(
                    customer_id INTERGER PRIMARY KEY,
                    first_name VARCHAR,
                    last_name VARCHAR,
                    email VARCHAR,
                    phone VARCHAR
                    )'''

# sales table
products_table = '''CREATE TABLE products(
                    product_id INTERGER PRIMARY KEY,
                    product_name VARCHAR,
                    cost_per_unit DECIMAL
                    )'''

# *** Methods *** 

# load dummy data
def load_dummy_data():
    '''
    This order you add the data is the default way the data will
    be shown in the DB-schema. 

    This is a blueprint forr adding äny type of data

    PRIMARY KEY is not included in this process.
    '''
    sales_data = '''INSERT INTO sales (customer_id, sales_date, product_id, cost_per_unit, quantity, total_price)
                    VALUES (?,?,?,?,?,?)'''
    customer_data = 'INSERT INTO customers (email, first_name, last_name, phone) VALUES (?,?)'
    product_data = 'INSERT INTO '