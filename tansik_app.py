# -*- coding: utf-8 -*-

import joblib
from flask import Flask
from flask import render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('public/tansik.html')
@app.route('/tansiky',methods=['POST','GET'])
def tansiky():
    if request.method == "GET":
       return home()
    elif request.method == "POST":
        data = request.form['grade']
        model = joblib.load('thanwy_model.sav')
        result = model.predict_proba([[float(data)]])
        return '<h1>'+str(result)+'</h1>'
    
