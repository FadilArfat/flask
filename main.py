from flask import Flask, jsonify,render_template, request
import os
import joblib

app = Flask(__name__)


@app.route('/',methods=['POST', 'GET'])
def home():
  feature = open('vect.pkl', 'rb')
  model = open('iris.pkl', 'rb')

  vec = joblib.load(feature)
  rbf = joblib.load(model)

  if request.method == 'POST':
    inp = request.form['inp']
    data = [inp]
    vect = vec.transform(data)
    my_prediction = rbf.predict(vect)[0]
    if my_prediction == 1:
        return render_template('home.html', message = "Sentimen negatif 😡")
    else:
        return render_template('home.html', message = 'sentimen positif 🙂')
    
  return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
