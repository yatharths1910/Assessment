import csv

file = open("movie_quotes.csv", "r")
all_quotes = list(csv.reader(file, delimiter=","))
file.close()

all_quotes.pop(0)
print(all_quotes[:181])
# print(all_quotes)

print("Length: {}".format(len(all_quotes)))