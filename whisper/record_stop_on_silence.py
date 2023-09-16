import pyaudio
import wave
from pydub import AudioSegment
import array
import os
import signal
import time
import webrtcvad
import numpy as np

class NotEnabledStereoMixException(Exception):
    def __init__(self, message="Please enable stereo mix"):
        super().__init__(message)
def calculate_energy(audio_data):
    # Calculate the energy of the audio data
    return np.sum(np.square(audio_data))

def record_and_save_audio(base_filename):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    audio = pyaudio.PyAudio()

    dev_index = None
    for i in range(audio.get_device_count()):
        dev = audio.get_device_info_by_index(i)
        if dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0:
            dev_index = dev['index']
            print('dev_index', dev_index)

    if dev_index is None:
        raise NotEnabledStereoMixException()

    def signal_handler(sig, frame):
        print("Recording stopped by user (Ctrl+C)")
        nonlocal recording
        recording = False

    signal.signal(signal.SIGINT, signal_handler)

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=dev_index,
                        frames_per_buffer=CHUNK)

    print("Recording... Press Ctrl+C to stop.")
    frames = []
    recording = True
    silence_started = None
    file_index = 0
    try:
        while recording:
            data = stream.read(CHUNK)
            frames.append(data)

            # Convert binary audio data to NumPy array of int16
            audio_samples = np.frombuffer(data, dtype=np.int16)

            # Calculate energy of audio samples
            energy = calculate_energy(audio_samples)

            # You can adjust this threshold as needed
            silence_threshold = 100000  # Adjust this value as needed

            if energy < silence_threshold:
                silence_started = silence_started or time.time()
            else:
                silence_started = None

            # Save audio if silence exceeds 3 seconds
            if silence_started and time.time() - silence_started >= 1.2:
                filename = base_filename + '_' + str(file_index)
                save_audio(frames, filename)
                file_index += 1
                frames = []
    except KeyboardInterrupt:
        pass

    # Save any remaining audio data
    if frames:
        filename = base_filename + '_' + str(file_index)
        save_audio(frames, filename)

    print("Finished recording!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

def save_audio(frames, filename):
    temp_wav_file = f"{filename}.wav"
    with wave.open(temp_wav_file, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

    temp_mp3_file = f"{filename}.mp3"
    convert_wav_to_mp3(temp_wav_file, temp_mp3_file)
    print(f"Saved {temp_mp3_file}")
    # Delete the temporary WAV file
    os.remove(temp_wav_file)

def convert_wav_to_mp3(wav_filename, mp3_filename):
    audio = AudioSegment.from_wav(wav_filename)
    audio.export(mp3_filename, format="mp3")

if __name__ == "__main__":
    base_filename = "recorded_audio"
    try:
        record_and_save_audio(base_filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
