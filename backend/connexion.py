import mysql.connector

class Connexion: 
    def __init__(self) :
        self.connection = None

    def connexion(self) : 
        if self.connection == None :     
            try : 
                db = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="", 
                    database="clustering_etudiant",
                )
                self.connexion = db 
                print ("connexion réussie")
            except mysql.connector.errors as erreur:
                print (f"erreur lors de la connexion a la db : \n{erreur}\n") 
                self.connection = None
        return self.connection

