from sqlalchemy import text

import db_connect
import db_creation


class Category:

    def __init__(self):
        self.conn = db_connect.db_connection

    def add_category(self, category_name):

        # Fetch for value where category name exists
        category_check = text("SELECT * from category where category_name='" + category_name + "'")

        x = self.conn.execute(category_check).fetchall()

        # If category name already exists then return
        if len(x) != 0:
            print("Category exists")
            return x

        # Fetch the max category_id
        get_max_category_id = text("SELECT max(category_id) from category")

        max_category_id = self.conn.execute(get_max_category_id).fetchall()
        cur_category_id = str(max_category_id[0][0]+1)

        # Insert the category
        insert_category = db_creation.category.insert()
        insert_category.execute(category_id=cur_category_id, category_name=category_name)

        print("Category Added Successfully")


class Product:

    def __init__(self):
        self.conn = db_connect.db_connection

    def add_product(self, product_name, category_name, product_cost, product_detail):

        # Fetch for value where product name exists
        product_check = text("SELECT * from product where product_name='" + product_name + "'")

        x = self.conn.execute(product_check).fetchall()

        # If product name already exists then return
        if x is True:
            print("Product exists")
            return

        # Fetch for value where category name exists
        category_check = text("SELECT category_id, category_name from category where category_name='" +
                              category_name + "'")

        category_check = self.conn.execute(category_check).fetchall()[0]

        # If category name does not exist then return
        if category_check is False:
            print("Category does not exist")
            return -1

        # Fetch the max product_id
        get_max_product_id = text("SELECT max(product_id) from product")

        max_product_id = self.conn.execute(get_max_product_id).fetchall()[0][0]

        # Insert the product
        insert_product = db_creation.product.insert()
        insert_product.execute(product_id=(str(int(max_product_id) + 1)), product_name=product_name,
                               category_id=category_check[0], category_name=category_name, product_cost=product_cost,
                               product_detail=product_detail)


class Cart:

    def __init__(self):
        self.conn = db_connect.db_connection

    def view_cart_products(self):

        # Fetch all cart products of user
        cart_products = text("SELECT username, product_name from cart")
        cart_products = self.conn.execute(cart_products).fetchall()

        return cart_products

    def view_user_bills(self):

        # Fetch all bills of user
        username_check = text("SELECT * from bill")
        username_check = self.conn.execute(username_check).fetchall()

        return username_check
