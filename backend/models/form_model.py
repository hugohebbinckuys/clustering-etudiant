from connexion import Connexion
from mysql.connector import Error

class Form:
    def __init__(self, open_at, closed_at, choice_number):
        self.open_at = open_at
        self.closed_at = closed_at
        self.choice_number = choice_number
        self.db_connexion = Connexion().connexion()

    def save(self):
        try:
            connection = self.db_connexion
            cursor = connection.cursor()
            query = "INSERT INTO form (open_at, closed_at, choice_number) VALUES (%s, %s, %s)"
            cursor.execute(query, (self.open_at, self.closed_at, self.choice_number))
            connection.commit()
            return True
        except Error as e:
            print(f"Erreur lors de l'insertion du formulaire : {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
