import text2emotion as te

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


def remAll(test_list, item):
 
    res = [i for i in test_list if i != item]
 
    return res

def removeGarbage(test_list, gbg_list):
    for i in gbg_list:
        test_list = remAll(test_list, i)
    return test_list

with open('Lyrics_PumpedUpKicks.txt') as f:
    lines = f.readlines()
mystring = ''
for x in lines: 
    mystring += x + ' '
mystring = mystring.lower()

mystring2 = cleanString(mystring)

result = mystring2.split(" ")

with open('garbage_words.txt') as g:
    gbglines = g.readlines()
gbgstring = ''
for y in gbglines:
    gbgstring += y + ' '
garbagelist = gbgstring.split(" ")

result = removeGarbage(result, garbagelist)
finalstring = ''
for i in result:
    finalstring += i + ' '

mood_old = te.get_emotion(mystring)
mood_new = te.get_emotion(finalstring)

#print(mystring)
#print(finalstring)
print(mood_old)
print(mood_new)
    

    
