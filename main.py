import csv
from collections import Counter,defaultdict
def parse(text):
    """
    This function parses text that is a list of strings "['str1','str2']" into the python list containing the strings 'str1' and 'str2'
    """
    if text.startswith("[") and text.endswith("]"):
        return eval(text)
    else:
        print("Error reading text: ", text)
        return []
 

anime = []
with open('myanimelist.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        anime.append(row)
        

# print(anime[0])
# print(anime[1][2])

genres = []
for row in anime[1:]:
    genres.append (parse(row[3]))
# print(genres[:10])
# print(set(sum(genres,[])))
print(Counter(sum(genres,[])))
genres_map=defaultdict(list)
for row in anime[1:]:
    for genre in parse(row[3]):
        genres_map[genre].append(row[1])
print(genres_map['Yaoi'])