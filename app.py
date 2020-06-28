#Hackmann 2020, Carmel, Samuel, Jolie, Arya; "Is a hotdog a sandwhich?"

from flask import Flask, session, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)
app.secret_key = b'5k\xd0\x1b\x96+\xbd(T\xd8"\x99\x84\x19 \x15'
app.debug = True

#Index
@app.route("/")
def index():
    session["qn"] = 0
    return redirect('/q')

#Q page
@app.route("/q", methods = ['GET', 'POST'])
def qpage(): 
    if request.method == 'POST':
        if request.form['yes'] == 'yes':
            return redirect('/a')
        elif request.form['no'] == 'no':
            return redirect('/a')

    session["qn"] = session["qn"] + 1
    print("qn up")
    qn = session["qn"]
    question = "Is a hotdog a sammich"


    return render_template('questionpage1.html', question_number = qn, question = question)

#A page
@app.route("/a")
def apage():
    qn = session["qn"]
    if(qn >= (5) - 1):
        return render_template('questionpage2.html', question_number = qn, nextLink = "/r")
    else:
        return render_template('questionpage2.html', question_number = qn, nextLink = "/q")

#Final page
@app.route("/r")
def results():
    return render_template('results.html')
