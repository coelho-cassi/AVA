import whisper

filein = "vocals.wav"
model = whisper.load_model("small")
result = model.transcribe(filein)

import json
with open("result_whisper.txt", "w") as file:
    file.write(json.dumps(result, indent = 2, ensure_ascii = False))