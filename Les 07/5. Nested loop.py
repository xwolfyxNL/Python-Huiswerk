nummer_lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nummer_lijst:
    for nummer in range(1, 11):
         print(num,'x',nummer,'=',num*nummer)
nummer_lijst.remove(min(nummer_lijst))
