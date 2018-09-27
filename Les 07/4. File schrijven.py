import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")

def hardloper(naam):
    bestand = open('hardlopers.txt', 'a')
    bestand.write(s + naam + "\n")
    bestand.close()