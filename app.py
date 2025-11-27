from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# List of sample quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal.",
    "Dream big and dare to fail.",
    "Action is the foundational key to all success."
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(debug=True)
