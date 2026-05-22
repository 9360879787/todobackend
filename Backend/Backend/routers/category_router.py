from flask import Blueprint,request,jsonify
from Backend.service.category_service import CategorySerive

    
from flask_jwt_extended import jwt_required

category = Blueprint('category',__name__)

@category.route('/category',methods=['POST'])
@jwt_required()

def addcategory():

    try:
        data = request.get_json()
        response = CategorySerive.create_category(data)

        return jsonify(response),201
    except Exception as e:
        return jsonify({
           "message":f"{e}"
           }),500

@category.route('/getcategory',methods=['POST'])
@jwt_required() 

def getCategory():
    try:
        data = request.get_json()
        response = CategorySerive.get_category(data)
        return jsonify(response)
    except Exception as e:
        return {"error":f"{e}"}


