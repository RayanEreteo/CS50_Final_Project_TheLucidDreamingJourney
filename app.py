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
    answers = [{"title": "What MILD mean ?", "answer": "Mnemonic Induced Lucid Dream"}]
    
    if request.method == "POST":
        user_answer = request.form.get("answer")
        current_question = request.form.get("current_question")
        current_question_answer = answers[int(current_question) - 1]
        
        if user_answer != current_question_answer["answer"]: 
            return jsonify({"verdict": "incorrect"})
        
        return jsonify({"verdict": "correct"})
    else:
        return render_template("quiz.html", tab=3, q1=answers[0]["title"])