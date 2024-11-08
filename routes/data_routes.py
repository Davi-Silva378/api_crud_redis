from flask import Blueprint, request, jsonify
from repositories.data_repository import DataRepository
from service.data_service import DataService
from controllers.data_controller import DataController

data_controller_bp = Blueprint('data_controller', __name__)

data_repository = DataRepository()
data_service = DataService(data_repository)
data_controller = DataController(data_service)

@data_controller_bp.route('/data/<key>', methods=['GET'])
def get_data(key):
  try:
    data = data_service.get_data(key)
    return jsonify({'data': data}), 200
  except Exception as e:
    return jsonify({'Error': str(e)}), 400
  
@data_controller_bp.route('/data', methods=['POST'])
def set_data():
  try:
    key = request.json.get('key')
    value = request.json.get('value')
    data_service.set_data(key, value)
    return jsonify({'message': 'Data set successfully'}), 201
  except Exception as e:
    return jsonify({'Error': str(e)}), 400
  
@data_controller_bp.route('/data', methods=['PUT'])
def update_data():
  try:
    key = request.json.get('key')
    new_value = request.json.get('new_value')
    data = data_service.update_data(key, new_value)
    return jsonify({'message': 'Data updated sucessfully!'}), 200
  except Exception as e:
    return jsonify({'Error': str(e)}), 400
  
@data_controller_bp.route('/data', methods=['DELETE'])
def delete_data():
  try:
    key = request.json.get('key')
    data = data_service.delete_data(key)
    return jsonify({'message': 'Data deleted sucessfully!'}), 200
  except Exception as e:
    return jsonify({'Error': str(e)}), 400