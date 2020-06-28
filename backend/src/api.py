import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

## ROUTES
'''
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['GET'])
def get_drinks():
    try: 
        drinks = [drink.short() for drink in Drink.query.all()]
        return json.dumps({
            'success': True,
            'drinks': drinks
        }), 200
            
    except:
        print(sys.exc_info())
        return json.dumps({
            'success': False,
            'error': 'Error while retrieving drinks'
        }), 500

'''
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(f):
    try: 
        drinks = [drink.long() for drink in Drink.query.all()]
        return json.dumps({
            'success': True,
            'drinks': drinks
        }), 200
            
    except:
        print(sys.exc_info())
        return json.dumps({
            'success': False,
            'error': 'Error while retrieving drinks detail'
        }), 500


'''
    POST /drinks endpoint
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(f):
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    if (title == None and recipe == None) or recipe == None:
        return jsonify({
            "success": False, 
            'error': 'Bad request'
        }), 400

    try:
        drink = Drink(title=title, recipe=json.dumps(recipe))
        drink.insert()

        return jsonify({
            "success": True, 
            "drinks": drink.long()
        }), 200
    except:
        print(sys.exc_info())
        return jsonify({
            "success": False, 
            'error': 'Error while saving drink'
        }), 500

'''
    PATCH /drinks/<id> endpoint
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(f, drink_id):
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    if (title == None and recipe == None) or recipe == None:
        return jsonify({
            "success": False, 
            'error': 'Bad request'
        }), 400

    try:
        drink = Drink.query.filter(
            Drink.id == drink_id).one_or_none()
        
        if drink:
            drink.title=title
            if recipe:
                drink.recipe=json.dumps(recipe)
            drink.update()
        else:
            return jsonify({
                "success": False, 
                'error': 'Drink not found'
            }), 404

        return jsonify({
            'success': True,
            'drinks': drink.long()
        }), 200

    except:
        return jsonify({
            "success": False, 
            'error': 'Error while updating drink'
        }), 500


'''
    DELETE /drinks/<id> endpoint
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(f, drink_id):
    try:
        drink = Drink.query.filter(
            Drink.id == drink_id).one_or_none()
        
        if drink:
            drink.delete()
        else:
            return jsonify({
                "success": False, 
                'error': 'Drink not found'
            }), 404

        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200

    except:
        return jsonify({
            "success": False, 
            'error': 'Error while deleting the drink'
        }), 500

## Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "bad request"
    }), 400

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def auth_error(exception):
    response = jsonify(exception.error)
    response.status_code = exception.status_code
    return response