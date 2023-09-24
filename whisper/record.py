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
    # CHUNK = 1024
    # FORMAT = pyaudio.paInt16
    # CHANNELS = 2
    # RATE = 44100

    # audio = pyaudio.PyAudio()

    # dev_index = None
    # for i in range(audio.get_device_count()):
    #     dev = audio.get_device_info_by_index(i)
    #     if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
    #         dev_index = dev['index']
    #         print('dev_index', dev_index)

    # if dev_index is None:
    #     raise NotEnabledStereoMixException() 

    def signal_handler(sig, frame):
        print("Recording stopped by user (Ctrl+C)")
        nonlocal recording
        recording = False

    signal.signal(signal.SIGINT, signal_handler)

    # stream = audio.open(format=FORMAT,
    #                     channels=CHANNELS,
    #                     rate=RATE,
    #                     input=True,
    #                     input_device_index=dev_index,
    #                     frames_per_buffer=CHUNK)

    print("Recording... Press Ctrl+C to stop.")
    frames = []
    recording = True
    start_time = time.time()
    file_counter = 0

    try:
        while recording:
            # data = stream.read(CHUNK)
            # frames.append(data)
            recorder.record(frames)
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration_seconds:
                # print("frame count is", len(frames) )
                start_time = time.time()
                wav_file_name = file_manager.save_wav_file(frames, file_counter)
                file_manager.convert_wav_to_mp3(wav_file_name)
                file_manager.delete_file(wav_file_name)
                # save_audio(frames, base_filename, file_counter, CHANNELS, FORMAT, RATE)
                # save_audio(frames, base_filename, file_counter, recorder.channels, recorder.format, recorder.rate)
                frames = []
                file_counter += 1
    except KeyboardInterrupt:
        pass

    # Save any remaining audio data
    if frames:
        # save_audio(frames, base_filename, file_counter, recorder.channels, recorder.format, recorder.rate)
        wav_file_name = file_manager.save_wav_file(frames, file_counter)
        file_manager.convert_wav_to_mp3(wav_file_name)
        file_manager.delete_file(wav_file_name)

    print("Finished recording!")

    # stream.stop_stream()
    # stream.close()
    # audio.terminate()

def save_audio(frames, base_filename, file_counter, channels, format, rate):
    temp_wav_file = f"{base_filename}_{file_counter}.wav"
    with wave.open(temp_wav_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    
    temp_mp3_file = f"{base_filename}_{file_counter}.mp3"
    convert_wav_to_mp3(temp_wav_file, temp_mp3_file)
    print(f"Saved {temp_mp3_file}")
    # Delete the temporary WAV file
    os.remove(temp_wav_file)


def convert_wav_to_mp3(wav_filename, mp3_filename):
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")

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

    