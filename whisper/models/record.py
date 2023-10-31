import traceback
from queue import Queue
import configs.config as config

from utils.recorder import Recorder

from utils.thread_coordinator import ThreadCoordinator

def record_and_save_audio(recorder:Recorder, shared_data_holder:Queue, thread_coordinator:ThreadCoordinator):

    print("Recording...")

    chunk_size = config.FRAMES_PER_SECOND * config.RECORDING_LENGTH
    frames = []
    try:
        while not thread_coordinator.shared_exit_flag.value:
            if len(frames) >= chunk_size:
                shared_data_holder.put(frames)
                frames = []
            data = recorder.record()
            frames.append(data)

    except KeyboardInterrupt:
        pass
    
    print("Finished recording!")
    thread_coordinator.running_thread_counter -= 1
# if __name__ == "__main__":
def main(shared_data_holder:Queue, recorder:Recorder, thread_coordinator:ThreadCoordinator):
    recorder.open_stream()
    try:
        record_and_save_audio(recorder, shared_data_holder, thread_coordinator)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()


    