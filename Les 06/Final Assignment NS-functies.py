# Functie standaardprijs
def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = 15 + 0.60 * afstandKM
    else:
        prijs = 0.80 * afstandKM
    if prijs < 0:
        prijs = 0
    return prijs

#Functie ritprijs
def ritprijs(leeftijd, weekendrit, afstandKM):
    prijsophalen = standaardprijs(afstandKM)
    if weekendrit == 'True':
        weekendkorting = 'True'
    else:
        weekendkorting = 'False'
    if leeftijd < 12 or leeftijd > 64:
        if weekendkorting == 'True':
            prijs = prijsophalen - (prijsophalen * .35)
        else:
            prijs = prijsophalen - (prijsophalen * .30)
    else:
        if weekendkorting == 'True':
            prijs = prijsophalen - (prijsophalen * .40)
        else:
            prijs = prijsophalen
    return prijs

leeftijd = int(input('Geef je leeftijd op: '))
weekendrit = input('Is het weekend? (True/False): ')
afstandKM = float(input('Hoeveel km heb je gereisd: '))

print('Je betaalt voor deze rit ' + str(ritprijs(leeftijd,weekendrit,afstandKM)))