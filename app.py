import json
from flask import Flask, render_template, request, jsonify

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

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    with open("questions.json") as f:
        questions = json.load(f)
    
    if request.method == "POST":
        user_answer = request.form.get("answer")
        current_question_index = request.form.get("current_question")
        current_question = questions[int(current_question_index) - 1]
        
        print(current_question)
        
        if user_answer != current_question["answer"]: 
            return jsonify({"verdict": "incorrect"})
        
        if int(current_question_index) == len(questions):
            return jsonify({"verdict": "end"}) 
        return jsonify({"verdict": "correct", "next_question": {"title": questions[int(current_question_index)]["title"], "possible_answer": questions[int(current_question_index)]["possible_answer"]}})
    else:
        return render_template("quiz.html", tab=3, q1=questions[0]["title"], pa=questions[0]["possible_answer"])

@app.route("/quizresult")
def quiz_result():
    return render_template("quiz_result.html")