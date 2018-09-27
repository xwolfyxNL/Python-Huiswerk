infile = open('Kaartnummers.txt', 'r')

for line in infile:
    line = line.split(',')
    template = '{} heeft kaartnumeer {}'
    print(template.format(line[1].rstrip(),line[0]))