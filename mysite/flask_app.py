
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

