#Hackmann 2020, Carmel, Samuel, Jolie, Arya; "Is a hotdog a sandwhich?"

from flask import Flask, session

app = Flask(__name__)
app.secret_key = b'5k\xd0\x1b\x96+\xbd(T\xd8"\x99\x84\x19 \x15'

#Index / First Q
@app.route('/')
def index():

#Subsequent Q's
@app.route('/<qNum>')
def qn(qNum):

#Comment
@app.route('/<cNum>')
def cn(cNum):

#Results
@app.route('/results')
def results():
