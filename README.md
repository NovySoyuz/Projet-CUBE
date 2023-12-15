# Projet-CUBE

Votre application devra : 
● Disposer d’une interface web consultable à travers un simple navigateur 
● Être “responsive” 
● Inclure un graphique des données température/humidité 
● Inclure un pictogramme ou code couleur pour déduire à partir des données la météo 
actuelle 
● BONUS : carte pour situer les sondes (sur un JPEG type plan de maison ou de 
terrain, ou sur une carte openstreet maps via leaflet par exemple) 
● BONUS : un bouton de “partage” du graphique ou du dernier relevé vous permettra 
d’envoyer facilement les données à vos amis/familles (mail, réseaux sociaux, autres 
?) 

L’API et la base de données 
● Méthode pour C(reate)R(ead)U(pdate) API sur la table sonde 
● Méthode pour C(reate)R(ead) API sur la table des relevés 
● Tourne sur la même machine locale (en attendant la mise en place du serveur 
Raspberry ou dans le cas de télétravail il est possible d’héberger sur une VM ou 
docker les services requis) 
● BONUS : gérer l’authentification des utilisateurs 

Serveur 
● Il héberge le serveur web 
● Il héberge le SGBDR correctement configuré 
● Il sera administrable via SSH 
● Il héberge l’API 
● La base de données ne sera accessible qu’à travers l’API 
● Il disposera d’un écran afin d’afficher : son adresse IP, la date et heure, et fera défiler 
les derniers relevés des sondes 

Sonde de température 
● Correctement câblée avec les capteurs de température/humidité et alimentation 
(vous ferez valider par un ingénieur de la R&D (votre pilote) le câblage avant mise 
sous tension) 
● Elle sera programmée avec le langage de votre choix compatible avec un ESP (C, 
micropython, LUA) 
● Afin d’éviter les relevés imprécis le capteur fera des relevés toutes les quelques 
secondes et vous en réaliserez une moyenne d’au moins 5 relevés afin d’envoyer 
des données “lissées” à l’API (et avoir un graphique cohérent) 
