from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/journal")
def dream_journal():
    return render_template("journal.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/introduction")
def introduction():
    return render_template("introduction.html")