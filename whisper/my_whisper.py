import threading
from multiprocessing import Process, Event, Value

import signal
from queue import Queue

import filemaker
import record
import transcribe

from utils.recorder import Recorder
from utils.thread_coordinator import ThreadCoordinator



# # Define a signal handler to set the shared flag when Ctrl+C is pressed
# def signal_handler(sig, frame):
#     print("Interrupt signal received. Exiting gracefully.")
#     global thread_coordinator
#     thread_coordinator.shared_exit_flag = True

class Whisper():
    def __init__(self):
        self.thread_coordinator = ThreadCoordinator()

    def start_recording(self):
        recorder = Recorder()
        shared_data_holder = Queue()
        devices = recorder.get_available_devices()
        device_name = "Stereo Mix (Realtek(R) Audio)"
        ret = recorder.set_device(device_name)
        if not ret:
            print("Failed to find device ", device_name)
        else:
            event = Event()
            record_thread = threading.Thread(target=record.main,args=[shared_data_holder,recorder, self.thread_coordinator],daemon=True)
            filemaker_thread = threading.Thread(target=filemaker.main,args=[shared_data_holder,recorder, self.thread_coordinator, event], daemon=True)

            
            record_thread.start()
            self.thread_coordinator.running_thread_counter += 1
            filemaker_thread.start()
            self.thread_coordinator.running_thread_counter += 1
            
            flag = Value("i",0)
            p = Process(target=transcribe.main, args=[event, flag])
            p.start()

            while self.thread_coordinator.running_thread_counter > 0:
                pass

            print("All threads finished")
            event.set()
            flag.value = 1
            p.join()
    
    def stop_recording(self):
        self.thread_coordinator.shared_exit_flag.value = 1
