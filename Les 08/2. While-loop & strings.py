inputwoord = ''
while len(inputwoord) != 4:
    inputwoord = input('Geef een string van vier letters: ')
    if len(inputwoord) == 4:
        print('Inlezen van correcte string: ' + inputwoord + ' is geslaagd')
        break
    print(inputwoord + ' heeft ' + str(len(inputwoord)) + ' letters')