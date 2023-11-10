from flask import Flask, request, jsonify
# Bibliotheque python pour se connecter a la BDD
import mysql.connector
import json                      

app = Flask(__name__)

# Configuration de MySQL
# Connexion à la BDD
db = mysql.connector.connect(               
    host="localhost",
    user="root",
    password="root",
    database="probe_values"
)
# Creation d'un objet curseur permettant d'executer des requetes SQL
cursor = db.cursor()

# Route pour recevoir et stocker les données de la sonde
# Creation de la route /releves accessible via POST
@app.route('/releves', methods=['GET','POST'])
# definition d'une fonction recuperant des donnees reçu par la sonde
def receive_data():
    if request.method == 'POST':
    # Si la méthode est POST, récupérez les données de la requête JSON
        data = request.json
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        
        # Stockage des données dans la base de données
        # execution de la requete sql pour inserer les temperatures
        cursor.execute("INSERT INTO table_des_releves (temperature, humidity) VALUES (%s, %s)", (temperature, humidity))
        # Validation et sauvagarde des modifications de la BDD
        db.commit()
        #reponse JSON de la bonne execution
        return jsonify({'message': 'Données reçues et stockées'})
    elif request.method == 'GET':
        # Si la méthode est GET, récupérez toutes les données de la table_des_releves
        cursor.execute("SELECT * FROM table_des_releves")
        data = cursor.fetchall()

        # Convertissez les données en format JSON
        response = jsonify(data)
        return response
if __name__ == '__main__':
    app.run(host='192.168.56.1', port=8080)
