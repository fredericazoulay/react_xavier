import warnings
import subprocess
import database
import db_users
from flask import Flask, jsonify, request, abort, make_response

#from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

import jwt
import datetime
from functools import wraps
import os

warnings.filterwarnings("ignore")
app = Flask(__name__)
items = []

app.config['SECRET_KEY'] = 'thisissecret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/antho/Documents/api_example/todo.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'flaskr2.db')
#db = SQLAlchemy(app)
#db.create_all()

# ********************************************************************
# AUTH
# ********************************************************************
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/api/v1.0/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    #user = User.query.filter_by(name=auth.username).first()
    db_users.get_user(request.json, auth.id_user)
    user = db_users.resultsExportUsers

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    #if user.password == auth.password: #
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

#@app.route('/api/v1.0/login', methods=['GET'])
#def get_login():
#    db_users.get_users()
#    result = db_users.resultsExportEtudiants
#    print (result)
#    return jsonify({'item': result}), 201

#@app.route('/api/v1.0/register', methods=['GET'])
#def get_register():
#    db_users.get_users()
#    result = db_users.resultsExportEtudiants
#    print (result)
#    return jsonify({'item': result}), 201

#@app.route('/api/v1.0/logout', methods=['GET'])
#def get_logout():
#    db_users.get_users()
#    result = db_users.resultsExportEtudiants
#    print (result)
#    return jsonify({'item': result}), 201

# ********************************************************************
# USERS
# ********************************************************************
@app.route('/api/v1.0/user', methods=['GET'])
def get_users():
    db_users.get_users()
    result = db_users.resultsExportUsers
    print (result)
    return jsonify({'item': result}), 201

@app.route('/api/v1.0/user/<id_user>', methods=['GET'])
def get_user(id_user):
    db_users.get_user(request.json, id_user)
    result = db_users.resultsExportUsers
    print (result)
    return jsonify({'item': result}), 201

@app.route('/api/v1.0/user', methods=['POST'])
def create_user():
    db_users.create_user(request.json)
    return jsonify({'item': 'user created'}), 201

@app.route('/api/v1.0/user/<id_user>', methods=['PUT'])
def update_user(id_user):
    db_users.update_user(request.json, id_user)
    return jsonify({'item': 'user updated'}), 201

@app.route('/api/v1.0/user/<id_user>', methods=['DELETE'])
def delete_user(id_user):
    db_users.delete_user(request.json, id_user)
    return jsonify({'item': 'user deleted'}), 201

@app.route('/api/v1.0/user', methods=['DELETE'])
def delete_users():
    db_users.delete_users()
    return jsonify({'item': 'users deleted'}), 201

# ********************************************************************
# ETUDIANTS
# ********************************************************************
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
