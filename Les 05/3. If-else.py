leeftijd = eval(input('Geef je leeftijd: '))
paspoort = input('Nederlands paspoort: ')
if leeftijd > 17 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag niet stemmen!')