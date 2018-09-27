def gemiddelde(input):
    input_list = input.split()
    len_lijst = []
    for woord in input_list:
          lengte = len(woord)
          len_lijst.append(lengte)
    resultaat = sum(len_lijst) / len(len_lijst)
    print(resultaat)