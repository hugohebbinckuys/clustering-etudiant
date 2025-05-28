import mysql.connector

class Connexion: 
    def __init__(self) :
        self.connection = None

    def connexion(self): 
        if self.connection is None:     
            try: 
                self.connection = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="", 
                    database="clustering_etudiant",
                )
                print("connexion réussie")
            except mysql.connector.Error as erreur:
                print(f"Erreur lors de la connexion à la DB : \n{erreur}\n") 
                self.connection = None
        return self.connection
