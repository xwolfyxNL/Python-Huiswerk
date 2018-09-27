list = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]
newlist = []
if len(list) < 10:
    print('De lijst bevat niet minimaal 10 strings')
else:
    for strings in list:
        if len(strings) == 4:
            newlist.append(strings)
    print('De nieuw-gemaakte lijst met alle vier-letter strings is: ' + str(newlist))


