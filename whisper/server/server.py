from flask import Flask

app = Flask(__name__)


@app.route("/Record/Start",methods=["POST"])
def start_recording():
    return "Recording Started"

@app.route("/Record/Stop",methods=["GET"])
def stop_recording():
    return{"00:00:00": "Bookmark Title 1", "01:00:10": "Bookmark Title 2", "00:00:15": "Bookmark Title 3"}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
