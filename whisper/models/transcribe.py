import os
from multiprocessing import Event, Value
# import signal

import configs.config as config
from utils.transcriber import Transcriber
from utils.filemanager import FileManager
from utils.timestamps import TimeStamps
from utils.thread_coordinator import ThreadCoordinator

# # Define a signal handler to set the shared flag when Ctrl+C is pressed
# def signal_handler(sig, frame):
#     print("transcribe.py received sig")

def main(event:Event, flag:Value):
    # signal.signal(signal.SIGINT, signal_handler)
    file_index = 0
    file_manager = FileManager()
    transcriber = Transcriber("base")
    timestamps = TimeStamps()
    while True:
        try:
            print("Transcribe wait, flag value is", flag.value)
            if flag.value != 1:
                event.wait()
                event.clear()
            print("Transcribe release")
            file_name = f"recorded_audio_{file_index}.mp3"
            if not file_manager.exists(file_name):
                break
            try:
                print("transcribing", file_name)
                transcript = transcriber.transcribe(file_name)
            except KeyboardInterrupt:
                pass
            timestamps.insert(transcript)
            file_manager.delete_file(file_name)
            file_index += 1
            timestamps.increase_time(config.RECORDING_LENGTH)
        except Exception as e:
            print("Error while transcribing ", str(e))
            if file_manager.exists(file_name):
                file_manager.delete_file(file_name)
            break
    print("Finished Transcribing!")
    current_directory = os.path.dirname(os.path.abspath(__file__ ))
    file_path = os.path.join(current_directory,"timestamps.json")
    print("transcriber file path",file_path)
    file_manager.write_json_file(file_path, timestamps.data)