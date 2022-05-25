import csv

def parse(text):
    """
    This function parses text that is a list of strings "['str1','str2']" into the python list containing the strings 'str1' and 'str2'
    """
    if text.startswith("['") and text.endswith("']"):
        return eval(text)
    else:
        print("Error reading text: ", text)
        return []
 

anime = []
with open('myanimelist.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        anime.append(row)
        

print(anime[0])
print(anime[1][2])

genres = parse(anime[1][3])
print(genres[0])
print(genres[1])