import text2emotion as te
import sys
import os.path

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
# The strongest emotion is: {Happy, Angry, Sad}
#
# It is rounded to one decimal place and will remove leading zeroes.
#
# Important Variables:
#   happy_weight - float value for happiness percentage of the song.
#   sad_weight - float value for sadness percentage of the song.
#   angry_weight - float value for angry percentage of the song.
#   strongest_mood - contains a string of the name of the highest mood(s)
#


#   Compares a string to a predetermined list of symbols to be removed and replaces them
#   with blank spaces, thus 'cleaning' the string.
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

#   Removes all instances of a specified word from a specified list.
def remAll(test_list, item):
    res = [i for i in test_list if i != item]
    return res

#   Compares a list against a predetermined list of words with negligible
#   meaning towards the overall mood of the song and removes them from the
#   list, thus 'removing the garbage' from the lyrics.
def removeGarbage(test_list, gbg_list):
    for i in gbg_list:
        test_list = remAll(test_list, i)
    return test_list
    
#   This function will determine which mood out of happy, sad, and anger has
#   the highest weighting and returns it regardless of whether or not it's 
#   within a 0.000001% difference from another mood.

def conclusiveResults(hw, sw, aw):
    weight_list = [hw, sw, aw]
    if(max(weight_list_2) == hw):
        return('Happy')
    elif(max(weight_list_2) == sw):
        return('Sad')
    else:
        return('Angry')

#   This function will determine which of the mood(s) hold the highest weighting.
#   If two (or three) emotions are within 5% of each other in overall weighting,
#   it will return that the results are inconclusive and which emotions are 'tied.'
def inconclusiveResults(hw, sw, aw):
    if ((hw - sw >= 5) and (hw - aw > 5)):
        return('Happy')
    elif ((sw - aw >= 5) and (sw - hw > 5)):
        return('Sad')
    elif ((aw - sw >= 5) and (aw - hw > 5)):
        return('Anger')
    elif ((abs(hw - sw) < 5) and (hw - aw > 5)):
        return('Inconclusive. Happy and Sad')
    elif ((abs(hw - aw) < 5) and (hw - sw > 5)):
        return('Inconclusive. Happy and Angry')
    elif ((abs(aw - sw) < 5) and (aw - hw > 5)):
        return('Inconclusive. Angry and Sad')
    else:
        return(' Inconclusive. Happy, Angry, and Sad')



def checkLyrics(song):

    #Checks to see if the song exits
    file_exists = os.path.exists(song)
    if(file_exists == False):
        return("Err: Lyrics file DNE")


    #Reading the lyrics into a usable variable mystring
    with open(song) as f:
        lines = f.readlines()
    mystring = ''
    for x in lines: 
        mystring += x + ' '
        
    if(len(mystring) == 0):
        return("Err: Empty txt document")
    oldstring = mystring
    
    #Setting up myString to clean itself out.
    mystring = mystring.lower()
    mystring = cleanString(mystring)
    result = mystring.split(" ")
    
    #   Reading in a list of garbage words to remove from the lyrics
    with open('garbage_words.txt') as g:
        gbglines = g.readlines()
    gbgstring = ''
    for y in gbglines:
        gbgstring += y + ' '
    garbagelist = gbgstring.split(" ")
    
    #   Removing the garbage words from the lyrics
    result = removeGarbage(result, garbagelist)

    #   Moving the results of cleaning into a string
    finalstring = ''
    for i in result:
        finalstring += i + ' '





    #   Running the string through the text2Emotion function.
    mood_new = te.get_emotion(finalstring)

    #   Pulling out just the values for Happy, Sad, and Anger
    happy_weight = mood_new['Happy']
    sad_weight = mood_new['Sad']
    angry_weight = mood_new['Angry']
    
    #   Weighing the weight of these three emotions against each other
    #   and determining what the weight of JUST happy, angry, and sad are.
    total_weight = happy_weight + sad_weight + angry_weight
    
    if(total_weight == 0):
        return("Err: No usable lyrics.")
    
    happy_weight = round(((happy_weight / total_weight) * 100),1)
    angry_weight = round(((angry_weight / total_weight) * 100),1)
    sad_weight = round(((sad_weight / total_weight) * 100),1)
    
    
    #   CONCLUSIVE For Conclusive answers Uncomment the following line and comment INCONCLUSIVE
    #strongest_mood = conclusiveResults(happy_weight, sad_weight, angry_weight)
    
    #   UNCONCLUSIVE For Inconclusive results, uncomment the following line and comment CONCLUSIVE 
    strongest_mood = inconclusiveResults(happy_weight, sad_weight, angry_weight)
        
    
    

    #   Print the percentages of each emotion
    
    #outStr1 = 'This song is ' + str(happy_weight) + '% happy.'
    #outStr2 = 'This song is ' + str(angry_weight) + '% angry.'
    #outStr3 = 'This song is ' + str(sad_weight) + '% sad.'
    #print(outStr1)
    #print(outStr2)
    #print(outStr3)
    
    finalString = "The strongest emotion is: "+ strongest_mood
    return finalString
    #   Final Return
    returnString = 'The strongest emotion is:',strongest_mood
    #returnString = strongest_mood_conclusive
    return(returnString)    
    

#   Feeding the input for the song file name into a variable
#song = str(sys.argv[1])
#checkLyrics(song)