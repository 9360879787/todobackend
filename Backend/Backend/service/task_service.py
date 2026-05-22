from Backend.repository.task_repo import Taskrepo

class TaskService:
    @staticmethod
    def add_task(data):
        try:
            if not data['user_id']:
                return{
                    "message":"user_id mot found"},401
            if not data['category_id']:
                return{
                    "message":"category_id mot found"},401
            if not data['tasks']:
                  return{
                    "message":"tasks mot found"},401
            if not data['task_data']:
                  return{
                    "message":"date mot found"},401
            return_data = Taskrepo.addtask(data)
        except Exception as e:
            return{
                "error":f"{e}"}
    @staticmethod
    def get_tasks(data):
        try:
            if not data['user_id']:
                return{
                    "message":"user_id mot found"},401
            if not data['category_id']:
                return{
                    "message":"category_id mot found"},401
            return_data = Taskrepo.gettask(data)
            return return_data
        except Exception as e:
            return{
                "error":f"{e}"}
        


