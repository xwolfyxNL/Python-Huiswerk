studentencijfers = {'Henk':1, 'Piet':9, 'Julia':6, 'Judith':10, 'Alex':9, 'Zyad':7, 'Alexander':6, 'Max':10, 'Lewis':9}
resultaat = dict((k, v) for k, v in studentencijfers.items() if v >= 9)
print(resultaat)