#! usr/bin/python3

# *** creating tables: SQL-foramt ***

# sales table
sales_table = '''CREATE TABLE sales (
                sales_id INTERGER PRIMARY KEY,
                sales_data DATE,
                customer_id INTEGER,
                product_id INTERGER,
                quantity INTEGER,
                )'''