
from flask import Blueprint,request,jsonify
from Backend.service.task_service import TaskService
from flask_jwt_extended import jwt_required

task = Blueprint('task',__name__)

@task.route('/addtask',methods=['POST'])
@jwt_required()
def add_task():
    try:
        data = request.get_json()
        if not data:
            return{
                "message":"data is missing"},401
        response = TaskService.add_task(data)
        return jsonify(response,{"message":"task created successfully"})
    except Exception as e:
        return {
            "error":f"{e}"}
@task.route('/gettasks',methods=['POST'])
@jwt_required()
def get_tasks():
    try:
        data = request.get_json()
        if not data:
            return{
                "message":"data is missing"},401
        response = TaskService.get_tasks(data)
        return jsonify(response)
    except Exception as e:
        return {
            "error":f"{e}"}



    