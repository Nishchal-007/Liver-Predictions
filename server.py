from flask import Flask, flash, request, redirect, url_for, render_template, send_file
import os
import warnings
warnings.filterwarnings("ignore")

PEOPLE_FOLDER = os.path.join('static','images')
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/check-up", methods=['GET'])
def Check_Up():
    return render_template('check.html')

#JUST DO IT!!!
if __name__=="__main__":
    app.run(port="9000")