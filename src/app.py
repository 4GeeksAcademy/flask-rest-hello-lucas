from flask import Flask, request, jsonify, abort
from models import db, User, People, Planet, Favorite

# Existing code...

@app.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    return jsonify([person.to_dict() for person in people]), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person_by_id(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.to_dict()), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planet.query.all()
    return jsonify([planet.to_dict() for planet in planets]), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get_or_404(planet_id)
    return jsonify(planet.to_dict()), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # For simplicity, assuming the user_id is passed as a query parameter
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400, 'User ID is required')
    user = User.query.get_or_404(user_id)
    favorites = Favorite.query.filter_by(user_id=user.id).all()
    return jsonify([favorite.to_dict() for favorite in favorites]), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400, 'User ID is required')
    user = User.query.get_or_404(user_id)
    favorite = Favorite(user_id=user.id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(favorite.to_dict()), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400, 'User ID is required')
    user = User.query.get_or_404(user_id)
    favorite = Favorite(user_id=user.id, people_id=people_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(favorite.to_dict()), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def remove_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400, 'User ID is required')
    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first_or_404()
    db.session.delete(favorite)
    db.session.commit()
    return '', 204

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def remove_favorite_people(people_id):
    user_id = request.args.get('user_id')
    if not user_id:
        abort(400, 'User ID is required')
    favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id).first_or_404()
    db.session.delete(favorite)
    db.session.commit()
    return '', 204
