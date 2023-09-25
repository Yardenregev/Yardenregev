from utils.filemanager import FileManager
from utils.dataholder import DataHolder
from shared_data import shared_exit_flag

def main(shared_data_holder:DataHolder, recorder):
    base_filename = "recorded_audio"
    file_manager = FileManager(recorder=recorder, base_filename=base_filename)
    file_index = 0
    while not shared_exit_flag.is_set():
        data = shared_data_holder.get()
        print("got frames")
        wav_file_name = file_manager.save_wav_file(data, file_index)
        file_manager.convert_wav_to_mp3(wav_file_name)
        file_manager.delete_file(wav_file_name)
        file_index += 1


