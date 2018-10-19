import csv


lines = []

with open('gamers.csv', 'r', newline='') as f:
    file_reader = csv.reader(f, delimiter=';', )
    [lines.append(';'.join(row)) for row in file_reader]
    hs = max(lines[-2:]).split(";")

    name = hs[0]
    date = hs[1].replace(" ", "")
    score = hs[2].replace(" ", "")

    print("On {0}, {1} placed a new high-score: {2}".format(date, name, score))

    f.close()