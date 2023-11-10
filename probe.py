# Permet de faire des requetes HTTP
import requests
import time
import random

while True:
    # Simulation de la collecte de données par la sonde
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)

    # Envoi des données à l'API du serveur Flask
    api_url = "http://192.168.56.1:8080/releves"
    data = {'temperature': temperature, 'humidity': humidity}
    # Envoi de la requete HTTP et les donnees sont en json
    response = requests.post(api_url, json=data)

    print("Données envoyées à l'API Flask :", response.json())

    # Attente avant la prochaine collecte de données (simulée ici toutes les 5 secondes)
    time.sleep(5)