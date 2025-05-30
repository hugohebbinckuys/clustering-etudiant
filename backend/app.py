from flask import Flask, request, jsonify
from flask_cors import CORS
from models.user_model import User
from models.form_model import Form
# from models.affinite_model import save_affinities



app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"]) #pour autoriser les requetes venant udu front

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = User(username=username, password=password)  # Role = "student" par défaut
    success = user.add_user()

    if success:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create user"}), 500
    
    
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.login_user(username, password)
    if user:
        return jsonify({
            "success": True,
            "id_user": user.id_user,
            "role": user.role,
            "username": user.username,
            "id_group": user.id_group
        }), 200
    else:
        return jsonify({"success": False, "message": "Identifiants invalides"}), 401


@app.route('/api/forms', methods=['POST'])
def create_form():
    data = request.get_json()
    open_at = data.get('open_at')
    closed_at = data.get('closed_at')
    choice_number = data.get('choice_number')

    form = Form(open_at, closed_at, choice_number)
    success = form.save()

    if success:
        return jsonify({'message': 'Formulaire créé'}), 201
    else:
        return jsonify({'error': 'Erreur lors de la création'}), 500


@app.route('/api/submit-vote', methods=['POST'])
def submit_vote():
    data = request.json
    try:
        save_affinities(data)
        return jsonify({'message': 'Votes enregistrés avec succès'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500






if __name__ == '__main__':
    app.run(debug=True)
