from mysql.connector import Error
from connexion import Connexion

class Affinitie:

    def __init__(self, id_affinity=None, student_1=None, student_2=None, value_aff=None):
        self.id_affinity = id_affinity
        self.student_1 = student_1
        self.student_2 = student_2
        self.value_aff = value_aff
        self.db_connection = Connexion().connexion()

    def save_affinities(self, data):
        try:
            connection = self.db_connection
            cursor = connection.cursor()

            voting_student = data['voting']
            votes = data['votes']  # Liste de { student_id, value }

            for vote in votes:
                cursor.execute("""
                    INSERT INTO affinities (student_1, student_2, value_aff)
                    VALUES (%s, %s, %s)
                """, (voting_student, vote['student_id'], vote['value']))

            connection.commit()
        except Error as e:
            print("Erreur lors de l'insertion dans affinities :", e)
        finally:
            if cursor:
                cursor.close()


    
    def add_affinity(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            query = " INSERT INTO affinity (student_1, student_2, value_aff)"
            values = (self.student_1,self.student_2,self.value_aff)

            cursor.execute(query,values)
            connection.commit()

            return True
            
        except Error as e:
            print(f"Failed to add affinity :{e}")
            return False
            
        finally: # execute in any case (failed or success) to free databases usage
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def delete_affinity(id_affinity):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM user WHERE id = %s"
            cursor.execute(query, (id_affinity,))
            connection.commit()
            
            return cursor.rowcount > 0
            
        except Error as e:
            print(f"failed to delete affinity : {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    

