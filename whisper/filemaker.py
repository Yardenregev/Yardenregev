from utils.filemanager import FileManager
from utils.recorder import Recorder
from queue import Queue, Empty
from utils.thread_coordinator import ThreadCoordinator
import config

def main(shared_data_holder:Queue, recorder:Recorder, thread_coordinator:ThreadCoordinator):
    base_filename = "recorded_audio"
    file_manager = FileManager(recorder=recorder, base_filename=base_filename)
    file_index = 0
    while not thread_coordinator.shared_exit_flag:
        try:
            data = shared_data_holder.get(timeout=(config.RECORDING_LENGTH + 5))
        except Empty:
            print("queue is empty")
            break
        wav_file_name = file_manager.save_wav_file(data, file_index)
        file_manager.convert_wav_to_mp3(wav_file_name)
        file_manager.delete_file(wav_file_name)
        file_index += 1
    thread_coordinator.running_thread_counter -= 1

