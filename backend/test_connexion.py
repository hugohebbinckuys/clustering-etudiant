import unittest
from unittest.mock import patch
from connexion import Connexion
import mysql.connector

class TestConnexion(unittest.TestCase):

    @patch('mysql.connector.connect')  # Mock de la connexion MySQL
    def test_connexion_success(self, mock_connect):
        # On simule une connexion réussie
        mock_connect.return_value.is_connected.return_value = True

        # Créer une instance de la classe Connexion
        connexion_instance = Connexion()

        # Appel de la méthode connexion
        connection = connexion_instance.connexion()

        # Vérifier si la connexion est réussie
        self.assertIsNotNone(connection)  # Vérifier que la connexion n'est pas None
        self.assertTrue(connection.is_connected())  # Vérifier si la connexion est active

    @patch('mysql.connector.connect')  # Mock de la connexion MySQL
    def test_connexion_failure(self, mock_connect):
        # On simule un échec de connexion
        mock_connect.side_effect = mysql.connector.Error("Connexion échouée")

        # Créer une instance de la classe Connexion
        connexion_instance = Connexion()

        # Appel de la méthode connexion
        connection = connexion_instance.connexion()

        # Vérifier que la connexion est échouée (retourne None)
        self.assertIsNone(connection)


if __name__ == '__main__':
    unittest.main()
