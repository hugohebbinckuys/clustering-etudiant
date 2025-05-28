import unittest
from unittest.mock import patch
from connexion import Connexion
import mysql.connector

class TestConnexion(unittest.TestCase):

    @patch('mysql.connector.connect')  
    def test_connexion_success(self, mock_connect):
        mock_connect.return_value.is_connected.return_value = True

        connexion_instance = Connexion()

        connection = connexion_instance.connexion()

        self.assertIsNotNone(connection)  
        self.assertTrue(connection.is_connected())  

    @patch('mysql.connector.connect')  
    def test_connexion_failure(self, mock_connect):
        mock_connect.side_effect = mysql.connector.Error("Connexion échouée")

        connexion_instance = Connexion()

        connection = connexion_instance.connexion()

        self.assertIsNone(connection)


if __name__ == '__main__':
    unittest.main()
