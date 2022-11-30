import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderkey():
  password = request.form['text']
  with open('ips.txt') as f:
    if request.remote_addr in f.read():
        return render_template('index.html', token='BRUH SCREW U')
  if (password == os.getenv('password')):
    token = os.getenv('token')
  else:
    f = open("ips.txt", "a")
    f.write(request.remote_addr+"\n")
    f.close()
    token = "BRUH SCREW U"

  return render_template('index.html', token=token)

app.run(host='0.0.0.0', port=4000)
