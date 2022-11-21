import sys
import librosa

#*****************************************************************************************************************************************************
# CS-4390 Senior Project : AVA Software
# Tempo Detection Program
# author: Jakob Childers
# verison: 11/13/2022
# 
#
# Input Arguements:
#   file can be ran in the CML one of two ways:
#          (1) python tempoDetect.py sample.mp3
#                   - sample.mp3 is the exact name of the mp3 file in the local directory
#                   - this will return the estimate BPM of the entire sample
#          (2) python tempoDetect.py sample.mp3 startingPoint duration 
#                   - sample.mp3 is the exact name of the mp3 file in the local directory
#                   - startingPoint is the starting point in seconds where the start the BPM analysis (0 can be specified to start at the beginning)
#                   - duration is the length in seconds that the sample should be processed starting at the startingPoint position.
#
#   file can be ran from another python script by doing the following:
#          As long as the script is within the current directory add "import tempoDetect" at the top.
#          
#          To run the program use the function detect_tempo() which will return a array with the BPM value.
#           examples:
#
#               # Using the function to determine the BPM for a specific interval of the music
#               # Refer to the above definitions for startingPoint and duration. 
#               BPM = tempoDetect.detect_tempo('example.mp3', startingPoint, duration)
#               print(BPM[0]) # this will print the BPM value
#
#               # Using the function to determine the avg BPM of the entire song
#               BPM = tempoDetect.detect_tempo('example.mp3')
#
# Dependencies:
# sys library - arguements
# librosa lib - BPM Detection
# librosa pip install  (type the command in the CML: pip install librosa)
#
#*****************************************************************************************************************************************************

# Main is only ran if the script is called via the command line
# Precondition  : 
#       Script must be called with the either of the following arguements:
#           (1)    python tempoDetect.py example.mp3
#           (2)    python tempoDetect.py example.mp3 startingPoint duration
#       NOTE:
#           - Both startingPoint and duration must be Numerical types. 
#             startingPoint must be less than the total length of the audio file
#           - duration can not be zero
#           - The order of the arguements must be like it is stated above, 
# Postcondition :
#       This function will print one of the following to the console:
#           (1) An Array with the BPM value as the first entry. 
#           (2) An Array with a string as the first entry indicating that
#               the given .mp3 string was invalid (FILE NOT FOUND ERROR)
def main():
    if len(sys.argv) == 2: # Only mp3 file is 
        tempo = detect_tempo(sys.argv[1])
        print(tempo)
    elif len(sys.argv) == 4:
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        tempo = detect_tempo(sys.argv[1],x,y);
        print(tempo)
    else:
        print("Invalid Parameter Format.")

# detect_tempo is ran if the script is called via a outside script or by the main method.
# Precondition  : 
#       Function must be called with the either of the following arguements:
#           (1)    detect_tempo(audioString)
#           (2)    detect_tempo(audioString, startingPoint, duration)
#       NOTE:
#           - Both startingPoint and duration must be Numerical types. 
#             startingPoint must be less than the total length of the audio file
#           - duration can not be zero
#           - The order of the arguements must be like it is stated above, 
# Postcondition :
#       This function will return one of the following:
#           (1) An Array with the BPM value as the first entry. 
#           (2) An Array with a string as the first entry indicating that
#               the given .mp3 string was invalid (FILE NOT FOUND ERROR)
def detect_tempo(audioString, startingPoint=None, length=None): # starting/ending point are measured in seconds
    try:
        if (startingPoint == None or length == None):
            # Uses the librosa library to load the music file and determine BPM
            try:
                y, sr = librosa.load(audioString)
                onset_env = librosa.onset.onset_strength(y=y,sr=sr)
                tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
            except ValueError:
                y, sr = librosa.load(audioString,sr=None)
                onset_env = librosa.onset.onset_strength(y=y,sr=sr)
                tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        else:
            try:
                # Starting at offset, load duration length
                y, sr = librosa.load(audioString, offset=startingPoint,duration=length)
                onset_env = librosa.onset.onset_strength(y=y,sr=sr)
                tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
            except ValueError:
                y, sr = librosa.load(audioString, offset=startingPoint,duration=length, sr=None)
                onset_env = librosa.onset.onset_strength(y=y,sr=sr)
                tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        return tempo
    except FileNotFoundError:
        retStr = 'Invalid FileName Given'
        tempo = [retStr]
        return tempo

if __name__ == '__main__':
    main();
