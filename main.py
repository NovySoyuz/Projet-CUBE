# Import du framework Flask 
# Bibliotheque request = envoyer des requetes http
# Bibliotheque jsonify = convertir les données en json
# Bibliotheque render_template = permet de récuprer des fichiers dans le dossier templates
from flask import Flask, request, jsonify, blueprints
# Bibliotheque flask_cors = permet, à travers des en-têtes HTTP, d'autoriser un utilisateur l'accès à des resources situées sur une autre origine que le site courant
from flask_cors import CORS
# Bibliotheque mysql.connector = connexion à une bdd
from database import db, cursor, create_database
# On importe data du fichier auth pour pouvoir aller sur la route 
from auth import data
# dotenv permet d'utiliser et de charger le contenu d'un fichier .env
from dotenv import load_dotenv
# Chargement des variables dans le .env
create_database()
load_dotenv()
# Lancement d'un script python
app = Flask(__name__)
# Initialise la route /data depuis data dans auth.py
app.register_blueprint(data, url_prefix='/data')
# Lancement de CORS
CORS(app)
# Route pour recevoir et stocker les données de la sonde
# Creation de la route /releves accessible via POST
# Argument methods (on aurait pu remplacer par endpoint ou autre) pour pouvoir utiliser la route
@app.route('/releves', methods=['GET','POST','PUT','DELETE'])
# definition d'une fonction recuperant des donnees reçu par la sonde

def receive_data():
    if request.method == 'POST':
    # Si la méthode est POST, récupérez les données de la requête en JSON
        data = request.json
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        # Stockage des données dans la base de données
        # execution de la requete sql pour inserer les temperatures
        # %s = sécurisation des requetes sql
        cursor.execute("INSERT INTO table_des_releves (temperature, humidity, date) VALUES (%s, %s, NOW())", (temperature, humidity))
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
