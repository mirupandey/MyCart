from user.action import connection

# Establish Connection
conn = connection.DBAccess()


def user_login():

    # User Login
    login_attempts = 1
    print("Enter User Credentials")
    username = input("Enter username:")
    password = input("Enter password:")
    connect = conn.login(username, password)

    # If login attempt failed
    if len(connect) == 0:
        while login_attempts < 4:

            print("Enter User Credentials attempt ", login_attempts)
            username = input("Enter username:")
            password = input("Enter password:")
            connect = conn.login(username, password)

            if len(connect) != 0:
                print("Welcome")
                break
            else:
                print("Incorrect username/password")
                login_attempts += 1
                continue

    if login_attempts == 4:
        return

    return connect


def user_signup():

    # Sign Up
    login_attempts = 1
    print("Enter User Details")
    username = input("Enter username:")
    password = input("Enter password:")
    first_name = input("Enter First Name:")
    last_name = input("Enter Last Name:")
    gender = input("Enter Gender:")
    mobile_no = input("Enter Mobile No:")

    connect = conn.sign_up(username, password, first_name, last_name, gender, mobile_no)

    # If login attempt failed
    if len(connect) == 0:
        while login_attempts < 4:

            print("Enter User Credentials attempt ", login_attempts)
            username = input("Enter username:")
            password = input("Enter password:")
            first_name = input("Enter First Name:")
            last_name = input("Enter Last Name:")
            gender = input("Enter Gender:")
            mobile_no = input("Enter Mobile No:")

            connect = conn.sign_up(username, password, first_name, last_name, gender, mobile_no)

            # Connection successful
            if len(connect) != 0:
                print("Welcome")
                break
            else:
                print("Invalid Values")
                login_attempts += 1
                continue

    # Login attempts exhausted
    if login_attempts == 4:
        return

    return connect
