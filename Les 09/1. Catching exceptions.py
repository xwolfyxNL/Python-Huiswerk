def get_cost(a):
    count = input("How many people are in your group: ")
    try:
        4356 / int(count)

        if 0 > int(count):
            print("Count = {0} - Negative numbers aren\'t allowed!".format(count))
        else:
            print("Each off the {0} people will have to pay €{1:.2f}".format(count, 4356 / int(count)))
    except ZeroDivisionError:
        print("Count = {0} - Division by zero isn't allowed".format(count))
    except ValueError:
        print("Please use numbers only")
    except Exception:
        print('Onjuiste invoer!')


price = 4356
get_cost(price)