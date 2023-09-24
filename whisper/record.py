import pyaudio
import wave
from pydub import AudioSegment
import tempfile
import os
import signal
import time

from utils.recorder import Recorder
from utils.filemanager import FileManager

def record_and_save_audio(recorder, file_manager, duration_seconds=10):

    def signal_handler(sig, frame):
        print("Recording stopped by user (Ctrl+C)")
        nonlocal recording
        recording = False

    signal.signal(signal.SIGINT, signal_handler)

    print("Recording... Press Ctrl+C to stop.")
    frames = []
    recording = True
    start_time = time.time()
    file_counter = 0

    try:
        while recording:
            recorder.record(frames)
    except KeyboardInterrupt:
        pass

    # Save any remaining audio data
    if frames:
        wav_file_name = file_manager.save_wav_file(frames, file_counter)
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
            record_and_save_audio(recorder, file_manager, duration_seconds=3)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    