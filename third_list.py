import json


def insert_a_valid_note():
    while True:
        note = int(input("Type a note: "))
        if note in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]:
            break
        else:
            print("Invalid value, keep trying")


def verify_password_equal_to_name():
    while True:
        name = input("Type your name: ")
        passwd = input("Type your password: ")
        if name == passwd:
            print("Try again, same name and password!!")
        else:
            break


def equal_population():
    number_of_first_population = 80000
    number_of_second_population = 200000

    while (number_of_first_population < number_of_second_population) and (
            number_of_first_population != number_of_second_population):
        print(number_of_first_population)
        number_of_first_population += number_of_first_population * 0.03
        number_of_second_population += number_of_second_population * 0.015

    print(number_of_first_population)
    print(number_of_second_population)


def print_1_20():
    for i in range(0, 21):
        print(str(i), end=' ')


def print_10():
    primeiro_valor = int(input("Digite o valor: "))
    for i in range(9):
        valor = int(input("Digite o valor: "))
        if valor < primeiro_valor:
            primeiro_valor = valor
    print(primeiro_valor)


def sum():
    valor = 0
    for i in range(10):
        valor += int(input("Digite o valor: "))
    print("Soma é igual a: " + str(valor))
    print("Média é igual a: " + str(valor / 10))


def print_odd_numbers():
    for i in range(1, 51, 2):
        print(str(i))


def print_integers():
    value1 = int(input("Type the first integer in interval: "))
    value2 = int(input("Type the second integer in interval: "))

    if value1 < value2:
        for i in range(value1, value2):
            print(str(i))
    else:
        for i in range(value2, value1, -1):
            print(str(i))


def tab_generator():
    valor = input("De que número queres a tabuada? ")
    print("Tabuada do " + valor + ":")

    for i in range(0, 11):
        print(str(valor) + " X " + str(i))


def pow():
    valor = 1
    base = int(input("Digite a base: "))
    potencia = int(input("Digite a potência: "))

    for i in range(potencia):
        valor *= base

    return valor


def amount_of_odds_and_even_numbers():
    even = 0
    odd = 0
    for i in range(10):
        number = int(input("TYPE A INTEGER: "))
        if number % 2 == 0:
            even += 1
        elif number % 3 == 0:
            odd += 1

    print("EVEN NUMBERS: " + str(even) + " ODD NUMBERS: " + str(odd))


def fibonacci():
    index = int(input("TYPE N: "))
    start_value = [0, 1]
    for i in range(index):
        start_value.append(start_value[i + 1] + start_value[i])

    start_value.pop(0)
    start_value.pop(-1)

    return start_value


def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


def major_minor_and_sum():
    values = []
    print("IF YOU WANT TO STOP THE READING, TYPE *STOP*")
    first_insert = input("TYPE THE NUMBER: ")
    if first_insert == "STOP":
        return "YOU DID NOT INSERTED ANY NUMBER!"

    while first_insert != "STOP":
        values.append(int(first_insert))
        first_insert = input("TYPE THE NUMBER: ")

    minor = values[0]
    major = values[0]
    sum = 0

    for i in values:
        sum += i
        if i < minor:
            minor = i
        if i > major:
            major = i

    return "Major = " + str(major) + "\n" + "Minor = " + str(minor) + "\n" + "SUM = " + str(sum)


def determine_prime(number: int) -> bool:
    primes = [1, 3, 5, 7]
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    condition = True

    if number in primes:
        return True

    for i in numbers:
        if number % i == 0:
            condition = False
            break

    if condition == True:
        return True
    else:
        return False


def age_mean(ages: tuple):
    sum = 0

    for i in ages:
        sum += i

    mean = sum / len(ages)

    if mean > 0 and mean <= 25:
        return "Young class!!"
    elif mean > 25 and mean <= 60:
        return "Adult class!!"
    else:
        return "Old class"


def mean_classes(classes: int, pupils: int):
    if pupils > 40:
        return "YOU CANT HAVE MORE THAN 40 PUPILS FOR CLASS"
    return str((pupils * classes) / classes) + " PUPILS MEAN"


def mean_cds(cds_amount: int, paid_value: float):
    return str((cds_amount * paid_value) / cds_amount) + " CD'S MEAN"


def one_ninety_nine_store():
    value = 1.99
    string = ""

    for i in range(1, 51):
        string += str(str(i) + " - R$ " + str(value * i) + "\n")

    return "Almost Two Store - Price Table: \n" + string


def beyond_ninety_nine():
    sum_commodities = 0
    condition = "S"

    while condition == "S" or condition == "s":
        print("Lojas Tabajara")
        product = 0
        while True:

            product_price = float(input("Produto " + str(product) + ": R$ "))
            sum_commodities += product_price
            product += 1

            if product_price == 0:
                break

        print("Total: " + str(sum_commodities))
        money_amount = float(input("Money: "))
        print("Money back: " + str(sum_commodities - money_amount))

        condition = input("Type <S> if you want to continue using the software: ")


def accidents(listy_of_tuples: list):
    minor_index_of_accidents = listy_of_tuples[0]["number_of_accidents"]
    major_index_of_accidents = listy_of_tuples[0]["number_of_accidents"]
    sum_for_mean_of_vehicles = 0
    city_major = ""
    city_minor = ""

    for i in listy_of_tuples:
        for key, value in i.items():
            if key == "code":
                city = value
            if key == "number_of_accidents" and value < minor_index_of_accidents:
                minor_index_of_accidents = value
                city_minor = city
            if key == "number_of_accidents" and value > major_index_of_accidents:
                major_index_of_accidents = value
                city_major = city

            if key == "number_of_cars":
                sum_for_mean_of_vehicles += value

    return "MAJOR NUMBER OF CARS ACCIDENTS: " + str(
        major_index_of_accidents) + ", CITY OF MAJOR OCCURANCE: " + city_major + "\n" + "MINOR NUMBER OF CAR ACCIDENTS: " \
                                                                                        "" + str(
        minor_index_of_accidents) + "\n" + "MEAN OF CARS IN FIVE CITIES: " + str(sum_for_mean_of_vehicles / 5)


def minor_and_major_note(mydict: dict):
    minor = 10000
    major = 0
    minor_pupil_name = ""
    major_pupil_name = ""

    for key, value in mydict.items():
        if value < minor:
            minor = value
            minor_pupil_name = key
        if value > major:
            major = value
            major_pupil_name = key

    return "GREATEST PUPIL NOTE AND NAME: " + str(
        major) + ", " + major_pupil_name + "\n" + "WORST PUPIL NOTE AND NAME: " + str(minor) + ", " + minor_pupil_name


def how_many_alumns(mydict):
    counter = 0

    for key in mydict.keys():
        counter += 1
    return counter


def calculate_mean(mydict):
    counter = 0
    counter_of_how_many_values = 0
    for value in mydict.values():
        counter += value
        counter_of_how_many_values += 1

    return "MEAN: " + str(counter / counter_of_how_many_values)


def print_templates(questions_answered: tuple, correct_answers: tuple):
    import ast
    mydict = {}

    with open("dicts.txt", "r") as file:
        a = file.readline()

    if a != "":
        with open("dicts.txt", "r") as read_file:
            mydict = (read_file.read())
            mydict = ast.literal_eval(mydict)

    while True:
        your_name = input("<0> BREAK PROGRAM\n"
                          "<1> LIST MINOR AND MAJOR NOTE\n"
                          "<2> COUNT HOW MANY STUDENTS HAVE ACESSED THE SOFTWARE\n"
                          "<3> CALCULATE THE CLASS MEAN\n"
                          "<DIGIT YOUR NAME> JUST TYPE YOUR NAME: ")
        if your_name == "0":
            break
        elif your_name == "1":
            print(minor_and_major_note(mydict))
            break
        elif your_name == "2":
            print(how_many_alumns(mydict))
            break
        elif your_name == "3":
            print(calculate_mean(mydict))
            break

        corrects = 0

        for i in range(len(questions_answered)):
            if questions_answered[i] == correct_answers[i]:
                corrects += 1

        mydict[your_name] = corrects

        print(mydict)
    with open("dicts.txt", "w") as file:
        file.write(str(mydict))


def invert_integer(integer: int):
    integer = str(integer)

    return integer[::-1]


def sum_serie(many_times: int):
    counter = 0
    string = ""
    numerator = 1
    denominator = 1
    sum = 0

    while counter != many_times:
        string += str(numerator) + "/" + str(denominator)
        string += " + "
        numerator += 1
        denominator += 2
        counter += 1
        sum += numerator / denominator

    return string[0:-3] + "\n" + "SOMA: " + str(sum)


def sum_serie2(many_times: int):
    counter = 0
    string = ""
    numerator = 1
    denominator = 1
    sum = 0

    while counter != many_times:
        string += str(numerator) + "/" + str(denominator)
        string += " + "

        denominator += 1
        counter += 1
        sum += numerator / denominator

    return string[0:-3] + "\n" + "SOMA: " + str(sum)


def list_of_prime_numbers(stop: int):
    my_list = list(range(1, stop + 1))
    final_list = []

    for i in my_list:
        if determine_prime(i) == True:
            final_list.append(i)

    return final_list

