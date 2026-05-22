
from Backend.repository.category_repo import Categoryrepo



class CategorySerive:
    @staticmethod
    def create_category(data):
        try:
            user_id = data['user_id']
            title = data['title']

            if not user_id:
                return{
                    "message":"user_id is missing"
                    },400

            if not title:
                return {
                    "message":"category title is missing"
                    },400

            return_data = Categoryrepo.addCategory(user_id,title)
            return return_data

        except Exception as e:
            return {
                "message":f"{e}"
                },500
    @staticmethod
    def get_category(data):

        try:
            
        
            if not data['user_id']:
                return {
                    "message":"user_id not exist"},400
            return_data = Categoryrepo.getCategory( data['user_id'] )
            return return_data
        except Exception as e:
            return{
                "error":f"{e}"}


        


