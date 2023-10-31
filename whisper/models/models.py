import json
import os

from http import HTTPStatus
from flask import Response
from multiprocessing import Process, Pipe

from models.excerpta import Excerpta
from utils.process_return_obj import ProcessReturnObject

class ExcerptaModel:
    def __init__(self):
        self.recording_running = False
        self.recording_process = None
        self.excerpta = Excerpta()

    def start_recording(self):
        if not self.recording_running:
            parent_conn, child_conn = Pipe()
            self.recording_process = Process(target=self.excerpta.start_recording, args=(child_conn,))
            self.recording_process.start()
            self.recording_running = True
            return_object = parent_conn.recv()
            return_object:ProcessReturnObject
            status = HTTPStatus.OK
            if return_object.status == False:
                self.recording_process.join()
                status = HTTPStatus.BAD_REQUEST
                self.recording_running = False
            return Response(status=status, response=return_object.message)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST,response="Recording already in progress")

    def stop_recording(self):    
        if not self.recording_running:
            return Response(status=HTTPStatus.BAD_REQUEST, response="No recording running")
        else:
            self.excerpta.stop_recording()
            self.recording_process.join()
            self.recording_running = False
            try:
                current_directory = os.path.dirname(os.path.abspath(__file__ ))
                file_path = os.path.join(current_directory, '..', 'models','timestamps.json')
                print("file path: " + file_path)
                with open(file_path, 'r') as timestamps_file:
                    data = json.load(timestamps_file)
                    return Response(status=HTTPStatus.OK, response=json.dumps(data))
            except FileNotFoundError:
                return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR, response="Something went wrong with making timestamps.json")
