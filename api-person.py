# PROJET API PERSON BY FLORIAN
# V1 20/05/2021

import json
from flask import Flask, request, jsonify
from flask_cors import *
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'apiperson',
    'host': 'localhost',
    'port': 27017
}

api_v1_cors_config = {
    "origins": ["*"],
    "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Authorization", "Access-Control-Allow-Origin", "content-type"]
}
CORS(app, resources={"/*": api_v1_cors_config})


db = MongoEngine()
db.init_app(app)


class Personne(db.Document):
    id = db.IntField(unique=True)
    nom = db.StringField(max_length=255, required=True)
    prenom = db.StringField(max_length=255, required=True)
    naissance = db.StringField(max_length=255, required=True)
    postale = db.IntField()
    email = db.StringField(max_length=255, required=True)
    tel = db.StringField(max_length=255)


@app.route("/")
@cross_origin()  # allow all origins all methods.
def __repr__():
    return "<h1> Ajouter une personne </h1><form action='/personne/addtraitement' method='POST'> <input name='nom' placeholder='nom'><input name='prenom' placeholder='prenom'><input name='naissance' placeholder='naissance'><input name='postale' placeholder='postale'><input name='email' placeholder='email'><input name='tel' placeholder='tel'><input type='submit'></form><br><h1>Supprimer une personne</h1><form action='/personne/deletetraitement' method='POST'> <input name='nom' placeholder='nom'><input name='prenom' placeholder='prenom'><input type='submit'></form><br><a href='/personne'>Voir toutes les personnes disponibles</a>"


@app.route("/up")
def up():
    """
    Just for test if API is up

    Returns :
    {string} -- OK if API is up
    """
    return "OK"


def test_up():
    assert up() == "OK"

# Route : /personne
# Méthode : GET
# Récupérer les informations de toutes les personnes


@app.route('/personne', methods=['GET'])
def query_records():
    tab_apiperson = []
    for p in Personne.objects:
        tab_apiperson.append(p)
    return jsonify(tab_apiperson)


# Route : /personne/only?nom=HOCHART&prenom=Florian
# Méthode : GET
# Récupérer les informations d'une personne

@app.route('/personne/only', methods=['GET'])
def query_record():
    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    personne = Personne.objects(nom=nom, prenom=prenom).first()
    if not personne:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(personne.to_json())


# Route : /personne
# Méthode : POST
# Ajouter une nouvelle personne

@app.route('/personne/addtraitement', methods=['GET', 'POST'])
@cross_origin()  # allow all origins all methods.
def create_record():
    record = request.form
    pid = record['id']
    pnom = record['nom']
    pprenom = record['prenom']
    pnaissance = record['naissance']
    ppostale = record['postale']
    pemail = record['email']
    ptel = record['tel']
    personne = Personne(id=pid, nom=pnom, prenom=pprenom,
                        naissance=pnaissance, postale=ppostale, email=pemail, tel=ptel)
    personne.save()
    return jsonify(personne.to_json())


# Route : /personne
# Méthode : DELETE
# Supprimer une personne existante

@app.route('/personne/deletetraitement', methods=['GET', 'POST', 'DELETE'])
@cross_origin()  # allow all origins all methods.
def delete_record():
    record = request.form
    name = record['nom']
    firstname = record['prenom']
    nom = name
    prenom = firstname
    personne = Personne.objects(nom=nom, prenom=prenom).first()
    if not personne:
        return jsonify({'error': 'data not found'})
    else:
        personne.delete()
    return jsonify(personne.to_json())


if __name__ == "__main__":
    app.run(debug=True)
