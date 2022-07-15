from flask import Flask, render_template, request, jsonify
from chat import get_response
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("webhome.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
if __name__ == "__main__":
    app.run(debug=True) 

@app.route("/LifestyleDiseases")
def lifedfacts_page():
    return render_template("lifedfacts.html")