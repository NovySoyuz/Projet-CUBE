# Bibliotheque mysql.connector = connexion à une bdd
import mysql.connector
# Module os = Permet d'opere avec le systempe d'exploitation  
import os
# dotenv permet d'utiliser et de charger le contenu d'un fichier .env
from dotenv import load_dotenv
# Chargement des variables dans le .env
load_dotenv()
# Configuration de MySQL
# Connexion à la BDD
# Mise en place de variable pour sécuriser l'accés à notre BDD

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS probe_values")
    cursor.execute("USE probe_values")
    cursor.execute("CREATE TABLE IF NOT EXISTS table_des_releves(temperature FLOAT, humidity FLOAT, releve_id INT AUTO_INCREMENT PRIMARY KEY, date DATETIME NOT NULL)")
    db.commit()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE"),
    port=os.getenv("DB_PORT")
)
# Creation d'un objet curseur permettant d'executer des requetes SQL
cursor = db.cursor()
# Fonction pour creer la bdd si elle n'existe pas
