import db

class Categoryrepo:
    @staticmethod
    def addCategory(user_id,title):

        try:
            conn = db.connection()
            mycursor = conn.cursor()

            qurey = """insert into category (user_id,title)
                        values (%s,%s)"""
            values = (user_id,title )

            row =  mycursor.execute(qurey,values)
            
            conn.commit()
            
            return {
                "id":mycursor.lastrowid,
                "message":"category added successfully "
                },201
        except Exception as e:
             conn.rollback()
             return {
               "error":f"{e}"
               },400
        finally:
            conn.commit()
            conn.close()


# -----------------GetCategory------------------

    @staticmethod
    def getCategory(user_id):
        try:
            conn = db.connection()
            mycursor = conn.cursor()

            query = """ 
           select * from category where user_id = (%s)
          """

            value = (user_id,)
            mycursor.execute(query,value)
            row = mycursor.fetchall()    
            column = [col[0] for col in mycursor.description]
            result = [dict(zip(column,r)) for r in row]
            return result

        except Exception as e:
            return{
                "error":f"{e}"}

        finally:
            conn.commit()
            conn.close()
            
           


        