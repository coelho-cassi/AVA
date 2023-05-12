import re
import json
frequency_rock = {}
frequency_pop = {}
frequency_metal = {}
frequency_blues = {}
frequency_country = {}
frequency_hiphop = {}
frequency_all = {}
frequency_song = {}
word_count_all = {}

document_text = open('AllLyricsRock.txt', 'r')
text_string = document_text.read().lower()
match_pattern_rock = re.findall(r'\b[a-z]{3,15}\b', text_string)

document_text2 = open('AllLyricsPop.txt', 'r')
text_string2 = document_text2.read().lower()
match_pattern_pop = re.findall(r'\b[a-z]{3,15}\b', text_string2)

document_text3 = open('AllLyricsMetal.txt', 'r')
text_string3 = document_text3.read().lower()
match_pattern_metal = re.findall(r'\b[a-z]{3,15}\b', text_string3)

document_text4 = open('AllLyricsHipHop.txt', 'r')
text_string4 = document_text4.read().lower()
match_pattern_hiphop = re.findall(r'\b[a-z]{3,15}\b', text_string4)

document_text5 = open('AllLyricsCountry.txt', 'r')
text_string5 = document_text5.read().lower()
match_pattern_country = re.findall(r'\b[a-z]{3,15}\b', text_string5)

document_text6 = open('AllLyricsBlues.txt', 'r')
text_string6 = document_text6.read().lower()
match_pattern_blues = re.findall(r'\b[a-z]{3,15}\b', text_string6)

total_word_string = text_string + text_string2 + text_string3 + text_string4 + text_string5 + text_string6
match_pattern_all = re.findall(r'\b[a-z]{3,15}\b', total_word_string)

blacklisted = ['the', 'and', 'for', 'that', 'which']


for word in match_pattern_pop:
    if word not in blacklisted:
        count_pop = frequency_pop.get(word,0)
        frequency_pop[word] = count_pop + 1
most_frequent_pop = dict(sorted(frequency_pop.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_pop = most_frequent_pop.keys()

for word in match_pattern_rock:
    if word not in blacklisted:
        count_rock = frequency_rock.get(word,0)
        frequency_rock[word] = count_rock + 1
most_frequent_rock = dict(sorted(frequency_rock.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_rock = most_frequent_rock.keys()

for word in match_pattern_metal:
    if word not in blacklisted:
        count_metal = frequency_metal.get(word,0)
        frequency_metal[word] = count_metal + 1
most_frequent_metal = dict(sorted(frequency_metal.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_metal = most_frequent_metal.keys()

for word in match_pattern_country:
    if word not in blacklisted:
        count_country = frequency_country.get(word,0)
        frequency_country[word] = count_country + 1
most_frequent_country = dict(sorted(frequency_country.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_country = most_frequent_country.keys()

for word in match_pattern_blues:
    if word not in blacklisted:
        count_blues = frequency_blues.get(word,0)
        frequency_blues[word] = count_blues + 1
most_frequent_blues = dict(sorted(frequency_blues.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_blues = most_frequent_blues.keys()

for word in match_pattern_hiphop:
    if word not in blacklisted:
        count_hiphop = frequency_hiphop.get(word,0)
        frequency_hiphop[word] = count_hiphop + 1
most_frequent_hiphop = dict(sorted(frequency_hiphop.items(), key=lambda elem: elem[1], reverse=True))
most_frequent_count_hiphop = most_frequent_hiphop.keys()


for word in match_pattern_all:
   if word not in blacklisted:
        count_all = frequency_all.get(word,0)
        frequency_all[word] = count_all + 1
most_frequent_all = dict(sorted(frequency_all.items(), key=lambda elem: elem[1], reverse=True))
most_frequenct_count_all = most_frequent_all.keys()


with open('rock_dict.txt', 'w') as fp:
    json.dump(most_frequent_rock, fp)
    
with open('pop_dict.txt', 'w') as fp:
    json.dump(most_frequent_pop, fp)
    
with open('metal_dict.txt', 'w') as fp:
    json.dump(most_frequent_metal, fp)
    
with open('blues_dict.txt', 'w') as fp:
    json.dump(most_frequent_blues, fp)
    
with open('hiphop_dict.txt', 'w') as fp:
    json.dump(most_frequent_hiphop, fp)
    
with open('country_dict.txt', 'w') as fp:
    json.dump(most_frequent_country, fp)

with open('all_dict.txt', 'w') as fp:
    json.dump(most_frequent_all, fp)


#for words in most_frequent_count_metal:
#    print(words, most_frequent_metal[words])



