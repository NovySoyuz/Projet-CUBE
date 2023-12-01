from flask import Blueprint, render_template, jsonify
from database import cursor
from dotenv import load_dotenv
load_dotenv()
data = Blueprint('data',__name__)
# Permet de rentrer les routes pour afficher le site web
# render_template permet de venir récuperer Page_Donee_Meteo.html dans le dossier templates
# Les route permettent de venir récup les données via le navigateur 
@data.route('/site')
def site_dashboard():
    return render_template("Page_Donee_Meteo.html")

@data.route('/Page_du_Graphique.html')
def graphique_dashboard():
    return render_template("Page_du_Graphique.html")

@data.route('/donnees_graphiques', methods=['GET'])
def get_graph_data():
    cursor.execute("SELECT date, temperature, humidity FROM table_des_releves")
    data = cursor.fetchall()
    
    # Transformez les données en un format attendu par la page web
    # labels permet de mettre en abscisse les informations pour afficher la date
    # Creation d'une liste labels en extrayant la 1er colonne (date) de chaque ligne
    labels = [entry[0] for entry in data]
    # Creation d'une liste temperature en extrayant la 2eme colonne (temperature) de chaque ligne
    temperature = [entry[1] for entry in data]
    # Creation d'une liste humidity en extrayant la 3eme colonne (humidity) de chaque ligne
    humidity = [entry[2] for entry in data]
    # Mise en place d'un dictionnaire pour rentrer les données
    response_data = {
        'labels': labels,
        'temperature': temperature,
        'humidity': humidity
    }

    response = jsonify(response_data)
    return response
