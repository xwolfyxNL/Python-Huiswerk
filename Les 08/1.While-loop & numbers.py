inputgetal = 1
lijstgetallen = []
while inputgetal != 0:
    inputgetal = int(input('Geef een getal: '))
    if inputgetal == 0:
        break
    lijstgetallen.append(inputgetal)
aantalgetallen = len(lijstgetallen)
sumgetallen = sum(lijstgetallen)
print('Er zijn ' + str(aantalgetallen) + ' ingevoerd, de som is: ' + str(sumgetallen))

