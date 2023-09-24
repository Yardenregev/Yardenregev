import whisper

class Transcriber():
    def __init__(self, model = "base"):
        self.model = whisper.load_model(model)

    def transcribe(self,file_name):
        result = self.model.transcribe(file_name)
        return result["text"]
