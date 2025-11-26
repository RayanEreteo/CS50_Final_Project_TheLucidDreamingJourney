from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", tab=0)

@app.route("/introduction")
def introduction():
    return render_template("introduction.html", tab=1)

@app.route("/dreamjournal")
def dream_journal():
    return render_template("journal.html", tab=2)


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", tab=3)