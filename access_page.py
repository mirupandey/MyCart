import logging

from admin import admin_tasks
from admin.action import admin_login
from user import user_tasks
from user.action import login

condition = True

while condition:

    print("Welcome to MyCart")
    login_choice = input("Choose Login Type (1 or 2 or 3)\n1. Admin 2. User 3. Exit\n")

    # Admin Login
    if login_choice == '1':

        admin = admin_login.admin_login()

        # Loop till admin is connected
        while len(admin) != 0:

            # Admin to make choice
            admin_choice = input("Choose what to do\n1. Add Category & Products\n2. Add Products\n"
                                 "3. View Details of Product in Cart\n4. Bills Generated by all the Users\n5. Exit")

            # Admin to Add Category and Product
            if admin_choice == '1':

                category_name = str(input("Category to be added:"))
                admin_tasks.Category().add_category(category_name)

                print("Category Added")
                print("Add products to the category")
                product_check = True

                # Add product to the category
                while product_check:

                    product_name = str(input("Product to be added: "))
                    product_cost = int(input("Product Cost: "))
                    product_detail=input("Product Detail: ")
                    add_product = admin_tasks.Product().add_product(product_name, category_name, product_cost,
                                                                    product_detail)
                    product_check = input("Continue adding more products?(Y/N)")

                    # If product not to be added more into the category at the moment
                    if product_check == 'N':
                        product_check = False

                print("Category & Product(s) added successfully")

            # Add products
            elif admin_choice == '2':

                product_check = True
                while product_check:
                    category_name = input("Category in which product to be added ")
                    product_name = input("Product to be added ")
                    product_cost = input("Product Cost: ")
                    product_detail = input("Product Detail: ")
                    add_product = admin_tasks.Product().add_product(product_name, category_name, product_cost,
                                                                    product_detail)
                    product_check = input("Continue adding more products?(Y/N)")
                    print(product_check)

                    # If product not to be added more into the category at the moment
                    if product_check == 'N':
                        product_check = False

                print("Product(s) added successfully")

            # View Details of the Products in Cart
            elif admin_choice == '3':

                print("Cart Products:")
                cart_products = admin_tasks.Cart().view_cart_products()

                # Check if products are present in cart or not
                if len(cart_products) == 0:
                    print("No Product in Cart")

                else:

                    # Print products added in cart by various users
                    for values in cart_products:
                        print("Username: ", values[0], " Product: ", values[2])

            # View Bills generated by various users
            elif admin_choice == '4':

                print("Bills Generated:")
                bills_generated = admin_tasks.Cart().view_user_bills()

                # Check if bill(s) are present for user(s) or not
                if len(bills_generated) == 0:
                    print("No Bills Generated till Now")

                else:

                    # Print bills of various users
                    for values in bills_generated:
                        print("Username: ", values[0], " Actual Bill: ", values[2], " Discount: ", values[3],
                              "Final Bill: ", values[4])

            # Disconnect Admin
            elif admin_choice == '5':

                print("Disconnect Admin")

                admin = None
                break

            # Invalid Option
            else:
                print("Invalid Choice")

    # User Login
    elif login_choice == '2':

        choose_log_type = input("Choose what to do\n1. Login\n2.Sign Up\n3.Exit\n")

        # Login
        if choose_log_type == '1':
            user = login.user_login()

        # Sign Up
        elif choose_log_type == '2':
            user = login.user_signup()

        # Disconnect
        elif choose_log_type == '3':
            condition = False
            print("Bye Bye")
            break

        else:
            print("Invalid Choice")
            break

        # Loop till user is connected
        while len(user) != 0:

            user_choice = input("Choose what to do\n1. View Categories\n2. View Cart Products\n3. Exit")

            # View various categories
            if user_choice == '1':

                categories = user_tasks.Category().view_categories()

                # Check if category is present or not
                if len(categories) != 0:

                    for values in categories:
                        print("Category ID: ", values[0], " Category: ", values[1])

                    category_product_view = input("Choose what to do\n1. View Products in a Category\n2. Exit")

                    # View Products Category
                    if category_product_view == '1':

                        category_id = int(input("Enter Category ID:"))
                        category_products = user_tasks.Product().view_products(category_id)

                        # Check if category has products or not
                        if len(category_products) != 0:

                            for values in category_products:
                                print("Product ID: ", values[0], " Product Name: ", values[1])

                            product_action = input("Choose what to do\n1. View Products Details"
                                                   "\n2. Add Product to Cart\n3. Exit")

                            # View Product Details
                            if product_action == '1':

                                product_id = int(input("Enter Product ID:"))
                                products = user_tasks.Product().view_product_details(product_id)

                                # Check if product details present or not
                                if len(products) != 0:

                                    print("Product ID: ", str(products[0]), " Product Name: ", products[1],
                                          " Product Details: ", products[2])

                                    product_detail_action = input("Choose what to do\n1. Add Product to Cart\n2. Exit")

                                    # Add Product to Cart
                                    if product_detail_action == '1':

                                        product_id = int(input("Enter Product ID:"))
                                        products = user_tasks.Cart().add_products_cart(product_id, user[0][0])

                                        print("Product Added Successfully")

                                    # Exit
                                    elif product_detail_action == '2':
                                        condition = False
                                        print("Bye Bye")
                                        break

                                    # Invalid Option
                                    else:
                                        print("Invalid Option")
                                        break

                            # Add Product to Cart
                            elif product_action == '2':

                                product_id = int(input("Enter Product ID:"))
                                user_tasks.Cart().add_products_cart(product_id, user[0][0])

                                print("Product Added Successfully")

                            # Exit
                            elif product_action == '3':
                                condition = False
                                print("Bye Bye")
                                break

                            # Invalid Option
                            else:
                                print("Invalid Option")
                                break

                        else:
                            print("Category does not exist")

                    # Exit
                    elif category_product_view == '2':
                        condition = False
                        print("Bye Bye")
                        break

                    else:
                        print("Invalid Option")

                else:
                    print("Invalid Choice")

            # View Cart Products
            elif user_choice == '2':

                cart_products = user_tasks.Cart().view_products_cart(user[0][0])

                # Check if cart has products
                if len(cart_products) != 0:

                    for values in cart_products:
                        print("Product ID: ", str(values[1]), " Product Name: ", values[2], " Cost: ", str(values[5]))

                    cart_product_action = input("Choose what to do\n1. Buy Cart Products\n2. Remove Cart Product"
                                                "\n3. Exit")

                    # Buy Cart Products
                    if cart_product_action == '1':

                        bill = user_tasks.Cart().buy_products(user[0])
                        print("Bill: ", bill)

                        # Check if bill present or not
                        if len(bill) != 0:
                            print("Bill\nBill ID: ", str(bill[1]), " Actual Amount: ", str(bill[2]),
                                  " Discounted Amount: ", str(bill[3]), " Final Amount: ", str(bill[4]))

                    # Remove Cart Products
                    elif cart_product_action == '2':

                        product_id = int(input("Enter Product ID:"))
                        products = user_tasks.Cart().remove_cart_products(user[0], product_id)

                        print("Product Removed Successfully")

                    # Exit
                    elif cart_product_action == '3':
                        condition = False
                        print("Bye Bye")
                        break

                    # Invalid Choice
                    else:
                        print("Invalid Choice")

            # Disconnect User
            elif user_choice == '3':

                print("Disconnect User")
                break

            # Invalid Choice
            else:
                print("Invalid Choice")

    # Exit
    elif login_choice == '3':

        condition = False
        print("Bye Bye")
        break

    # Invalid Option
    else:
        print("Invalid Option")