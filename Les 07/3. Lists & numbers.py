invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijstgetallen = []
for line in invoer:
    line = line.split('-')
    if line[0] != '':
        lijstgetallen.append(line[0])
results = [int(line) for line in lijstgetallen]
totaal = sum(results)
gemiddelde = totaal / len(results)
print('Gesorteerde list van ints ' + str(results))
print('Grootste getal ' + str(results[-1]) + ' en Kleinste getal: ' + str(results[0]))
print('Aantal getallen: ' + str(len(lijstgetallen)) + ' en Som van de getallen: ' + str(totaal))
print('Gemiddelde: ' + str(gemiddelde))