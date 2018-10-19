import csv

products = [[121, 'ABC123', 'Highlight pen', 231, 0.56],
            [123, 'PQR678', 'Nietmachine', 587, 9.99],
            [128, 'ZYX163', 'Bureaulamp', 34, 19.95],
            [137, 'MLK709', 'Monitorstandaard', 66, 32.50],
            [271, 'TRS665', 'Ipad hoes', 155, 19.01]]

with open('products.csv', 'r+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Product#", "Product-code", "Name", "Stock", "Price"])
    for p in products:
        csv_writer.writerow(p)

lines = []
with open("products.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    [lines.append(line) for line in csv_reader]

    lowest_count = 'unset'
    highest_price = 0
    total_products = 0
    most_expensive_product = []

    for line in lines[1:]:
        count = int(line[3])

        if lowest_count == 'unset':
            lowest_count = count
            lowest_count_product = line
        elif lowest_count > count:
            lowest_count = count
            lowest_count_product = line

        if float(line[4]) > highest_price:
            highest_price = float(line[4])
            most_expensive_product = line
        total_products += int(line[3])

    print('Het duurste artikel is', most_expensive_product[2], 'en die kost', most_expensive_product[4])
    print("Er zijn slechts", lowest_count_product[3], "exemplaren in voorraad van het product met nummer", lowest_count_product[0])
    print('In totaal hebben wij', total_products, 'producten in ons magazijn liggen')