import mysql.connector

class Connexion: 
    def __init__(self) :
        self.connection = None

    def is_connected (self) : 
        if self.connection != None : 
            return True
        return False

    def connexion(self) : 
        if not self.is_connected() :     
            try : 
                db = mysql.connector.connect(
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
                self.connection = None
                return self.connection 

