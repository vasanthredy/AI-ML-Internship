from flask import Flask, render_template, request
import joblib
import webbrowser

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":
        text = request.form["text"]

        text_vector = vectorizer.transform([text])

        prediction = model.predict(text_vector)[0]

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5008")
    app.run(debug=True, port=5008)