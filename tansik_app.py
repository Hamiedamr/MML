# -*- coding: utf-8 -*-

import joblib
from flask import Flask
from flask import render_template,request
import numpy as np
from wtforms import Form, FloatField  , validators
app=Flask(__name__)
model = joblib.load('thanwy_model.sav')
encoder = joblib.load('encoder.sav')


class TansikForm(Form):
    tansik = FloatField("tansik",[validators.NumberRange(min=205,max=410,message="Enter valid grade"),validators.DataRequired()])

def top_ten(y_proba):
  y=y_proba[0]

  m=[]
  counter=0
  while (counter<42):
      mx_class=y.argmax()
      counter+=1
      m.append(mx_class)
      y=np.delete(y,mx_class,0)
  
  return m
  
def predict(model,encoder,data):
    y_proba = model.predict_proba([[float(data)]])
    result=encoder.inverse_transform(top_ten(y_proba))
    return result


@app.route('/',methods=['POST','GET'])
def tansiky():
    form  = TansikForm(request.form)
    if request.method == "POST" and  form.validate():
        data = form.tansik.data
        result=predict(model,encoder,float(data))
        return render_template('public/results.html',result=result)
    return render_template('public/tansik.html',form=form)
    

