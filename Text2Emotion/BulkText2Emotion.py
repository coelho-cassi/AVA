import text2emotion as te
import sys

#
# Program: Text2Emotion.py
# Author: Jacob Sisk
# Last Update Date: 11/14/2022
#
# Supporting Documents:
# clean_words_list.txt - List of symbols to clean from the lyrics
# garbage_words.txt - List of Garbage Words to remove from lyrics
# [file with song lyrics].txt - The lyrics to the song you want to be analyzed
#
# IMPORTANT: These files must be present in the same folder as this program or 
#            it will not run without editing.
#
# Description
# This song takes the predefined lyrics of a song and outputs what it believes
# to be the percentage of the song that the emotions happiness, sadness, and anger to be.
#
# Input Requirements
# When calling the function you need to pass the name of a text file containing the lyrics
# to the song you want to analyze. For example:
# python Text2Emotion.py Lyrics_DontStopBelieving.txt
#
# The Output will look like:
# 
# This song is 00.0% happy.
# This song is 00.0% angry.
# This song is 00.0% sad.
#
# It is rounded to one decimal place and will remove leading zeroes.
#
# Important Variables:
#   happy_weight - float value for happiness percentage of the song.
#   sad_weight - float value for sadness percentage of the song.
#   angry_weight - float value for angry percentage of the song.
#   strongest_mood - contains a string of the name of the highest mood(s)
#


#Function written to remove punctuation and other things that will lower the accuracy of the results
def cleanString(mystring):
    with open('clean_words_list.txt') as cln:
        remSymbols = cln.readlines()
    symbolString = ''
    for z in remSymbols:
        symbolString += z + ' '
    symbolList = symbolString.split(" ")
    
    mystring = mystring.replace("in'", "ing")
    for i in symbolList:
        mystring = mystring.replace(i,'')
    return mystring

#Function used by removeGarbage to remove all instances of every word on its list
def remAll(test_list, item):
    res = [i for i in test_list if i != item]
    return res

#Fuction used to remove the garbage words
def removeGarbage(test_list, gbg_list):
    for i in gbg_list:
        test_list = remAll(test_list, i)
    return test_list

def checkLyrics(song):
    #Feeding the input for the song file name into a variable
    #song = str(sys.argv[1])

    #print("ARRIVED IN MAIN FUNCTION")

    #Reading the lyrics into a usable variable mystring
    with open(song) as f:
        lines = f.readlines()
    mystring = ''
    for x in lines: 
        mystring += x + ' '
    oldstring = mystring
    
    #print("READ THE SONG FILE")
    
    #Setting up myString to clean itself out.
    mystring = mystring.lower()
    mystring = cleanString(mystring)
    result = mystring.split(" ")
    
    #print("CLEANED THE FILE")
    
    #Reading in a list of garbage words to remove from the lyrics
    with open('garbage_words.txt') as g:
        gbglines = g.readlines()
    gbgstring = ''
    for y in gbglines:
        gbgstring += y + ' '
    garbagelist = gbgstring.split(" ")
    
    #Removing the garbage words from the lyrics
    result = removeGarbage(result, garbagelist)
    
    #print("REMOVED THE GARBAGE")

    #Moving the results of cleaning into a string
    finalstring = ''
    for i in result:
        finalstring += i + ' '

    #Running the string through the text2Emotion function.
    mood_old = te.get_emotion(oldstring)
    mood_new = te.get_emotion(finalstring)
    
    #print("GOT THE MOOD")

    #Pulling out just the values for Happy, Sad, and Anger
    happy_weight = mood_new['Happy']
    sad_weight = mood_new['Sad']
    angry_weight = mood_new['Angry']

    old_happy_weight = mood_old['Happy']
    old_sad_weight = mood_old['Sad']
    old_angry_weight = mood_old['Angry']
    old_surprise_weight = mood_old['Surprise']
    old_fear_weight = mood_old['Fear']
    
    #print("PULLED OUT THE WEIGHTS")

    weight_list = [old_angry_weight, old_fear_weight, old_happy_weight, old_sad_weight, old_surprise_weight]

    if( max(weight_list) == old_angry_weight):
        old_strongest_mood = 'Angry'
    elif(max(weight_list) == old_fear_weight):
        old_strongest_mood = 'Fear'
    elif(max(weight_list) == old_happy_weight):
        old_strongest_mood = 'Happy'
    elif(max(weight_list) == old_sad_weight):
        old_strongest_mood = 'Sad'
    else:
        old_strongest_mood = 'Surprise'
        
    #print("DETERMINED OLD MOOD") 
        

    #Weighing the weight of these three emotions against each other
    total_weight = happy_weight + sad_weight + angry_weight
    happy_weight = round(((happy_weight / total_weight) * 100),1)
    angry_weight = round(((angry_weight / total_weight) * 100),1)
    sad_weight = round(((sad_weight / total_weight) * 100),1)
    
    weight_list_2 = [happy_weight, sad_weight, angry_weight]
    
    if(max(weight_list_2) == happy_weight):
        strongest_mood_conclusive = 'Happy'
    elif(max(weight_list_2) == sad_weight):
        strongest_mood_conclusive = 'Sad'
    else:
        strongest_mood_conclusive = 'Angry'
    
    #print("CALCULATED NEW WEIGHTS")

    #Output Formatting
    #outStr1 = 'This song is ' + str(happy_weight) + '% happy.'
    #outStr2 = 'This song is ' + str(angry_weight) + '% angry.'
    #outStr3 = 'This song is ' + str(sad_weight) + '% sad.'
    #print(outStr1)
    #print(outStr2)
    #print(outStr3)

    #Determining which mood(s) have the highest weight
    #if ((happy_weight - sad_weight >= 5) and (happy_weight - angry_weight > 5)):
    #    strongest_mood = 'Happy'
    #elif ((sad_weight - angry_weight >= 5) and (sad_weight - happy_weight > 5)):
    #    strongest_mood = 'Sad'
    #elif ((angry_weight - sad_weight >= 5) and (angry_weight - happy_weight > 5)):
    #    strongest_mood = 'Anger'
    #elif ((abs(happy_weight - sad_weight) < 5) and (happy_weight - angry_weight > 5)):
    #    strongest_mood = 'Inconclusive. Happy and Sad'
    #elif ((abs(happy_weight - angry_weight) < 5) and (happy_weight - sad_weight > 5)):
    #    strongest_mood = 'Inconclusive. Happy and Angry'
    #elif ((abs(angry_weight - sad_weight) < 5) and (angry_weight - happy_weight > 5)):
    #    strongest_mood = 'Inconclusive. Angry and Sad'
    #else:
    #    strongest_mood = ' Inconclusive. Happy, Angry, and Sad'
        
    #print("DETERMINED OLD MOODS")
    spaces = ''
    spaces2 = ''
    for x in range (35 - len(song)):
        spaces = spaces + ' '
    for x in range (20 - len(old_strongest_mood)):
        spaces2 = spaces2 + ' '
    returnString = ''
    returnString = song + spaces + 'Before: ' + old_strongest_mood + spaces2 + 'After: ' + strongest_mood_conclusive + '\n'
    
    #PRINT("FORMED FINAL STRING")
    
    return returnString
    
    
    #print('The strongest emotion is:',strongest_mood)



print("Starting")
with open('LyricsList.txt') as LL:
    dirtySongList = LL.readlines()
songListString = ''

for z in dirtySongList:
    songListString += z + ' '
songListString = songListString.replace('\n','')
cleanSongList = songListString.split(" ")
plain_text = open("result_conclusive.txt", "a")

for i in cleanSongList:
    if(i == ''):
        exit()
    lastString = checkLyrics(i)
    plain_text.write(lastString)
    print("Analyzed Song " + i)