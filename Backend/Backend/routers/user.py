
from flask import Blueprint,request,jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
import db
from flask_jwt_extended import create_access_token,create_refresh_token, get_jwt_identity,jwt_required

login = Blueprint('login',__name__)

@login.route('/refresh',methods=['POST'])
@jwt_required(refresh=True)
def refres():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify({
        "message":access_token})



@login.route('/login',methods=['POST'])

def loginuser():
    data = request.get_json()
    token = data.get('token')
    idinfo = id_token.verify_oauth2_token(
        token, 
        requests.Request(),
       "271579416782-249cq1ltjtrn49ir9i96qcqe0iggb8s0.apps.googleusercontent.com")
    
    name = idinfo.get('name')

    email_id = idinfo.get('email')

    google_id = idinfo.get('sub')

    profile_pic = idinfo.get('picture')
    
    conn = db.connection()
    mycursor = conn.cursor()
    if not email_id:    
        return jsonify({"message":"Email not exist"}),400
    
    try:
        def fetch_data(email_id,mycursor):
            mycursor.execute("select * from user where email_id = %s",(email_id,))
            return mycursor.fetchall()
    
        row = fetch_data(email_id,mycursor)
        def convert_to_dict(row,mycursor,email_id):
                access_token = create_access_token(identity=email_id)
                refresh_token = create_refresh_token(identity=email_id)
        
                columns = [column[0] for column in mycursor.description]
                print(columns)

                user = [dict(zip(columns, r))for r in row]

                return jsonify({
                    "data": user,
                    "access_token":access_token,
                    "refresh_token":refresh_token
                        
                })
        if row:
             return convert_to_dict(row,mycursor,email_id)
        else:
            if not name or not  email_id or not  google_id or  not profile_pic:
                return jsonify({"message":"some value is missing"}),400
            query1 = "insert into user (u_name, email_id, google_id, profile_pic) values (%s,%s,%s,%s)"
            values = (name,email_id,google_id,profile_pic)
            mycursor.execute(query1,values)
            conn.commit()
            conn.close()
            row = fetch_data(email_id,mycursor)
            if row:
                return convert_to_dict(row,mycursor,email_id),201
      
            return jsonify({
                "message": "User created successfully"
            }),
    except Exception as e:
        return jsonify({"message":f"{e}"}),500
        

