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
                self.connection = db 
                print ("connexion réussie")
                return self.connection
            except mysql.connector.Error as erreur:
                print (f"erreur lors de la connexion a la db : {erreur}") 
                print("connexion réussie")
            except mysql.connector.Error as erreur:
                print(f"Erreur lors de la connexion à la DB : \n{erreur}\n") 
                self.connection = None
                return self.connection 

