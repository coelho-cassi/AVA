import re
import json


with open('rock_dict.txt', 'r') as fp:
    rock_dict = json.load(fp)
    
with open('pop_dict.txt', 'r') as fp:
    pop_dict = json.load(fp)
    
with open('metal_dict.txt', 'r') as fp:
    metal_dict = json.load(fp)
    
with open('blues_dict.txt', 'r') as fp:
    blues_dict = json.load(fp)
    
with open('hiphop_dict.txt', 'r') as fp:
    hiphop_dict = json.load(fp)
    
with open('country_dict.txt', 'r') as fp:
    country_dict = json.load(fp)
    
with open('all_dict.txt', 'r') as fp:
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

rock_word_total = 0
pop_word_total = 0
metal_word_total = 0
country_word_total = 0
blues_word_total = 0
hiphop_word_total = 0

for words in rock_dict_count:
    rock_word_total += rock_dict[words]
for words in pop_dict_count:
    pop_word_total += pop_dict[words]
for words in metal_dict_count:
    metal_word_total += metal_dict[words]
for words in country_dict_count:
    country_word_total += country_dict[words]
for words in blues_dict_count:
    blues_word_total += blues_dict[words]
for words in hiphop_dict_count:
    hiphop_word_total += hiphop_dict[words]

print('rock ', rock_word_total/10000)
print('pop ', pop_word_total/10000)
print('metal ', metal_word_total/10000)
print('country ', country_word_total/10000)
print('hiphop ', hiphop_word_total/10000)
print('blues ', blues_word_total/10000)