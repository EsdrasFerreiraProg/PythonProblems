
def insert_a_valid_note():
    while True:
        note = int(input("Type a note: "))
        if note in [1,2,3,4,5,6,7,8,9,10,0]:
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
    
    while (number_of_first_population < number_of_second_population) and (number_of_first_population != number_of_second_population):
        print(number_of_first_population)
        number_of_first_population += number_of_first_population * 0.03
        number_of_second_population += number_of_second_population * 0.015

    print(number_of_first_population)
    print(number_of_second_population)

def print_1_20():
    for i in range(0,21):
        print(str(i), end = ' ')

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
    print("Média é igual a: " + str(valor/10))

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

    for i in range(0,11):
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

    print("EVEN NUMBERS: " + str(even) + " ODD NUMBERS: "+ str(odd))

def fibonacci():
    index = int(input("TYPE N: "))
    start_value = [0,1]
    for i in range(index):
        start_value.append(start_value[i +1] + start_value[i])

    start_value.pop(0)
    start_value.pop(-1)

    return start_value

def factorial(number):
    if number == 1:
        return number
    else:
        return number*factorial(number-1)

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

def determine_prime(number: int):
    primes = [1,3,5,7]
    numbers = [2,3,4,5,6,7,8,9]
    condition = True

    if number in primes:
        return "It's prime!"

    for i in numbers:
        if number % i == 0:
            condition = False
            break

    if condition == True:
        return "It's prime dude!"
    else:
        return "Number is not prime!"

