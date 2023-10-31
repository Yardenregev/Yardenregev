import threading
from multiprocessing import Process, Event, Value

from queue import Queue

import models.filemaker as filemaker
import models.record as record
import models.transcribe as transcribe

from utils.recorder import Recorder
from utils.thread_coordinator import ThreadCoordinator
from utils.process_return_obj import ProcessReturnObject

class Excerpta():
    def __init__(self):
        self.thread_coordinator = ThreadCoordinator()

    def start_recording(self, pipe_conn):
        recorder = Recorder()
        shared_data_holder = Queue()
        devices = recorder.get_available_devices()
        device_name = "Stereo Mix (Realtek(R) Audio)"
        ret = recorder.set_device(device_name)
        return_obj = ProcessReturnObject()
        if not ret:
            ret_message = "Failed to find device " + device_name
            return_obj.status = False
            return_obj.message = ret_message
            pipe_conn.send(return_obj)
            pipe_conn.close()
        else:
            ret_message = "Recording started successfully"
            return_obj.status = True
            return_obj.message = ret_message

            pipe_conn.send(return_obj)
            pipe_conn.close()


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
