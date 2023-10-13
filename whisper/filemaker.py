from utils.filemanager import FileManager
from utils.recorder import Recorder
from queue import Queue
from shared_data import shared_exit_flag as exit_flag

def main(shared_data_holder:Queue, recorder:Recorder):
    print("got shared data holder", shared_data_holder)
    base_filename = "recorded_audio"
    file_manager = FileManager(recorder=recorder, base_filename=base_filename)
    file_index = 0
    while not exit_flag:
        data = shared_data_holder.get()
        wav_file_name = file_manager.save_wav_file(data, file_index)
        file_manager.convert_wav_to_mp3(wav_file_name)
        file_manager.delete_file(wav_file_name)
        file_index += 1


