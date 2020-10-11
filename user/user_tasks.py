from sqlalchemy import text

import db_connect
import db_creation


class Category:

    def __init__(self):
        self.conn = db_connect.db_connection

    def view_categories(self):

        # Fetch for value where category name exists
        category_check = text("SELECT * from category")

        category_check = self.conn.execute(category_check).fetchall()

        return category_check


class Product:

    def __init__(self):
        self.conn = db_connect.db_connection

    def view_products(self, category_id):

        # Fetch for value where product name exists
        product_check = text("SELECT * from product where category_id='" + str(category_id) + "'")

        product_check = self.conn.execute(product_check).fetchall()

        return product_check

    def view_product_details(self, product_id):

        # Fetch for value where product name exists
        product_check = text("SELECT product_id, product_name, product_detail from product where product_id='"
                             + str(product_id) + "'")

        product_check = self.conn.execute(product_check).fetchall()[0]

        return product_check


class Cart:

    def __init__(self):
        self.conn = db_connect.db_connection

    def view_products_cart(self, username):

        # Search product
        search_products = text("SELECT * from cart where username='" + username + "'")

        search_products = self.conn.execute(search_products).fetchall()

        return search_products

    def add_products_cart(self, product_id, username):

        # Search product
        search_product = text("SELECT product_name, category_id, category_name, product_cost from product "
                              "where product_id=" + str(product_id))

        search_product = self.conn.execute(search_product).fetchall()

        # Add product to cart
        add_cart_product = db_creation.cart.insert()
        add_cart_product.execute(username=username, product_id=product_id, product_name=search_product[0][0],
                                 category_id=search_product[0][1], category_name=search_product[0][2],
                                 cost=search_product[0][3])

    def buy_products(self, username):

        # Find if cart table has value
        cart_not_empty = text("SELECT * from cart where username='" + username[0] + "'")

        cart_not_empty = self.conn.execute(cart_not_empty).fetchall()

        # Check if cart is empty or not
        if len(cart_not_empty) == 0:
            print("Nothing in Cart")
            return

        # Check total cost of Cart Items
        sum_cost = text("SELECT sum(cost) from cart where username='" + username[0] + "'")

        sum_cost = self.conn.execute(sum_cost).fetchall()[0][0]

        # Find if bill table has value
        bill_present = text("SELECT * from bill where username='" + username[0] + "' and rowid<2")

        bill_present = self.conn.execute(bill_present).fetchall()

        # Check if bill is present or not
        if len(bill_present) != 0:

            # Find last update bill_id
            max_bill_id = text("SELECT max(bill_id) from bill")

            max_bill_id = self.conn.execute(max_bill_id).fetchall()[0]
            max_bill_id = max_bill_id[0][0]

        else:

            max_bill_id = 0

        # Discount Calculation
        discount_amount = 0

        if sum_cost > 10000:
            discount_amount = 500

        # Final Amount Calculation
        final_amount = sum_cost - discount_amount
        cur_bill_id = int(max_bill_id) + 1

        # Buy product from cart, add to bill
        add_bill = db_creation.bill.insert()
        add_bill.execute(username=username[0], bill_id=cur_bill_id, actual_amount=sum_cost,
                         discount_amount=discount_amount, final_amount=final_amount)

        # Remove products from cart
        delete_from_cart = db_creation.cart.delete()
        delete_from_cart.execute()

        # Save the changes in the database
        return_bill = text("SELECT * from bill where bill_id=" + str(cur_bill_id))

        return_bill = self.conn.execute(return_bill).fetchall()

        return return_bill[0]

    def remove_cart_products(self, username, product_id):

        # Delete Product
        delete_from_cart = db_creation.cart.delete()

        # Save the changes in the database
        delete_from_cart.execute(username=username, product_id=product_id)
