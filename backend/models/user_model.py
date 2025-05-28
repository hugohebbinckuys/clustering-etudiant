import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connexion import Connexion

from mysql.connector import Error
from connexion import Connexion

class User:
    def __init__(self, id_user=None, role="student", username=None, password=None, id_group=None ):

        self.id_user = id_user
        self.role = role
        self.username = username
        self.password = password
        self.id_group = id_group

        self.db_connexion = Connexion().connexion() 
        # ici Connexion à avec une majuscule et des parenthèses car crée une instance de Connexion donc parenthèses. 

    
    def add_user(self):
        connection = self.db_connexion
        if connection is None:
            print("Connexion à la base échouée")
            return False

        cursor = None
        try:
            cursor = connection.cursor()
            query = "INSERT INTO user (role, username, password, id_group) VALUES (%s, %s, %s, %s)"
            values = (self.role, self.username, self.password, self.id_group)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Error as e:
            print(f"Failed to create new user: {e}")
            return False
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def login_user(username, password):
        from connexion import Connexion
        connection = Connexion().connexion()

        if connection is None:
            print("Connexion à la base échouée")
            return None

        cursor = None
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM user WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                return User(
                    id_user=result["id_user"],
                    role=result["role"],
                    username=result["username"],
                    password=result["password"],
                    id_group=result["id_group"]
                )
            else:
                print("Identifiants incorrects")
                return None
        except Error as e:
            print(f"Erreur lors de la tentative de login : {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()




    
    def update_user(self):

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            query =''

            values = (self.nom,self.role,self.username,self.password,self.id_group)

            cursor.execute(query,values)
            connection.commit()

            return True
        
        except Error as e :
            print(f"failed to update user : {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def delete_user(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM user WHERE id = %s"
            cursor.execute(query, (self.id,))
            connection.commit()
            
            return cursor.rowcount > 0
            
        except Error as e:
            print(f"failed to delete user : {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def get_user_by_id(user_id):

        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = "SELECT * FROM user WHERE id_user = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                return User(
                    id=result['id_user'],
                    role=result['role'],
                    username=result['username'],
                    password=result['password'],
                    id_group = result["id_group"],
                )
            return None
            
        except Error as e:
            print(f"failed to get user by id : {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def get_all_user():
        
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = "SELECT * FROM user ORDER BY id_user"
            cursor.execute(query)
            results = cursor.fetchall()
            
            users = []
            for result in results:
                users.append(User(
                    id_user=result['id_user'],
                    role=result['role'],
                    username=result['username'],
                    password=result['password'],
                    id_group=result['id_group'],
                ))
            
            return users
            
        except Error as e:
            print(f"failed to display users : {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def get_all_students():
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = "SELECT * FROM user ORDER BY id_user where role = student"
            cursor.execute(query)
            results = cursor.fetchall()
            
            users = []
            for result in results:
                users.append(User(
                    id_user=result['id_user'],
                    role=result['role'],
                    username=result['username'],
                    password=result['password'],
                    id_group=result['id_group'],
                ))
            
            return users
            
        except Error as e:
            print(f"failed to display students : {e}")
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()








    



