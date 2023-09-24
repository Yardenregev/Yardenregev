import signal
import traceback

from utils.recorder import Recorder
from utils.filemanager import FileManager
from utils.dataholder import DataHolder

FRAMES_PER_SECOND = 44

def record_and_save_audio(recorder, file_manager):

    def signal_handler(sig, frame):
        print("Recording stopped by user (Ctrl+C)")
        nonlocal recording
        recording = False

    signal.signal(signal.SIGINT, signal_handler)

    print("Recording... Press Ctrl+C to stop.")

    data_holder = DataHolder(chunk_size=(FRAMES_PER_SECOND * 10))
    
    recording = True

    try:
        while recording:
            data = recorder.record()
            data_holder.append(data)

    except KeyboardInterrupt:
        pass


    number_of_chunks = data_holder.get_number_of_chunks()
    for chunk_index in range(number_of_chunks):
        chunk_data = data_holder.get_data(chunk_index)
        wav_file_name = file_manager.save_wav_file(chunk_data, chunk_index)
        file_manager.convert_wav_to_mp3(wav_file_name)
        file_manager.delete_file(wav_file_name)

    print("Finished recording!")

if __name__ == "__main__":
    base_filename = "recorded_audio"
    recorder = Recorder()
    file_manager = FileManager(recorder=recorder, base_filename=base_filename)
    devices = recorder.get_available_devices()
    device_name = "Stereo Mix (Realtek(R) Audio)"
    ret = recorder.set_device(device_name)
    if not ret:
        print("Failed to find device ", device_name)
    else:
        recorder.open_stream()
        try:
            record_and_save_audio(recorder, file_manager)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            traceback.print_exc()


    