import pymysql
import bcrypt
import uuid

import time, datetime


from config import host, username, password, db


current_data = datetime.datetime.now()
joindata = time.mktime(current_data.timetuple())

salt = bcrypt.gensalt()

uid = uuid.uuid4()

try:
    connection = pymysql.connect(
        host=host,
        user=username,
        password=password,
        database=db,
        cursorclass=pymysql.cursors.DictCursor
        )
except Exception as ex:
    print(str(ex))

def reg(email,password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    with connection.cursor() as cursor:
        try:
            insert_query = "INSERT INTO `user` (email,password,joindate) VALUES (%s,%s,%s)"
            cursor.execute(insert_query,(email,hashed_password,joindata))
            connection.commit()
            return True
        except Exception as ex:
            print(f"Error:{ex}")
            return False

def exist_email(email):
    try:
        with connection.cursor() as cursor:
            # Check if the email exists in the 'user' table
            query = "SELECT * FROM user WHERE email = %s"
            cursor.execute(query, (email))
            result = cursor.fetchone()

            # If the result is not None, the email exists
            if result:
                return True
            else:
                return False

    except Exception as ex:
        print(str(ex))

def log(email,password):
    try:
        with connection.cursor() as cursor:
            # Check if the email exists in the 'user' table
            query = "SELECT password FROM user WHERE email = %s"
            cursor.execute(query, (email))
            result = cursor.fetchone()
            if result:
                stored_hashed_password = result['password'].encode('utf-8')
                user_input_password = password.encode('utf-8')

                # Check with using bcrypt
                if bcrypt.checkpw(user_input_password, stored_hashed_password):
                    return True
                else:
                    return False
            else:
                    # Handle the case where the email doesn't exist
                return False

    except Exception as ex:
        print(str(ex))

def add_articles(name,about,price,image,creator):
    image.save('static/photo/' + str(uid)+'.png')
    with connection.cursor() as cursor:
        try:
            insert_query = "INSERT INTO `article` (name,uuid,about,price,creator,createdate) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query,(name,uid,about,price,creator,joindata))
            connection.commit()
            return True
        except Exception as ex:
            print(f"Error:{ex}")
            return False
        
def get_user_articles(email):
    try:
        with connection.cursor() as cursor:
            # Check if the email exists in the 'user' table
            query = "SELECT * FROM `article` WHERE creator = %s "
            cursor.execute(query, (email))
            result = cursor.fetchall()

            return result

    except Exception as ex:
        print(str(ex))

def get_article(uuid):
    try:
        with connection.cursor() as cursor:
            
            query = "SELECT * FROM `article` WHERE uuid = %s "
            cursor.execute(query, (uuid))
            result = cursor.fetchone()
            return result

    except Exception as ex:
        print(str(ex))

def get_all_articels():
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article`"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as ex:
        print(str(ex))
        
def get_articles_by_name(name):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM `article` WHERE name LIKE %s"
            cursor.execute(query,('%' + name + '%'))
            result = cursor.fetchall()
            return result
    except Exception as ex:
        print(str(ex))

