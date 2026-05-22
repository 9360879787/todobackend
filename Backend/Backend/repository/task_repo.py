
import db


class Taskrepo:
    @staticmethod
    def addtask(data):
        try:
            conn = db.connection()
            mycursor = conn.cursor()

            query = """insert into task (user_id,category_id,tasks,task_data) values (%s,%s,%s,%s)"""
            values = (data['user_id'],data['category_id'],data['tasks'],data['task_data'])
            mycursor.execute(query,values)
            conn.commit()
            return {
                "message":"added successfully"}
        except Exception as e:
            conn.rollback()
            return {
                "message":f"{e}"}
        finally:
            conn.commit()
            conn.close()
    @staticmethod
    def gettask(data):
        try:
            conn = db.connection()
            mycursor = conn.cursor()
            query = """select * from task where user_id = (%s) and category_id = (%s)"""
            values = (data['user_id'],data['category_id'])
            mycursor.execute(query,values)
            row = mycursor.fetchall()    
            column = [col[0] for col in mycursor.description]
            result = [dict(zip(column,r)) for r in row]
            return result
        except Exception as e:
            return {
                "message":f"{e}"}


