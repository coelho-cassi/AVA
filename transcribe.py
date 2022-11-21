import whisper

filein = "audio_output/Radiohead_Spectre/vocals.wav"
fileout = "audio_output/Radiohead_Spectre/lyrics.txt"

model = whisper.load_model("small")
result = model.transcribe(filein, fp16=False, language = 'English')    # takes ~5mins
print(result["text"])
output = open(fileout, "w")
output.write(result["text"].strip())
output.close()