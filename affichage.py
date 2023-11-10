from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="probe_values"
)
cursor = db.cursor()

# Route pour afficher les données sur une page web
@app.route('/')
def afficher_donnees():
    cursor.execute("SELECT * FROM table_des_releves")
    data = cursor.fetchall()
    return render_template('affichage_donnees.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)