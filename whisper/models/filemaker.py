from multiprocessing import Event

from utils.filemanager import FileManager
from utils.recorder import Recorder
from queue import Queue, Empty
from utils.thread_coordinator import ThreadCoordinator
import configs.config as config

def main(shared_data_holder:Queue, recorder:Recorder, thread_coordinator:ThreadCoordinator, event:Event):
    base_filename = "recorded_audio"
    file_manager = FileManager(recorder=recorder, base_filename=base_filename)
    file_index = 0
    file_count = 0
    while not thread_coordinator.shared_exit_flag.value:
        try:
            data = shared_data_holder.get(timeout=(config.RECORDING_LENGTH + 5))
        except Empty:
            print("queue is empty")
            break
        wav_file_name = file_manager.save_wav_file(data, file_index)
        try:
            file_manager.convert_wav_to_mp3(wav_file_name)
        except:
            file_manager.delete_file(wav_file_name)
            break
        file_manager.delete_file(wav_file_name)
        file_count += 1
        file_index += 1
        if file_count == config.FILE_COUNT_MINIMUM_BEFORE_TRANSCRIPTION:
            file_count -= 1
            event.set()
            print("event set")
    thread_coordinator.running_thread_counter -= 1
    event.set()

