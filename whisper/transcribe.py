from utils.transcriber import Transcriber
from utils.filemanager import FileManager

file_index = 0
file_manager = FileManager()
transcriber = Transcriber("base")
while True:
    try:
        file_name = f"recorded_audio_{file_index}.mp3"
        if not file_manager.exists(file_name):
            break
        transcript = transcriber.transcribe(file_name)
        file_manager.write_file(f"transcription_{file_index}.txt", transcript)
        file_manager.delete_file(file_name)
        file_index += 1
    except Exception as e:
        print("Error while transcribing ", str(e))
        break
print("Finished Transcribing!")