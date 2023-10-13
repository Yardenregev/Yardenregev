import traceback
from queue import Queue
import config

from utils.recorder import Recorder

from shared_data import shared_exit_flag as exit_flag

def record_and_save_audio(recorder:Recorder, shared_data_holder:Queue):

    print("Recording... Press Ctrl+C to stop.")

    chunk_size = config.FRAMES_PER_SECOND * config.RECORDING_LENGTH
    frames = []
    try:
        while not exit_flag:
            if len(frames) >= chunk_size:
                shared_data_holder.put(frames)
                frames = []
            data = recorder.record()
            frames.append(data)

    except KeyboardInterrupt:
        pass

    print("Finished recording!")

# if __name__ == "__main__":
def main(shared_data_holder:Queue, recorder:Recorder):
    recorder.open_stream()
    try:
        record_and_save_audio(recorder, shared_data_holder)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()


    