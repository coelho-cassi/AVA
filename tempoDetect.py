import sys
import librosa

#*****************************************************************************************************************************************************
# CS-4390 Senior Project : AVA Software
# Tempo Detection Program
# author: Jakob Childers
# verison: 10/27/2022
# 
#
# Input Arguements:
#   file can be ran in the CML one of two ways:
#          (1) python tempoDetect_2.py sample.mp3
#                   - sample.mp3 is the exact name of the mp3 file in the local directory
#                   - this will return the estimate BPM of the entire sample
#          (2) python tempoDetect_2.py sample.mp3 startingPoint duration 
#                   - sample.mp3 is the exact name of the mp3 file in the local directory
#                   - startingPoint is the starting point in seconds where the start the BPM analysis (0 can be specified to start at the beginning)
#                   - duration is the length in seconds that the sample should be processed starting at the startingPoint position.
#
#   NOTES:
#       review Notes.txt for detailed testing
#       Try/Catch statements needed in case of invalid path
#
# Dependencies:
# sys library - arguements
# librosa lib - BPM Detection
# librosa pip install  (type the command in the CML: pip install librosa)
#
#*****************************************************************************************************************************************************

def main():
    if len(sys.argv) == 2:
        tempo = detect_tempo(sys.argv[1])
        print(tempo)
    elif len(sys.argv) == 4:
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        tempo = detect_tempo(sys.argv[1],x,y);
        print(tempo)
    else:
        print("Invalid Parameter Format.")

def detect_tempo(audioString, startingPoint=None, length=None): # starting/ending point are measured in seconds
    if (startingPoint == None or length == None):
        y, sr = librosa.load(audioString)
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
    else:
        y, sr = librosa.load(audioString, offset=startingPoint,duration=length) # Starting at offset, load duration length
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
    return tempo

if __name__ == '__main__':
    main();
