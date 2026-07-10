from flask import Flask, render_template, request
import fitz
import os
import webbrowser

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load skills
with open(os.path.join(BASE_DIR, "skills.txt"), "r") as f:
    skills = [line.strip().lower() for line in f.readlines()]


def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()
    return text.lower()


@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    matched = []
    missing = []

    if request.method == "POST":

        if "resume" not in request.files:
            return render_template(
                "index.html",
                score=None,
                matched=[],
                missing=[]
            )

        file = request.files["resume"]

        if file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            text = extract_text(filepath)

            for skill in skills:
                if skill in text:
                    matched.append(skill)
                else:
                    missing.append(skill)

            score = round((len(matched) / len(skills)) * 100, 2)

    return render_template(
        "index.html",
        score=score,
        matched=matched,
        missing=missing
    )


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5004")
    app.run(host="127.0.0.1", port=5004, debug=True)