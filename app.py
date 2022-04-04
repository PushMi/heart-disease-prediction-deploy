# Importing the libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Global Variables
app = Flask("app")
loaded_model = pickle.load(open('Model.pkl', 'rb'))


# Routes
@app.route("/")
def home():
    return render_template("page.html")

@app.route("/prediction", methods = ['Post'])
def predict():
    age = int(request.form["age"])
    gender = int(request.form["gender"])
    paintype = int(request.form["paintype"])
    restingbp = int(request.form["restingbp"])
    cholesterol = int(request.form["cholesterol"])
    fastingbs = int(request.form["fastingbs"])
    restingecg = int(request.form["restingecg"])
    maxhr = int(request.form["maxhr"])
    exercise = int(request.form["exercise"])
    oldpeak = float(request.form["oldpeak"])
    stslope = int(request.form["stslope"])
     
    print (type (age))
    print (type(gender))
    print (type(paintype))
    print (type(restingbp))
    print (type(cholesterol))
    print (type(fastingbs))
    print (type(restingecg))
    print (type(maxhr))
    print (type(exercise))
    print (type(oldpeak))
    print (type(stslope))
    
    prediction = loaded_model.predict([[age, gender, paintype, restingbp, cholesterol, fastingbs, restingecg, maxhr, exercise, oldpeak, stslope]])[0]
    probability = loaded_model.predict_proba([[age, gender, paintype, restingbp, cholesterol, fastingbs, restingecg, maxhr, exercise, oldpeak, stslope]])
    probability = np.round((np.max(probability) * 100), 2)
    output = " "
    probability = f"{probability}"
    
    if prediction == 0:
        output = "You don't have Heart Disease :)"
    else:
        output = "you have Heart Disease :/"
        
    print(prediction, probability)
    
    return render_template("page.html", output_prediction = output, output_proba = probability)

     
# Main function
if __name__ == '__main__':
    app.run(debug = True)