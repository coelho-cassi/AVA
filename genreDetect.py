import sys
import librosa
import math
#*****************************************************************************************************************************************************
# CS-4390 Senior Project : AVA Software
# Genre Detection Program
# author: Jakob Childers
# verison: 11/13/2022
#
# Input Arguements:
#   file can be ran in the CML by running the following command:
#           python genreDetect.py [example1.mp3] [interval_length] 
#               - example1.mp3 is the mp3 file that is going to be analyzed
#               - interval_length is the length of seconds that the program will make each seqment of audio. 
#                  NOTE: A lower value may yield more accurate results. 
#
#   file can be ran from another python script by doing the following:
#           As long as the script is within the current directory add "import genreDetect" at the top.
#
#           To run the program, simply call the execute() function which will return a list containing each Genre's Probability
#             Examples:
#                    (1) genreList1 = genreDetect.execute('example1.mp3',30) # Splits example1.mp3 into 30 second seqments
#                 
#                    (2) genreList2 = genreDetect.execute('example2.mp3',15) # Splits example2.mp3 into 15 second seqments
#           NOTE:
#               - If analysis is successful, then the returned list will be exactly 8 values long. Each index of the list 
#                 is a string containing a genre with the calculated probability.
#               - If analysis is unsucessful, then the returned list will be exactly 1 value long. The value will be a string
#                 explaining the error message or unknown genre. (BPM values did not match any range) 
#               - interval length can not be zero.
#
# Dependencies:
# sys library - arguements
# librosa lib - BPM Detection
# librosa pip install  (type the command in the CML: pip install librosa)
# math library - Floor function
#*****************************************************************************************************************************************************

# Main is only ran if the script is called via the command line
# Precondition  : 
#       Script must be called with the following arguements:
#           (1)    python genreDetect.py [mp3file] [interval_length]
#       NOTE:
#           - mp3file must be a valid mp3 file that exists in the current directory.
#           - interval_length must be greater than 0 and less than the length of the audio file.
# Postcondition :
#       This function will print analysis information as it calculates the genre of the file.
#       Lastly it will print to the console one of the following:
#           (1) Invalid Number of arguements
#           (2) Unable to find song within current directory (incorrect mp3 name)
#           (3) Unknown Genre (BPM values do not match any range listed for genres)
#           (4) Each Genre with calculated probability
#       
def main():
    if len(sys.argv) == 3:
        song = sys.argv[1]
        interval_length = int(sys.argv[2])
    else:
        print("Invalid Number of Arguments")
        quit()
    
    tempoList = []
    try:
        y, sr = librosa.load(song)                  # Loads Song using the Librosa library
    except FileNotFoundError:                       # File not found in current directory
        print("Unable to find ", song, " within current directory")
        quit()
    
    x = librosa.get_duration(y=y,sr=sr)             # Calculates Length of the mp3 file
    print("Total Length: ", x)
    x1 = math.floor(x)                              # Remove Decimal from length value
    a = math.floor(x1 / interval_length)            # Determines the number of seqments
    b = x1 % interval_length                        # Determines the length of the final seqment  
                                                    # NOTE: (a*interval_length + b) = total length of mp3
                                                    
    print("Number of seqments : ", a,"\nExcess :", b, "seconds")
    for i in range(1,a+1):                          # Splits the audio into 'a' segments
        temp = i*interval_length
        y, sr = librosa.load(song, offset=temp,duration=30)
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        tempoList.append(tempo[0])                  # Appends current seqment BPM to List
    if b != 0:
        y, sr = librosa.load(song, offset=temp, duration=b)     # If b is not zero then the program will calculate
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)     # the BPM of the last seqment
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        tempoList.append(tempo[0])                  # Appends final sequment BPM to List
    #print(tempoList)
    nodups = [*set(tempoList)]                      # Removes all of the duplicates from the list
    print("List of BPM Values with Duplicates removed : \n", nodups) # NOTE: The order might be changed
    tempoList = genreClassification(nodups)         # Determines the Genre using the BPM 
    print("Probable Genres:")
    for i in tempoList:                             # Prints Each line of the tempoList0
        print(i)

# execute function is only ran via an outside script
#   It performs the same functionaility as main but it returns the genreList.
# 
# Precondition:
#       Function must be called by using the following arguments:
#           execute(songName, interval_length)
#            NOTE: 
#               - songName must be a string consisting of the mp3 file name (Ex: 'example1.mp3') 
#               - interval_length must be a integer that is not zero and less than the total length
#                 of the file.  (Ex: 30)
# 
# Postcondition:
#       This program will return one of the following:
#           (1) List : Size = 1, "Incorrect File Name Given" (incorrect mp3 name)
#           (2) List : Size = 1, "Unable to determine Genre" (BPM values do not match any range listed for genres)
#           (3) List : Size = 8, Each Genre with calculated probability
def execute(song,interval_length):
    tempoList = []
    try:
        y, sr = librosa.load(song)                  # Loads Song using the Librosa library
    except FileNotFoundError:
        tempoList.append('Incorrect File Name Given')
        return tempoList
    
    x = librosa.get_duration(y=y,sr=sr)             # Calculates Length of the mp3 file
    x1 = math.floor(x)                              # Remove Decimal from length value
    a = math.floor(x1 / interval_length)            # Determines the number of seqments
    b = x1 % interval_length                        # Determines the length of the final seqment  
                                                    # NOTE: (a*interval_length + b) = total length of mp3
                                                    
    for i in range(1,a+1):                          # Splits the audio into 'a' segments
        temp = i*interval_length
        y, sr = librosa.load(song, offset=temp,duration=30)
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        tempoList.append(tempo[0])                  # Appends current seqment BPM to List
    if b != 0:                                      
        y, sr = librosa.load(song, offset=temp, duration=b)     # If b is not zero then the program will calculate
        onset_env = librosa.onset.onset_strength(y=y,sr=sr)     # the BPM of the last seqment
        tempo = librosa.beat.tempo(onset_envelope=onset_env,sr=sr)
        tempoList.append(tempo[0])                  # Appends final sequment BPM to List
        
    nodups = [*set(tempoList)]                      # Removes all of the duplicates from the list   
                                                    # NOTE: The order might be changed
    tempoList = genreClassification(nodups)         # Determines the Genre using the BPM 

    return tempoList                               

# genreClassication classifies the BPMs by genre using a hard-coded range for each genre.
# NOTE: This function is called by both execute() and main(). This method does not need to be
#       called from a outside script. 
#
# Precondition:
#       BPM_List must be a list with numerical values. Error will occur with anything non-numeric
#       
# Postcondition:
#       This function will return one of the following:
#           (1) List : Size = 1 - "Unable to determine Genre"
#           (2) List : Size = 8 - Genres each with their own probability
def genreClassification(BPM_List):
    unknownCount = 0                            # Intialize unknownCount to zero.
    genreDict = {                               # genreDict is used to count the number of times a BPM
        "Blues": 0,                             # exists in the defined ranges for each genre.
        "Classical": 0,
        "Country": 0,
        "HipHop": 0,
        "Jazz": 0,
        "Metal": 0,
        "Pop": 0,
        "Rock": 0}
    genreList = ["  Blues     : ",              # genreList is predefined with the description of
                 "  Classical : ",              # each genre.
                 "  Country   : ",
                 "  HipHop    : ",
                 "  Jazz      : ",
                 "  Metal     : ",
                 "  Pop       : ",
                 "  Rock      : "]
    arrLen = len(BPM_List)
    for i in range(0,arrLen):                   # i is the index of each BPM in the given List
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
    temp = math.floor(((genreDict["Blues"] / arrLen) * 100))        # Formats temp as a percentage
    genreList[0] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
        
    # Adding Classical Probability
    temp = math.floor(((genreDict["Classical"] / arrLen) * 100))    # Formats temp as a percentage
    genreList[1] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
        
    # Adding Country Probability
    temp = math.floor(((genreDict["Country"] / arrLen) * 100))      # Formats temp as a percentage
    genreList[2] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
     
    #Adding HipHop Probability
    temp = math.floor(((genreDict["HipHop"] / arrLen) * 100))       # Formats temp as a percentage
    genreList[3] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
       
    #Adding Jazz Probability
    temp = math.floor(((genreDict["Jazz"] / arrLen) * 100))         # Formats temp as a percentage
    genreList[4] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
        
    #Adding Metal Probability
    temp = math.floor(((genreDict["Metal"] / arrLen) * 100))        # Formats temp as a percentage
    genreList[5] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
      
    #Adding Pop Probability
    temp = math.floor(((genreDict["Pop"] / arrLen) * 100))          # Formats temp as a percentage
    genreList[6] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
        
    #Adding Rock Probability
    temp = math.floor(((genreDict["Rock"] / arrLen) * 100))         # Formats temp as a percentage
    genreList[7] += str(temp) + '%'
    if temp == 0:
        unknownCount += 1                       # If probability = 0 then add one to the UnknownCount
        
    if unknownCount == 8:                       # If unknownCount = 8 then the program was unable to determine a genre
        retList = ['Unable to determine Genre']
        return retList                          # Returns list of size 1
    else:
        return genreList                        # Returns list of size 8
        
        
if __name__ == '__main__':
    main();
