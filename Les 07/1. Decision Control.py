def seizoen(maand):
    lijst = ('januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december')
    som = maand - 1
    if som == 12 or som == 1 or som == 2:
        seizoennaam = 'winter'
    elif som == 3 or som == 4 or som == 5:
        seizoennaam = 'lente'
    elif som == 6 or som == 7 or som == 8:
        seizoennaam = 'zomer'
    else:
        seizoennaam = 'herfst'
    resultaat = lijst[som]
    print(resultaat + ' ' + seizoennaam)