from flask import Flask, render_template, request
import csv
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

movies = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "movies.csv"), "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row)


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        genre = request.form["genre"]

        for movie in movies:
            if movie["genre"].lower() == genre.lower():
                recommendations.append(movie["title"])

    return render_template(
        "index.html",
        recommendations=recommendations
    )


def open_browser():
    webbrowser.open("http://127.0.0.1:5002")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, port=5002)