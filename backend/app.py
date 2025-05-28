from flask import Flask, request, jsonify
from user_model import User

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user_route () : 
    infos = request.get_json()
    user = User() 

    