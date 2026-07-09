from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

def open_browser():
    webbrowser.open("http://127.0.0.1:5001")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=True, port=5001)