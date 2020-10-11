from sqlalchemy import Table, Column, Integer, DECIMAL, String, ForeignKey
from sqlalchemy.dialects import mysql


def create_tables_and_insert_dummy_data(meta, engine) -> None:
    """
        A method to create database tables and insert dummy datas
    :return: None
    """
    admin_login = Table(
        'admin_login', meta,
        Column('username', String, primary_key=True, nullable=False),
        Column('password', String, nullable=False)
    )

    user_login = Table(
        'user_login', meta,
        Column('username', String, primary_key=True, nullable=False),
        Column('password', String, nullable=False),
        Column('first_name', String, nullable=False),
        Column('last_name', String, nullable=False),
        Column('gender', String(1), nullable=False),
        Column('mobile_no', mysql.INTEGER(10), nullable=False, unique=True)
    )

    category = Table(
        'category', meta,
        Column('category_id', Integer, primary_key=True, nullable=False),
        Column('category_name', String, nullable=False)
    )

    product = Table(
        'product', meta,
        Column('product_id', Integer, primary_key=True, nullable=False),
        Column('product_name', String, nullable=False),
        Column('category_id', Integer, ForeignKey("category.category_id"), nullable=False),
        Column('category_name', String, ForeignKey("category.category_name"), nullable=False),
        Column('product_cost', DECIMAL, nullable=False),
        Column('product_detail', String, nullable=False)
    )

    cart = Table(
        'cart', meta,
        Column('username', String, ForeignKey("user_login.username"), primary_key=True, nullable=False),
        Column('product_id', Integer, ForeignKey("product.product_id"), nullable=False),
        Column('product_name', String, ForeignKey("product.product_name"), nullable=False),
        Column('category_id', Integer, ForeignKey("category.category_id"), nullable=False),
        Column('category_name', String, ForeignKey("category.category_name"), nullable=False),
        Column('cost', Integer, ForeignKey("product.product_cost"), nullable=False)
    )

    bill = Table(
        'bill', meta,
        Column('username', String, ForeignKey("user_login.username"), primary_key=False, nullable=False),
        Column('bill_id', String, nullable=False, unique=True),
        Column('actual_amount', Integer, nullable=False),
        Column('discount_amount', Integer, nullable=False),
        Column('final_amount', Integer, nullable=False)
    )

    meta.create_all(engine)

    admin_login_insert = admin_login.insert()
    admin_login_insert.execute(username='admin', password='admin123')

    user_login_insert = user_login.insert()
    user_login_insert.execute(username='miru', password='miru123', first_name='Mrinal',
                              last_name='Pandey', gender='Female', mobile_no='9784314332')

    user_login_insert = user_login.insert()
    user_login_insert.execute(username='aayushi', password='aayu123', first_name='Aayushi',
                              last_name='Priya', gender='Female', mobile_no='9887908868')

    category_insert = category.insert()
    category_insert.execute(category_id='1', category_name='Furniture')

    product_insert = product.insert()
    product_insert.execute(product_id='1', product_name='Table', category_id='1', category_name='Furniture',
                           product_cost='5000', product_detail='Office Table')

    product_insert = product.insert()
    product_insert.execute(product_id='2', product_name='Chair', category_id='1', category_name='Furniture',
                           product_cost='1000', product_detail='Office Chair')

    category_insert = category.insert()
    category_insert.execute(category_id='2', category_name='Utensils')

    product_insert = product.insert()
    product_insert.execute(product_id='3', product_name='Pan', category_id='2', category_name='Utensils',
                           product_cost='600', product_detail='Non Stick Pan')

    product_insert = product.insert()
    product_insert.execute(product_id='4', product_name='Knife', category_id='2', category_name='Utensils',
                           product_cost='60', product_detail='Sharpened Knife')
