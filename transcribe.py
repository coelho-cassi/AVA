import whisper

filein = "vocals.wav"
fileout = "lyrics.txt"

model = whisper.load_model("small")
result = model.transcribe(filein)    # takes ~5mins
output = open(fileout, "w")
output.write(result["text"])
output.close()