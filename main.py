from flask import Flask, request, jsonify
from flask_cors import CORS
# Bibliotheque python pour se connecter a la BDD
import mysql.connector
import json                      
import os
from dotenv import load_dotenv

# Chargement des variables dans le .env
load_dotenv()
app = Flask(__name__)
CORS(app)

# Configuration de MySQL
# Connexion à la BDD
db = mysql.connector.connect(               
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE"),
    port=os.getenv("DB_PORT")
)
# Creation d'un objet curseur permettant d'executer des requetes SQL
cursor = db.cursor()

# Route pour recevoir et stocker les données de la sonde
# Creation de la route /releves accessible via POST
@app.route('/releves', methods=['GET','POST','PUT','DELETE'])
# definition d'une fonction recuperant des donnees reçu par la sonde
def receive_data():
    if request.method == 'POST':
    # Si la méthode est POST, récupérez les données de la requête JSON
        data = request.json
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        
        # Stockage des données dans la base de données
        # execution de la requete sql pour inserer les temperatures
        # %s = sécurisation des requetes sql
        cursor.execute("INSERT INTO table_des_releves (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
        # Validation et sauvagarde des modifications de la BDD
        db.commit()
        #reponse JSON de la bonne execution
        return jsonify({'message': 'Données reçues et stockées'})
    
    if request.method == 'GET':
        # Si la méthode est GET, récupérez toutes les données de la table_des_releves
        
        cursor.execute("SELECT * FROM table_des_releves")
        # Récupère toutes les lignes du résultat
        data = cursor.fetchall()

        # Convertissez les données en format JSON
        response = jsonify(data)
        return response
    
    if request.method == 'PUT':
        # Si la méthode est PUT, récupérez toutes les données de la table_des_releves
        releve_id = request.args.get('releve_id')
        temperature = request.json.get('temperature')
        humidity = request.json.get('humidity')
        cursor.execute("UPDATE table_des_releves SET temperature=%s, humidity=%s WHERE releve_id=%s", (temperature, humidity, releve_id))
        db.commit()
        
        # Réponse JSON de la mise à jour réussie
        return jsonify({'message': 'Données mises à jour avec succès'})
    if request.method == 'DELETE':
        # Supprimez les données de la table "table_des_releves"
        releve_id = request.args.get('releve_id')
        cursor.execute("DELETE FROM table_des_releves WHERE releve_id=%s", (releve_id,))
        db.commit()
        
        # Réponse JSON de la suppression réussie
        return jsonify({'message': 'Données supprimées avec succès'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
