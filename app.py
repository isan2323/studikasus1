from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritzy", "score": 40},
    {"name": "Sirlus", "score": 75},
]

@app.route("/")
def index():
    return render_template("index.html", students=students)