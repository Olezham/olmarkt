import pymysql
import bcrypt
import uuid

import time, datetime
import os

from config import host, username, password, db

current_data = datetime.datetime.now()
joindata = time.mktime(current_data.timetuple())
salt = bcrypt.gensalt()


def establish_connection():
    connection = pymysql.connect(
        host=host,
        user=username,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def generate_uid():
    return str(uuid.uuid4())

def reg(email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `user` (email,password,joindate) VALUES (%s,%s,%s)"
            cursor.execute(insert_query, (email, hashed_password, joindata))
            connection.commit()
            return True

def exist_email(email):
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM user WHERE email = %s"
            cursor.execute(query, (email))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False

def log(email, password):
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT password FROM user WHERE email = %s"
            cursor.execute(query, (email))
            result = cursor.fetchone()
            if result:
                stored_hashed_password = result['password'].encode('utf-8')
                user_input_password = password.encode('utf-8')
                if bcrypt.checkpw(user_input_password, stored_hashed_password):
                    return True
                else:
                    return False
            else:
                return False


def add_articles(name,about,price,image,creator):
    uid = generate_uid()
    image.save('olmarkt/static/photo/' + str(uid)+'.png')
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `article` (name,uuid,about,price,creator,createdate) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query,(name,uid,about,price,creator,joindata))
            connection.commit()
            return True


def get_user_articles(email):
    connection = establish_connection()

    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article` WHERE creator = %s "
            cursor.execute(query, (email))
            result = cursor.fetchall()
            return result


def get_article(uuid):
    connection = establish_connection()

    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article` WHERE uuid = %s "
            cursor.execute(query, (uuid))
            result = cursor.fetchone()
            return result

def get_all_articels():
    connection = establish_connection()

    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article`"
            cursor.execute(query)
            result = cursor.fetchall()
            return result

def get_articles_by_name(name):
    connection = establish_connection()

    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article` WHERE name LIKE %s"
            cursor.execute(query,('%' + name + '%'))
            result = cursor.fetchall()
            return result

def get_owner(uuid):
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT creator FROM `article` WHERE uuid = %s"
            cursor.execute(query,(uuid))
            result = cursor.fetchone()
            return result

def del_article(uuid):
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            query = "DELETE FROM article WHERE uuid = %s"
            cursor.execute(query,(uuid))
            connection.commit()
    os.remove('olmarkt/static/photo/' + uuid +'.png')