import threading
import signal
from queue import Queue

import filemaker
import record


from utils.recorder import Recorder
from utils.thread_coordinator import ThreadCoordinator

thread_coordinator = ThreadCoordinator()

# Define a signal handler to set the shared flag when Ctrl+C is pressed
def signal_handler(sig, frame):
    print("Interrupt signal received. Exiting gracefully.")
    global thread_coordinator
    thread_coordinator.shared_exit_flag = True


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    recorder = Recorder()
    shared_data_holder = Queue()
    devices = recorder.get_available_devices()
    device_name = "Stereo Mix (Realtek(R) Audio)"
    ret = recorder.set_device(device_name)
    if not ret:
        print("Failed to find device ", device_name)
    else:
        record_thread = threading.Thread(target=record.main,args=[shared_data_holder,recorder, thread_coordinator],daemon=True)
        filemaker_thread = threading.Thread(target=filemaker.main,args=[shared_data_holder,recorder, thread_coordinator], daemon=True)

        
        record_thread.start()
        thread_coordinator.running_thread_counter += 1
        filemaker_thread.start()
        thread_coordinator.running_thread_counter += 1
        while thread_coordinator.running_thread_counter > 0:
            pass

        print("All threads finished")