from models.excerpta import Excerpta
from multiprocessing import Process

if __name__ == '__main__':
    recording_running = False
    recording_process = None
    excerpta = Excerpta()

    while True:
        inp = input("enter 's' to start recording and 't' to stop recording and 'e' to exit\n")
        if inp == 's':
            if not recording_running:
                print("Starting recording")
                recording_process = Process(target=excerpta.start_recording)
                recording_process.start()
                recording_running = True
            else:
                print("Recording already started")

        elif inp == 't':
            if not recording_running:
                print("Recording not running")
            else:
                print("Stopping recording")
                excerpta.stop_recording()
                recording_process.join()

        elif inp == 'e':
            print("Goodbye")
            break