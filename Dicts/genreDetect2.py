import re
import json
import sys

def execute(song):

    with open('Dicts/rock_dict.txt', 'r') as fp:
        rock_dict = json.load(fp)
        
    with open('Dicts/pop_dict.txt', 'r') as fp:
        pop_dict = json.load(fp)
        
    with open('Dicts/metal_dict.txt', 'r') as fp:
        metal_dict = json.load(fp)
        
    with open('Dicts/blues_dict.txt', 'r') as fp:
        blues_dict = json.load(fp)
        
    with open('Dicts/hiphop_dict.txt', 'r') as fp:
        hiphop_dict = json.load(fp)
        
    with open('Dicts/country_dict.txt', 'r') as fp:
        country_dict = json.load(fp)
        
    with open('Dicts/all_dict.txt', 'r') as fp:
        all_dict = json.load(fp)

    rock_dict_count = rock_dict.keys()
    pop_dict_count = pop_dict.keys()
    metal_dict_count = metal_dict.keys()
    blues_dict_count = blues_dict.keys()
    hiphop_dict_count = hiphop_dict.keys()
    country_dict_count = country_dict.keys()
    all_dict_count = all_dict.keys()

    #for words in rock_dict_count:
    #    print(words, rock_dict[words])

    song_input = song

    song_text = open(song_input, 'r')
    text_string = song_text.read().lower()
    if( len(text_string) < 100): return 'NoLyrics'
    #if( len(text_string) < 100): print("No Lyrics")
    match_pattern_song = re.findall(r'\b[a-z]{3,15}\b', text_string)
    blacklisted = ['the', 'and', 'for', 'that', 'which']

    rock_weight, rock_word_count = 0, 0
    pop_weight, pop_word_count = 0, 0
    metal_weight, metal_word_count = 0, 0
    country_weight, country_word_count = 0, 0
    blues_weight, blues_word_count = 0, 0
    hiphop_weight, hiphop_word_count = 0, 0
    total_unique_word_count = 0
    frequency_song = {}

    for word in match_pattern_song:
        if word not in blacklisted:
            count = frequency_song.get(word,0)
            frequency_song[word] = count + 1
    song_dict = dict(sorted(frequency_song.items(), key=lambda elem: elem[1], reverse=True))
    song_dict_count = song_dict.keys()

    for words in song_dict_count:
        total_unique_word_count += 1
        if (words in all_dict_count): 
            if (words in rock_dict_count):
                rock_word_count += 1
                rock_weight += song_dict[words] * (rock_dict[words] / all_dict[words])
            if (words in pop_dict_count):
                pop_word_count += 1
                pop_weight += song_dict[words] * (pop_dict[words] / all_dict[words])
            if (words in metal_dict_count):
                metal_word_count += 1
                metal_weight += song_dict[words] * (metal_dict[words] / all_dict[words])
            if (words in hiphop_dict_count):
                hiphop_word_count += 1
                hiphop_weight += song_dict[words] * (hiphop_dict[words] / all_dict[words])
            if (words in country_dict_count):
                country_word_count += 1
                country_weight += song_dict[words] * (country_dict[words] / all_dict[words])
            if (words in blues_dict_count):
                blues_word_count += 1
                blues_weight += song_dict[words] * (blues_dict[words] / all_dict[words])
            
    #print('')
    #print('Rock Weighting: ', rock_weight)
    #print('Pop Weighting: ', pop_weight)
    #print('Metal Weighting: ', metal_weight)
    #print('HipHop Weighting: ', hiphop_weight)
    #print('Country Weighting: ', country_weight)
    #print('Blues Weighting: ', blues_weight)

    rock_perc = ((rock_word_count / total_unique_word_count) * 100)
    pop_perc = ((pop_word_count / total_unique_word_count) * 100)
    metal_perc = ((metal_word_count / total_unique_word_count) * 100)
    hiphop_perc = ((hiphop_word_count / total_unique_word_count) * 100)
    country_perc = ((country_word_count / total_unique_word_count) * 100)
    blues_perc = ((blues_word_count / total_unique_word_count) * 100)

    rock_weight = rock_weight / 1.6769
    pop_weight = pop_weight / 2.4992
    metal_weight = metal_weight / 1.5593
    country_weight = country_weight / 1.3178
    hiphop_weight = hiphop_weight / 4.3953
    blues_weight = blues_weight / 1.2362

    #print('')
    #print('Percentage of words in Rock dict: ', rock_perc)
    #print('Percentage of words in Pop dict: ', pop_perc)
    #print('Percentage of words in Metal dict: ', metal_perc)
    #print('Percentage of words in HipHop dict: ', hiphop_perc)
    #print('Percentage of words in Country dict: ', country_perc)
    #print('Percentage of words in Blues dict: ', blues_perc)
    #print('')

    max_weight = max(rock_weight, pop_weight, metal_weight, hiphop_weight, country_weight, blues_weight)
    max_perc = max(rock_perc, pop_perc, metal_perc, hiphop_perc, country_perc, blues_perc)

    weight_winner = ''
    if(max_weight == rock_weight): weight_winner += 'Rock'
    if(max_weight == pop_weight): weight_winner += 'Pop'
    if(max_weight == metal_weight): weight_winner += 'Metal'
    if(max_weight == hiphop_weight): weight_winner += 'HipHop'
    if(max_weight == country_weight): weight_winner += 'Country'
    if(max_weight == blues_weight): weight_winner += 'Blues'

    perc_winner = ''
    if(max_perc == rock_perc): perc_winner += 'Rock'
    if(max_perc == pop_perc): perc_winner += 'Pop'
    if(max_perc == metal_perc): perc_winner += 'Metal'
    if(max_perc == hiphop_perc): perc_winner += 'HipHop'
    if(max_perc == country_perc): perc_winner += 'Country'
    if(max_perc == blues_perc): perc_winner += 'Blues'

    #print('')
    #print('By weighting the words, we think this songs genre is:', weight_winner)
    #print('By checking the word percentiles, we think this songs genre is:', perc_winner)
    #print('')
    return weight_winner

