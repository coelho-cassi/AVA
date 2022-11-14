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


#Feeding the input for the song file name into a variable
song = str(sys.argv[1])

#Reading the lyrics into a usable variable mystring
with open(song) as f:
    lines = f.readlines()
mystring = ''
for x in lines: 
    mystring += x + ' '
    
#Setting up myString to clean itself out.
mystring = mystring.lower()
mystring = cleanString(mystring)
result = mystring.split(" ")

#Reading in a list of garbage words to remove from the lyrics
with open('garbage_words.txt') as g:
    gbglines = g.readlines()
gbgstring = ''
for y in gbglines:
    gbgstring += y + ' '
garbagelist = gbgstring.split(" ")

#Removing the garbage words from the lyrics
result = removeGarbage(result, garbagelist)

#Moving the results of cleaning into a string
finalstring = ''
for i in result:
    finalstring += i + ' '

#Running the string through the text2Emotion function.
mood_new = te.get_emotion(finalstring)

#Pulling out just the values for Happy, Sad, and Anger
happy_weight = mood_new['Happy']
sad_weight = mood_new['Sad']
angry_weight = mood_new['Angry']

#Weighing the weight of these three emotions against each other
total_weight = happy_weight + sad_weight + angry_weight
happy_weight = round(((happy_weight / total_weight) * 100),1)
angry_weight = round(((angry_weight / total_weight) * 100),1)
sad_weight = round(((sad_weight / total_weight) * 100),1)

#Output Formatting
outStr1 = 'This song is ' + str(happy_weight) + '% happy.\n'
outStr2 = 'This song is ' + str(angry_weight) + '% angry.\n'
outStr3 = 'This song is ' + str(sad_weight) + '% sad.\n'
print(outStr1,outStr2,outStr3)


    

    
