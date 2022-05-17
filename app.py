from flask import Flask, render_template, request, redirect
import numpy as np
import joblib


app =  Flask(__name__)


def predict_student_score(number_courses, time_study):
    filepath = 'model/student_prediction_model.sav'
    model = joblib.load(filename=filepath)
    return model.predict(np.array([number_courses, time_study]).reshape(1,-1))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict-score", methods=["POST","GET"]) 
def predict_score():

    if request.method == "POST":

        try:
            number_courses = int(request.form['number_courses'])
            time_study = int(request.form['time_study'])

            test_score = predict_student_score(number_courses, time_study)
            test_score = round(test_score[0],2)
            return render_template("index.html", prediction_text=test_score)

        except ValueError:

            error_message = "Invalid Input - Use numerical values."
            return render_template("index.html", prediction_text=error_message)

    else:
        redirect("/")
        
        return "Hi"
if __name__ == "__main__":
    app.run(debug=True)