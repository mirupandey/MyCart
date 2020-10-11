from admin.action import admin_connection
from user import user_tasks
from user.action import connection


def test_view_product():
    category_id = 1
    user_product = user_tasks.Product()
    assert user_product.view_products(category_id) == [(1, 'Table', 1, 'Furniture', 5000, 'Office Table'),
                                                       (2, 'Chair', 1, 'Furniture', 1000, 'Office Chair')]


def test_view_category():
    user_category = user_tasks.Category()
    assert user_category.view_categories() == [(1, 'Furniture'), (2, 'Utensils')]


def test_view_product_details():
    product_id = 1
    user_product = user_tasks.Product()
    assert user_product.view_product_details(product_id) == (1, 'Table', 'Office Table')


def test_user_login():
    username = 'aayushi'
    password = 'aayu123'
    user_access = connection.DBAccess()
    assert user_access.login(username, password) == [('aayushi', 'aayu123', 'Aayushi', 'Priya',
                                                      'Female', 9887908868)]


def test_admin_login():
    username = 'admin'
    password = 'admin123'
    admin_access = admin_connection.DBAccess()
    assert admin_access.login(username, password) == [('admin', 'admin123')]


test_view_product()
test_view_category()
test_view_product_details()
test_user_login()
test_admin_login()