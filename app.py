from flask import Flask, request, redirect, url_for, flash, render_template
import json 

app = Flask(__name__)

with open('./templates/config.json', 'r') as c:
    params = json.load(c)["params"]

@app.route('/')
def home():
    return render_template('home.html', params=params)

if __name__ == "__main__":
    app.run(debug=True)