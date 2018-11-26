import warnings

import subprocess

import database

from flask import Flask, jsonify, request, abort

warnings.filterwarnings("ignore")

app = Flask(__name__)

items = []

@app.route('/api/v1.0/etudiant', methods=['GET'])
def get_studients():
    database.get_studients()
    result = database.resultsExportEtudiants
    print (result)
    return jsonify({'item': result}), 201

@app.route('/api/v1.0/etudiant/<id_etudiant>', methods=['GET'])
def get_studient(id_etudiant):
    database.get_studient(request.json, id_etudiant)
    result = database.resultsExportEtudiants
    print (result)
    return jsonify({'item': result}), 201

@app.route('/api/v1.0/etudiant', methods=['POST'])
def create_studient():
    database.create_studient(request.json)
    return jsonify({'item': 'studient created'}), 201

@app.route('/api/v1.0/etudiant/<id_etudiant>', methods=['PUT'])
def update_studient(id_etudiant):
    database.update_studient(request.json, id_etudiant)
    return jsonify({'item': 'studient updated'}), 201


@app.route('/api/v1.0/etudiant/<id_etudiant>', methods=['DELETE'])
def delete_studient(id_etudiant):
    database.delete_studient(request.json, id_etudiant)
    return jsonify({'item': 'studient deleted'}), 201

@app.route('/api/v1.0/etudiant', methods=['DELETE'])
def delete_studients():
    database.delete_studients()
    return jsonify({'item': 'studients deleted'}), 201

if __name__ == '__main__':
    app.run(debug=True)
