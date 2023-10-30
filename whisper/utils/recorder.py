import pyaudio

class NotEnabledStereoMixException(Exception):
    def __init__(self, message="Please enable stereo mix"):
        super().__init__(message)

class Recorder:
    def __init__(self, chunk=1024,
                    format=pyaudio.paInt16,
                    channels=2, rate=44100, device=None):
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.device = device
        self.stream = None

        self.audio = pyaudio.PyAudio()
    
    def __del__(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        print ("stream terminated")

    def open_stream(self):
        self.stream = self.audio.open(format=self.format,
        channels=self.channels,
        rate=self.rate,
        input=True,
        input_device_index=self.device,
        frames_per_buffer=self.chunk)
    
    def record(self):
        if self.stream is None:
            print("Must open stream first")
            return
        data = self.stream.read(self.chunk)
        return data

    def get_available_devices(self):
        devices = {}
        for i in range(self.audio.get_device_count()):
            dev = self.audio.get_device_info_by_index(i)
            devices[dev['index']] = dev['name']
        return devices
    
    def set_device(self, device_name):
        dev_index = None
        for i in range(self.audio.get_device_count()):
            dev = self.audio.get_device_info_by_index(i)
            if (dev['name'] == device_name and dev['hostApi'] == 0):
                    dev_index = dev['index']
        
        if dev_index is None:
            return False
        self.device = dev_index
        return True
