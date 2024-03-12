from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

#  GET ROUTE
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id":user_id,
        "name":"John Doe",
    }

    extra = request.args.get("extra")

    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data),200 # Status of sucess is 200

# POST ROUTE
@app.route("/create-user",methods = ["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201