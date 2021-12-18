
def first_word(palavra):
    aux = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            break
        elif palavra[i] != " ":
            aux += palavra[i]


    print(aux)

def find_zeros(a):
    aux = str(a)
    contador = 0
    for i in reversed(aux):
        if i == "0":
            contador += 1
        else:
            break
    print(contador)

def list_with_no_number(a,b): ## ([1,2,3,3,4,5], 3) ==  [3,3,4,5]
    lista_auxiliar = []
    aux = 0

    for i in range(len(a)):
        if a[i]==b:
            aux = i
            break
    print(aux)
    while True:
        if aux == len(a):
            break
        lista_auxiliar.append(a[aux])
        aux += 1

    print(lista_auxiliar)

def all_upper(a):
    booleano = True
    for i in a:
        if i != i.upper():
            booleano = False
    return booleano

def split(a): ##assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    lista = []
    exemplo = ""
    contador_auxiliar = 0
    contador = 0

    while True:
        if contador_auxiliar == len(a):
            break
        exemplo += a[contador]
        contador += 1
        contador_auxiliar += 1

        if contador_auxiliar % 2 == 0:
            lista.append(exemplo)
            exemplo = ""
        elif contador_auxiliar == len(a):
            break

    if len(a) % 2 != 0:
        exemplo_2 = ""
        exemplo_2+=(a[-1])
        exemplo_2+="_"
        lista.append(exemplo_2)


    return lista

def zeros_in_beggining(a):
    contador = 0

    for i in a:
        if i=="0":
            contador += 1
        else:
            break
    print(contador)

def nearest_value(a,K):
    lst = []

    for i in a:
        lst.append(i)

    print(lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))])

def between_markers1(a,b,c):  ##assert between_markers('What is >apple<', '>', '<') == "apple"
    condition = False
    string = ""
    for i in a:
        if i == b:
            condition = True
            continue
        if i == c:
            condition = False
        if condition == True:
            string += i
    return string

def correct_sentence(a):
    string = ""
    if a[-1] != ".":
        a += "."
    string += a[0].upper()

    condicao = True

    for i in a:

        if condicao == True:
            condicao = False
            continue

        string += i

    return string

def sum_numbers(a):
    soma = 0
    lista = []
    string = ""
    condicao = True

    a += "."

    for i in range(len(a)):
        if a[i] == "1" or a[i] == "2" or a[i] == "3" or a[i] == "4" or a[i] == "5" or a[i] == "6" or a[i] == "7" or a[i] == "8" or a[i] == "9" or a[i] == "0":
            string += a[i]
        if a[i] == " " and (a[i-1] == "1" or a[i-1] == "2" or a[i-1] == "3" or a[i-1] == "4" or a[i-1] == "5" or a[i-1] == "6" or a[i-1] == "7" or a[i-1] == "8" or a[i-1] == "9" or a[i-1] == "0"):
            lista.append(string)
            string = ""
        elif a[i] == "." and (a[i-1] == "1" or a[i-1] == "2" or a[i-1] == "3" or a[i-1] == "4" or a[i-1] == "5" or a[i-1] == "6" or a[i-1] == "7" or a[i-1] == "8" or a[i-1] == "9" or a[i-1] == "0"):
            lista.append(string)
            string = ""

    for i in lista:
        soma += int(i)

    return soma

def fix(a):
    multiplier = 0
    if a == []:
        return 0

    for i in range(0,len(a),2):
        multiplier += a[i]

    multiplier *= a[-1]
    return multiplier

def checkio(a):
    string = ""
    lista = []
    a += " "
    special_number = 0
    counting_three_strings = 0
    first_condition = None
    second = None
    third = None

    for i in a:
        if i != " ":
            string += i
        elif i == " ":
            lista.append(string)
            string = ""

    special_number = len(lista) - 2

    if len(lista) < 3:
        return False

    for i in range(special_number):
        for h in lista[i]:
            if h in ["1","2","3","4","5","6","7","8","9","0"]:
                first_condition = False
            else:
                first_condition = True

        for h in lista[i+1]:
            if h in ["1","2","3","4","5","6","7","8","9","0"]:
                second = False
            else:
                second = True

        for h in lista[i+2]:
            if h in ["1","2","3","4","5","6","7","8","9","0"]:
                third = False
            else:
                third = True

        if first_condition == True and second == True and third == True:
            counting_three_strings += 1

    if counting_three_strings >= 1:
        return True
    else:
        return False

def first_word(a: str):
    a = a.strip()

    string = ""
    strings_lowercase =  ["a","b","c","d", "'","e","f","g","h","i","j","k","l","m",
                 "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    strings_uppercase = []

    for i in strings_lowercase:
        strings_uppercase.append(i.upper())

    strings_lowercase = strings_lowercase + strings_uppercase

    condition = False

    for i in a:
        if i in strings_lowercase:
            condition = True
            string += i
        elif (i == " " or i == "." or i == ",") and condition == True:
            break

    return string

def count_digits(a): # hi my name 1938 is 1839 and12io
    list = []
    auxiliar_string = ""
    condicao = False
    a += " "
    strings_lowercase = ["a", "b", "c", "d", "'", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", " ", "."]
    strings_uppercase = []

    for i in strings_lowercase:
        strings_uppercase.append(i.upper())

    strings_lowercase = strings_lowercase + strings_uppercase

    for i in a:
        if i in ["1","2","3","4","5","6","7","8","9","0"]:
            condicao = True
            auxiliar_string += i

        elif condicao == True and i in strings_lowercase:
            list.append(auxiliar_string)
            auxiliar_string = ""
            condicao = False

    numero_digitos = 0

    for i in range(len(list)):
        for h in list[i]:
            numero_digitos += 1

    return numero_digitos

def backward_string_by_word(a):
    list = []
    auxiliar_string =  ""
    condicao = False
    a += " "
    strings_lowercase = ["a", "b", "c", "d", "'", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "á", "é", "í", "ó","ú"]
    strings_uppercase = []

    for i in strings_lowercase:
        strings_uppercase.append(i.upper())

    strings_lowercase = strings_lowercase + strings_uppercase


    for i in a:

        if i in strings_lowercase:
            auxiliar_string += i

        elif i == " ":

            list.append(auxiliar_string)
            auxiliar_string = ""
            list.append(" ")

        nova_string = ""
        list2 = []

        for i in list:
            for char in reversed(i):
                nova_string += char

            list2.append(nova_string)
            nova_string = ""

        final_string = ""

        for i in list2:
            final_string += i

    return final_string.strip()

def bigger_price(a, b):
    lista = []
    lista2 = []

    for i in b:
        if "price" in i:
            lista.append(i["price"])
    lista.sort()
    lista.reverse()

    condicao = 0
    condicao2 = a

    while condicao != condicao2:
        for i in b:
            if i["price"] == lista[condicao]:
                lista2.append(i)

        condicao += 1

    return lista2

def between_markers(text: str, begin: str, end: str) -> str:
    condition = False
    str_first_verification = ""
    str_second_verification = ""
    final_string = ""
    first_index = 0
    second_index = 0

    if len(begin) > 1 and len(end)>1:

        for i in range(len(text)):
            if text[i] == begin[0] and text[i+1] == begin[1]:

                for h in range(i, len(text)):
                    str_first_verification += text[h]
                    if text[h] == begin[-1]:
                        break

        for i in range(len(text)):
            if text[i] == end[0] and text[i+1] == end[1]:
                for h in range(i, len(text)):
                    str_second_verification += text[h]
                    if text[h] == end[-1]:
                        break
                break

        if str_first_verification == begin and str_second_verification == end: ##has begin and end
            for i in range(len(text)):
                if text[i] == begin[-1] and text[i-1] == begin[-2]:

                    for h in range(i+1, len(text)):
                        if text[h] == end[0] and text[h+1] == end[1]:
                            break
                        final_string += text[h]

        elif str_first_verification == begin and str_second_verification != end: ## has begin but no end
            for i in range(len(text)):
                if text[i] == begin[-1] and text[i-1] == begin[-2]:
                    for h in range(i+1, len(text)):
                        final_string += text[h]

        elif str_first_verification != begin and str_second_verification == end:
            for i in range(len(text)):
                if text[i] == end[0] and text[i+1] == end[1]:
                    break

                final_string += text[i]
        elif str_first_verification != begin and str_second_verification != end:
            return text

    elif len(begin) == 1 and len(end) == 1:

        for i in range(len(text)):
            if text[i] == begin:
                first_index = i

            if text[i] == end:
                second_index = i
        if first_index < second_index:

            for i in range(len(text)):
                if text[i] == begin:
                    for h in range(i+1, len(text)):
                        if text[h] == end:
                            break
                        final_string += text[h]

    return final_string

def find_exclusive(a: list) -> list:

    mydict = {}
    minor = 10000
    searched_key = []
    first_condition = False
    second_condition = False

    for first in a:
        mydict.update({first: 0})

    ##two conditions: first one: the values always have to be different of each other, second: if there is one value being repeated like [1,1,1,1,1]
    ##the program must return the list

    if len(mydict) == 1 and len(a) > 1:
        return a

    for i in a:
        counter = 0
        for h in a:
            if i == h:
                counter += 1

        mydict[i] = counter

    for key, value in mydict.items():
        if value < minor:
            minor = value

    required_keys = []
    reference_for_difference = mydict[a[0]]
    reference_for_difference2 = list(mydict.keys())[0]

    for key, value in mydict.items():
        if value != reference_for_difference:

            first_condition = True

        if key != reference_for_difference2:
            second_condition = True

    for key,value in mydict.items():
        if value == minor:
            required_keys.append(key)

    for h in required_keys:
        for i in range(len(a)):
            if a[i] == h:
                a.pop(i)
                break

    if first_condition == True:

        return a
    else:
        return []

def find_popularity(text: str, list: list) -> dict:
    words = text.split("\n")
    string = ""

    for i in words:
        string += i
        string += " "

    string = string.strip()
    words = string.split(" ")

    new_string = []
    mydict = {}

    for i in words:
        new_string.append(i.lower())

    for i in list:
        mydict[i] = 0

    for key, value in mydict.items():
        for i in new_string:
            if i == key:
                mydict[key] += 1

    return mydict

def second_index(string: str, search: str):
    condition = 0
    if search == " " and " " not in string:
        return None

    for i in range(len(string)):

        if string[i] == search and condition == 1:
            return i
        if string [i] == search:
            condition += 1









