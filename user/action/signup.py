from user.action import connection

# SQL command to insert the data in the table
username = input("Enter username:")
pswd = input("Enter password:")
first_name = input("Enter First Name:")
last_name = input("Enter Last Name:")
gender = input("Enter Gender:")
mobile_no = input("Enter Mobile No:")

conn = connection.DBAccess.getConnection(username, pswd)

print("Welcome ", conn.first_name)