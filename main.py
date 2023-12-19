# Bibliotheque Request, Jsonify, render_template, Flask_cors, Mysql.connector

from flask import Flask, request, jsonify, blueprints
from flask_cors import CORS
from database import db, cursor, create_database
# Importation des fichiers
from auth import data
from dotenv import load_dotenv
from flasgger import Swagger
# Variables dans le .env
create_database()
load_dotenv()
# Lancement d'un script python
app = Flask(__name__)
swagger = Swagger(app)
# Initialise la route /data depuis data dans auth.py
app.register_blueprint(data, url_prefix='/data')
# Lancement de CORS
CORS(app)
# Route pour recevoir et stocker les données de la sonde
# Creation de la route /releves accessible via POST
@app.route('/releves', methods=['GET','POST','PUT','DELETE'])

# Donner recupéré par la sonde methode post
def receive_data():
    """
    Endpoint to receive and store sensor data.
    ---
    parameters:
      - name: temperature
        in: formData
        type: number
        required: true
        description: The temperature value.
      - name: humidity
        in: formData
        type: number
        required: true
        description: The humidity value.
    responses:
      200:
        description: Data received and stored successfully.
    """
    if request.method == 'POST':
        data = request.json
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        cursor.execute("INSERT INTO table_des_releves (temperature, humidity, date) VALUES (%s, %s, NOW())", (temperature, humidity))
        db.commit()
        return jsonify({'message': 'Données reçues et stockées'})
    #Methode Get
    if request.method == 'GET':
        
        cursor.execute("SELECT * FROM table_des_releves")
        data = cursor.fetchall()

        # Convertissez les données en format JSON
        response = jsonify(data)
        return response
    #methode Put
    if request.method == 'PUT':
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
