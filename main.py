import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderkey():
  password = request.form['text']
  if (password == os.getenv('password')):
    token = os.getenv('token')
  else:
    token = "BRUH SCREW U"

  return render_template('index.html', token=token)

app.run(host='0.0.0.0', port=8080)
