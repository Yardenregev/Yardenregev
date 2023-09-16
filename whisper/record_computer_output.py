import pyaudio
import wave
from pydub import AudioSegment

# Configure audio settings
audio_format = pyaudio.paInt16
channels = 2
sample_rate = 44100
chunk = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

for i in range(audio.get_device_count()):
    dev = audio.get_device_info_by_index(i)
    if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
        dev_index = dev['index'];
        print('dev_index', dev_index)

# Open an audio stream
stream = audio.open(format=audio_format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    input_device_index=dev_index,
                    frames_per_buffer=chunk)

# Create an empty list to store audio data
frames = []

# Record audio for a specified duration (in seconds)
duration = 10  # Adjust this value to control recording duration

for _ in range(0, int(sample_rate / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the audio stream
stream.stop_stream()
stream.close()

# Terminate the PyAudio instance
audio.terminate()

# Save the recorded audio as a WAV file
output_wav_file = "output.wav"
with wave.open(output_wav_file, 'wb') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(audio_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))

# Load the WAV file and convert it to MP3
output_mp3_file = "output.mp3"
audio = AudioSegment.from_wav(output_wav_file)
audio.export(output_mp3_file, format="mp3")

print("Audio recording saved as MP3:", output_mp3_file)
