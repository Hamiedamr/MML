# -*- coding: utf-8 -*-

import joblib
from flask import Flask
from flask import render_template,request
app = Flask(__name__)

def top_ten(y_proba):
  y=y_proba[0]

  m=[]
  counter=0
  while (counter<10):
      mx_class=y.argmax()
      counter+=1
      m.append(mx_class)
      y=np.delete(y,mx_class,0)
  
  return m
  
def predict(model,encoder,data):
    y_proba = model.predict_proba([[float(data)]])
    result=encoder.inverse_transform(top_ten(y_proba))
    return result


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
        encoder = joblib.load('encoder.sav')
        result=predict(model,encoder,float(data))
        return '<h1>'+str(result)+'</h1>'
    
