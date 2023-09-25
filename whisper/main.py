import threading
import signal

import filemaker
import record


from utils.recorder import Recorder
from utils.dataholder import DataHolder

from shared_data import shared_exit_flag

# Define a signal handler to set the shared flag when Ctrl+C is pressed
def signal_handler(sig, frame):
    print("Interrupt signal received. Exiting gracefully.")
    shared_exit_flag.set()



if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    recorder = Recorder()
    shared_data_holder = DataHolder()
    devices = recorder.get_available_devices()
    device_name = "Stereo Mix (Realtek(R) Audio)"
    ret = recorder.set_device(device_name)
    if not ret:
        print("Failed to find device ", device_name)
    else:
        record_thread = threading.Thread(target=record.main,args=(shared_data_holder,recorder))
        filemaker_thread = threading.Thread(target=filemaker.main,args=(shared_data_holder,recorder))

        record_thread.start()
        filemaker_thread.start()

        record_thread.join()
        filemaker_thread.join()

        print("All threads finished")