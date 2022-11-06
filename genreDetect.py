import sys
import librosa
import math
#*****************************************************************************************************************************************************
# CS-4390 Senior Project : AVA Software
# Genre Detection Program
# author: Jakob Childers
# verison: 11/06/2022
#
# Input Arguements:
#   python genreDetect.py [example1.mp3] [interval_length] 
#       - example1.mp3 is the mp3 file that is going to be analyzed
#       - interval_length is the length of seconds that the program will make each seqment of audio. A lower value may yield more accurate results. 
#         
# Dependencies:
# sys library - arguements
# librosa lib - BPM Detection
# librosa pip install  (type the command in the CML: pip install librosa)
# math library - Floor function
#*****************************************************************************************************************************************************

def main():
    if len(sys.argv) == 3:
        song = sys.argv[1]
        interval_length = int(sys.argv[2])
    else:
        print("Invalid Number of Arguments")
        quit()
    
    tempoList = []
    y, sr = librosa.load(song)
    x = librosa.get_duration(y=y,sr=sr)
    print("Total Length: ", x)
    x1 = math.floor(x)
    a = math.floor(x1 / interval_length)            # Determines the number of seqments
    b = x1 % interval_length                        # Determines the length of the final seqment  
                                                    # NOTE: (a*interval_length + b) = total length of mp3
                                                    
    print("Number of seqments : ", a,"\nExcess :", b, "seconds")
    for i in range(1,a+1):
        temp = i*interval_length
        y, sr = librosa.load(song, offset=temp,duration=30)
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        tempoList.append(tempo[0])
    y, sr = librosa.load(song, offset=temp, duration=b)
    onset_env = librosa.onset.onset_strength(y=y,sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
    tempoList.append(tempo[0])
    #print(tempoList)
    nodups = [*set(tempoList)]
    print("List of BPM Values with Duplicates removed : \n", nodups)
    tempoList = genreClassification(nodups)
    print("Probable Genres:")
    for i in tempoList:
        print(i)
    
def genreClassification(BPM_List):
    genreDict = {
        "Blues": 0,
        "Classical": 0,
        "Country": 0,
        "HipHop": 0,
        "Jazz": 0,
        "Metal": 0,
        "Pop": 0,
        "Rock": 0}
    genreList = ["  Blues     : ",
                 "  Classical : ",
                 "  Country   : ",
                 "  HipHop    : ",
                 "  Jazz      : ",
                 "  Metal     : ",
                 "  Pop       : ",
                 "  Rock      : "]
    arrLen = len(BPM_List)
    for i in range(0,arrLen):
        ft = BPM_List[i]
        if ft >= 40 and ft <= 100:
            genreDict["Blues"] += 1
        if ft >= 120 and ft <= 140:
            genreDict["Classical"] += 1
        if ft >= 60 and ft <= 100:
            genreDict["Country"] += 1
        if ft >= 85 and ft <= 115:
            genreDict["HipHop"] += 1
        if ft >= 120 and ft <= 125:
            genreDict["Jazz"] += 1
        if ft >= 100 and ft <= 160:
            genreDict["Metal"] += 1
        if ft >= 100 and ft <= 130:
            genreDict["Pop"] += 1
        if ft >= 110 and ft <= 140:
            genreDict["Rock"] += 1
    # Adding Blues Probability
    temp = math.floor(((genreDict["Blues"] / arrLen) * 100))
    genreList[0] += str(temp) + '%'
        
    # Adding Classical Probability
    temp = math.floor(((genreDict["Classical"] / arrLen) * 100))
    genreList[1] += str(temp) + '%'
        
    # Adding Country Probability
    temp = math.floor(((genreDict["Country"] / arrLen) * 100))
    genreList[2] += str(temp) + '%'
     
    #Adding HipHop Probability
    temp = math.floor(((genreDict["HipHop"] / arrLen) * 100))
    genreList[3] += str(temp) + '%'
       
    #Adding Jazz Probability
    temp = math.floor(((genreDict["Jazz"] / arrLen) * 100))
    genreList[4] += str(temp) + '%'
      
    #Adding Metal Probability
    temp = math.floor(((genreDict["Metal"] / arrLen) * 100))
    genreList[5] += str(temp) + '%'
      
    #Adding Pop Probability
    temp = math.floor(((genreDict["Pop"] / arrLen) * 100))
    genreList[6] += str(temp) + '%'
        
    #Adding Rock Probability
    temp = math.floor(((genreDict["Rock"] / arrLen) * 100))
    genreList[7] += str(temp) + '%'
    return genreList
if __name__ == '__main__':
    main();
