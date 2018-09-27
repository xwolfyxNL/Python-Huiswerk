infile = open('Kaartnummers.txt', 'r')
bestand = infile.readlines()
regels = len(bestand)
lijst = []
for line in bestand:
    line = line.split(',')
    lijst.append(line[0])
maxnummer = max(lijst)
for num, line in enumerate(bestand, 1):
        if maxnummer in line:
            regelmaxnummer = num


print('De file telt ' + str(regels) + ' Regels')
print('Het grootste kaartnummer is: ' + maxnummer + ' en dat staat op regel ' + str(regelmaxnummer))
