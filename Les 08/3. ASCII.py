def code(invoerstring):
    string = ''
    for letter in invoerstring:
        ascii = ord(letter)
        encryptie = ascii + 3
        string += chr(encryptie)
    print (string)
code('RutteAlkmaarDen Helder')