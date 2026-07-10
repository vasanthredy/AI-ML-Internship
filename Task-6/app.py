from flask import Flask, render_template, request
import joblib
import webbrowser

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        news = request.form["news"]

        transformed = vectorizer.transform([news])
        prediction = model.predict(transformed)[0]

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5006")
    app.run(debug=True, port=5006)