import json

from flask import Flask, Response
from my_whisper import Whisper
from multiprocessing import Process, Pipe

app = Flask(__name__)

recording_running = False
recording_process = None
whisper = Whisper()

@app.route("/Record/Start",methods=["POST"])
def start_recording():
    global recording_running
    global recording_process
    global whisper

    if not recording_running:
        parent_conn, child_conn = Pipe()
        recording_process = Process(target=whisper.start_recording, args=(child_conn,))
        recording_process.start()
        recording_running = True
        ret_obj = parent_conn.recv()
        status = 200
        if ret_obj[0] == 0:
            recording_process.join()
            status = 400
        return Response(status=status, response=ret_obj[1])
    else:
        return "Recording already in progress"

@app.route("/Record/Stop",methods=["GET"])
def stop_recording():
    global recording_running
    global recording_process
    global whisper
    
    if not recording_running:
        return Response(status=400, response="No recording running")
    else:
        whisper.stop_recording()
        recording_process.join()
        try:
            with open('../timestamps.json', 'r') as timestamps_file:
                data = json.load(timestamps_file)
                return Response(status=200, response=data)
        except FileNotFoundError:
            return Response(status=500, response="Something went wrong with making timestamps.json")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
