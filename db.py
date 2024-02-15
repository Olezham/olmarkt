from mysql import establish_connection
import subprocess
import sys, os


def create_tables():
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
            create_table_article = """
                CREATE TABLE IF NOT EXISTS article (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(45) NOT NULL,
                    uuid VARCHAR(45) NOT NULL,
                    about VARCHAR(256) NOT NULL,
                    price VARCHAR(45) NOT NULL,
                    creator VARCHAR(45) NOT NULL,
                    createdate VARCHAR(45) NOT NULL
                )
            """
            
            try:
                cursor.execute(create_table_article)
                cursor.execute()
                print("[LOG] Tables was seccsessfuly created")
            except Exception as e:
                print("[ERROR]:", e)
            create_user_table_query = """
                CREATE TABLE IF NOT EXISTS user (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(45) NOT NULL,
                    password VARCHAR(256) NOT NULL,
                    joindate VARCHAR(45) NOT NULL
                )
            """
            try:
                cursor.execute(create_user_table_query)
                cursor.execute()
                print("[LOG] Tables was seccsessfuly created")
            except Exception as e:
                print("[ERROR]:", e)
                
def create_virtualenv():
    # Creating virtual einveiromnet 
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
def main():
    create_virtualenv()
    
if __name__ == "__main__":
    main()