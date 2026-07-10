from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import cv2
import webbrowser
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load YOLOv8 model
model = YOLO("yolov8n.pt")


@app.route("/", methods=["GET", "POST"])
def home():
    image = None

    if request.method == "POST":

        file = request.files["image"]

        if file.filename != "":
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # Run YOLO prediction
            results = model(filepath)

            # Plot detection boxes
            annotated = results[0].plot()

            # Save output image
            output_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            cv2.imwrite(output_path, annotated)

            image = file.filename

    return render_template("index.html", image=image)


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5005")
    app.run(debug=True, port=5005)