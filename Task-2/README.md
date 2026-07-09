# Task-2: Real-Time Object Detection System

## Description
This project is a real-time object detection system developed using Python, OpenCV, and YOLOv8. It uses the computer's webcam to detect and identify objects in real time.

## Features
- Real-time webcam object detection
- Uses YOLOv8 pre-trained model
- Detects multiple objects
- Displays bounding boxes and labels
- Fast and accurate detection

## Technologies Used
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- Flask

## Project Structure
```
Task-2/
│── app.py
│── detect.py
│── requirements.txt
│── README.md
│── yolov8n.pt
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python detect.py
```

## Output

- Opens the webcam.
- Detects objects in real time.
- Displays object names and confidence scores.
- Press **Q** to quit.