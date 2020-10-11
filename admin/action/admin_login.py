from admin.action import admin_connection

conn = admin_connection.DBAccess()


def admin_login():

    login_attempts = 1
    print("Enter Admin Credentials")
    username = input("Enter username:")
    password = input("Enter password:")
    connect = conn.login(username, password)

    if connect is None:
        while login_attempts < 4:
            print("Enter Admin Credentials")
            username = input("Enter username:")
            password = input("Enter password:")
            connect = conn.login(username, password)

            if connect is not None:
                print("Welcome Admin")
                break
            else:
                print("Incorrect username/password")
                login_attempts += 1
                continue

    if login_attempts == 4:
        return

    return connect
