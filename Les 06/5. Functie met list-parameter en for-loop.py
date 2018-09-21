def kwadraten_som(grondGetallen):
    positieveGetallen = [x for x in grondGetallen if x >= 0]
    kwadraatGetallen = [x ** 2 for x in positieveGetallen]
    return sum(kwadraatGetallen)