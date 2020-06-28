#Hackmann 2020, Carmel, Samuel, Jolie, Arya; "Is a hotdog a sandwhich?"

from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = b'5k\xd0\x1b\x96+\xbd(T\xd8"\x99\x84\x19 \x15'
app.debug = True

#Index / First Q
@app.route("/")
def index():
    return render_template('questionpage1.html',question_number=1, question="Is a hotdog a sandwhich?")
