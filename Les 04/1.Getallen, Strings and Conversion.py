cijferICOR = 7
cijferPROG = 8
cijferCSN = 7
cijferpunt = 30
gemiddelde = (cijferICOR+cijferPROG+cijferCSN) / 3
beloning = gemiddelde * cijferpunt
overzicht = 'Mijn cijfers (gemiddeld een',round(gemiddelde, 1),') leveren een beloning van €',beloning,' op!'
print (overzicht)