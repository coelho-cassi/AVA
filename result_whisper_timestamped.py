#pip3 install git+https://github.com/linto-ai/whisper-timestamped

import whisper_timestamped as whisper

filein = "vocals.wav"
model = whisper.load_model("small")
result = whisper.transcribe(model, filein)

import json
with open("result_whisper_timestamped.txt", "w") as file:
    file.write(json.dumps(result, indent = 2, ensure_ascii = False))