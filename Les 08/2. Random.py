import random

def monopolyworp():
    dobbelsteen1 = random.randrange(1, 7)
    dobbelsteen2 = random.randrange(1, 7)
    dobbelsteentotaal = dobbelsteen1 + dobbelsteen2
    if dobbelsteen1 != dobbelsteen2:
        print('' + str(dobbelsteen1) + ' + ' + str(dobbelsteen2) + ' = ' + str(dobbelsteentotaal) + '')
    else:
        dubbelgooien = 0
        while dobbelsteen1 == dobbelsteen2:
            print('' + str(dobbelsteen1) + ' + ' + str(dobbelsteen2) + ' = ' + str(dobbelsteentotaal) + ' (dubbel)')
            dubbelgooien += 1
            dobbelsteen1 = random.randrange(1, 7)
            dobbelsteen2 = random.randrange(1, 7)
            dobbelsteentotaal = dobbelsteen1 + dobbelsteen2
            if dobbelsteen1 != dobbelsteen2:
                print('' + str(dobbelsteen1) + ' + ' + str(dobbelsteen2) + ' = ' + str(dobbelsteentotaal) + '')
                break
            elif dubbelgooien == 2:
                print('' + str(dobbelsteen1) + ' + ' + str(dobbelsteen2) + ' = ' + str(dobbelsteentotaal) + ' (direct naar de gevangenis)')
                break
monopolyworp()