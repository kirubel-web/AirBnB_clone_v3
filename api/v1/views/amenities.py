#!/usr/bin/python3
"""
    Flask route that returns json respone
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities/', methods=['GET', 'POST'])
def amenities_no_id(amenity_id=None):
    """
        amenities route that handles http requests no ID given
    """
    if request.method == 'GET':
        amenities = []
    for amenity in storage.all("Amenity").values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)

    if request.method == 'POST':
        if not request.get_json():
            return make_response(jsonify({'error': 'Not a JSON'}), 400)
        if 'name' not in request.get_json():
            return make_response(jsonify({'error': 'Missing name'}), 400)
        amenity = Amenity(**request.get_json())
        amenity.save()
        return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenities_with_id(amenity_id=None):
    """
        amenities route that handles http requests with ID given
    """
    amenity_obj = storage.get('Amenity', amenity_id)
    if amenity_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(amenity_obj.to_json())

    if request.method == 'DELETE':
        amenity_obj.delete()
        del amenity_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        amenity_obj.bm_update(req_json)
        return jsonify(amenity_obj.to_json()), 200
