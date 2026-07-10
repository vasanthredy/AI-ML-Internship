from flask import Flask, render_template, request
import joblib
import numpy as np
import webbrowser

app = Flask(__name__)

# Load trained model
model = joblib.load("digit_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        try:
            pixels = request.form["pixels"]

            values = [float(x) for x in pixels.split(",")]

            if len(values) != 64:
                prediction = "Please enter exactly 64 pixel values."

            else:
                values = np.array(values).reshape(1, -1)
                prediction = model.predict(values)[0]

        except:
            prediction = "Invalid input."

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5007")
    app.run(debug=True, port=5007)