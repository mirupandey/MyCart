from sqlalchemy.sql import text

import db_connect
import db_creation


class DBAccess:

    def __init__(self):
        self.is_connect = False
        self.db_connection = None

    def login(self, username, password):

        try:
            self.db_connection = db_connect.db_connection
            self.is_connect = True

        # If connection is not successful
        except():
            print("Can't connect to database")
            return 0
            # If Connection Is Successful
        print("Connected")

        # Log In the User
        login_check = text("SELECT * from user_login where user_login.username='" + username +
                           "' and user_login.password='" + password + "'")

        login_check = self.db_connection.execute(login_check).fetchall()

        # If data exists then login
        return login_check

    def sign_up(self, username, password, first_name, last_name, gender, mobile_no):

        try:
            self.db_connection = db_creation.engine.connect()
            self.is_connect = True

        # If connection is not successful
        except():
            print("Can't connect to database")
            return 0

        # If Connection Is Successful
        print("Connected")

        # Checking if username exists
        login_check = text("SELECT * from user_login where username='" + username + "' and password='" + password + "'")

        login_check = self.db_connection.execute(login_check).fetchall()

        if len(login_check) != 0:
            print("Username already exists.")
            return 0

        # Create new user
        create_user = db_creation.user_login.insert()
        create_user.execute(username=username, password=password, first_name=first_name, last_name=last_name,
                            gender=gender, mobile_no=mobile_no)

        # Log In the User
        login_check = text("SELECT * from user_login where username='" + username + "' and password='" + password + "'")

        login_check = self.db_connection.execute(login_check).fetchall()

        # If data exists then login
        return login_check
