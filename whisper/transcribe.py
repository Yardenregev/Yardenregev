import config
from utils.transcriber import Transcriber
from utils.filemanager import FileManager
from utils.timestamps import TimeStamps
file_index = 0
file_manager = FileManager()
transcriber = Transcriber("base")
timestamps = TimeStamps()
while True:
    try:
        file_name = f"recorded_audio_{file_index}.mp3"
        if not file_manager.exists(file_name):
            break
        transcript = transcriber.transcribe(file_name)
        timestamps.insert(transcript)
        # file_manager.write_file(f"transcription_{file_index}.txt", transcript)
        file_manager.delete_file(file_name)
        file_index += 1
        timestamps.increase_time(config.RECORDING_LENGTH)
    except Exception as e:
        print("Error while transcribing ", str(e))
        break
print("Finished Transcribing!")
file_manager.write_json_file("timestamps.json", timestamps.data)