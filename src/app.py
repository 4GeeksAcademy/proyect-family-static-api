"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Endpoint GET para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_members():
    # Obtenemos todos los miembros
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint GET para recuperar un miembro de la familia por ID 
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "No se encontro miembro"}), 404

# Endpoint POST para agregar un miembro a la familia
@app.route('/member', methods=['POST'])
def add_new_member():
    data = request.json
    # Verificar si los datos contienen los campos necesarios
    if not data or not all(key in data for key in ["first_name", "age", "lucky_numbers"]):
        return jsonify({"error": "Entrada no válida. Se requieren los campos: 'name', 'age', 'lucky_numbers'"}), 400
     
    # Agregar el miembro utilizando el método add_member de FamilyStructure
    member = jackson_family.add_member(data)
     
    # Devolver el miembro agregado en formato JSON con código de estado 201 (creado)
    return jsonify(member), 200

# Endpoint DELETE para borrar un miembro de la familia
@app.route('/member/<int:position>', methods=['DELETE'])
def delete_member(position):
    result = jackson_family.delete_member(position)
    if result:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
