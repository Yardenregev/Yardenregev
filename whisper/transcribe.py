import whisper
import os
model = whisper.load_model("base")
file_index = 1
while True:
    try:
        file_name = f"recorded_audio_{file_index}.mp3"
        result = model.transcribe(file_name)
        print(result["text"])
        os.remove(file_name)
        file_index += 1
    except Exception as e:
        print("Error while transcribing ", str(e))
        break
print("Finished Transcribing")