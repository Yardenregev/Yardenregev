import pyaudio
import wave
from pydub import AudioSegment
from utils.recorder import Recorder
import os

class FileManager():

    def __init__(self, recorder:Recorder = None, base_filename:str = None):
        if recorder is not None:
            self.channels = recorder.channels
            self.format = recorder.format
            self.rate = recorder.rate
        if base_filename is not None:
            self.base_filename = base_filename
    
    def save_wav_file(self, frames, file_counter):
        wav_file_name = f"{self.base_filename}_{file_counter}.wav"
        with wave.open(wav_file_name, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
        return wav_file_name
    
    def convert_wav_to_mp3(self,wav_file_name):
        mp3_file_name = wav_file_name.split('.')[0]
        mp3_filename = mp3_file_name + ".mp3"
        print(mp3_filename)
        audio = AudioSegment.from_wav(wav_file_name)
        audio.export(mp3_filename, format="mp3")

    def delete_file(self, file_to_delete):
        os.remove(file_to_delete)

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w') as f:
                f.write(content)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
    
    def exists(self, file_path):
        return os.path.exists(file_path)

    