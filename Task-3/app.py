import webbrowser
from threading import Timer

from flask import Flask, render_template, request
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

model = joblib.load(os.path.join(BASE_DIR, "diabetes_model.pkl"))


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        values = [
            float(request.form["Pregnancies"]),
            float(request.form["Glucose"]),
            float(request.form["BloodPressure"]),
            float(request.form["SkinThickness"]),
            float(request.form["Insulin"]),
            float(request.form["BMI"]),
            float(request.form["DiabetesPedigreeFunction"]),
            float(request.form["Age"]),
        ]

        result = model.predict([values])[0]

        if result == 1:
            prediction = "⚠️ Diabetic"
        else:
            prediction = "✅ Not Diabetic"

    return render_template("index.html", prediction=prediction)

def open_browser():
    webbrowser.open("http://127.0.0.1:5004")
if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, port=5004)