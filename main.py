import csv
anime = []
with open('myanimelist.csv', newline='', encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        anime.append(row)
        #print(', '.join(row))
        # break

print(anime[0])
print(anime[1][2])
