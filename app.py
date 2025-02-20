from flask import Flask, render_template, request
from pickle import load
from sqlite3 import *

# Load the model from the pickle file
with open("diab.pkl", "rb") as f:
   model = load(f)

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the input values from the form
        fs = float(request.form["fs"])  # Fasting sugar
        fu = request.form["fu"]  # Frequent urination: "yes" or "no"
        
        # Prepare the input data for the model
        if fu == "no":
            data = [[fs, 1, 0]]  # No frequent urination
        else:
            data = [[fs, 0, 1]]  # Yes frequent urination
        
        # Get the model prediction
        ans = model.predict(data)
        if ans == 1:
            msg = "Model says: " + "YES"
        else:
            msg = "Model says: " + "NO"
        
        return render_template("home.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
