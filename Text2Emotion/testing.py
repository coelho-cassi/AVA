import text2emotion as te

with open('Lyrics_DontStopBeliving.txt') as f:
    lines = f.readlines()
    mystring = ' '
    for x in lines: 
        mystring += ' ' + x
    beans = te.get_emotion(mystring)
    print(mystring + "\n")
    print(beans)
    print("\n")
    
with open('Lyrics_DontStopBeliving2.txt') as f:
    lines = f.readlines()
    mystring = ' '
    for x in lines: 
        mystring += ' ' + x
    beans = te.get_emotion(mystring)
    print(mystring + "\n")
    print(beans)
