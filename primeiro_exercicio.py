def valor_combustivel():  ##questao1
    valor_litro = float(input("Qual o valor do litro do combustível?"))
    valor_dinheiro = float(input("Qual o valor que desejas colocar?"))
    litros = valor_dinheiro / valor_litro
    print(litros)


def media_consumo():
    valor_inicial = float(input("Qual o valor do KM inicial?"))
    valor_final = float(input("Qual o valor do KM final?"))
    litros_gastos = float(input("Quantos litros foram gastos?"))
    consumo = str((valor_final - valor_inicial) / litros_gastos)
    print("O carro faz " + consumo + " km com um litro")


def valor_divida():
    valor_original = float(input("Valor original da dívida: "))
    qtd_dias_atraso = int(input("Dias atraso: "))
    valor_multa_dia = float(input("Qual o valor da multa por dia de atraso? "))
    valor_a_ser_pago = str((valor_multa_dia * qtd_dias_atraso) + valor_original)
    print("Sua dívida total é de: " + valor_a_ser_pago + " reais")


def area_total_casa():
    largura_comodo_1 = float(input("Largura do primeiro cômodo: "))
    comprimento_comodo_1 = float(input("Comprimento do primeiro cômodo: "))
    largura_comodo_2 = float(input("Largura do segundo cômodo: "))
    comprimento_comodo_2 = float(input("Comprimento do segundo cômodo: "))
    largura_comodo_3 = float(input("Largura do terceiro cômodo: "))
    comprimento_comodo_3 = float(input("Comprimento do terceiro cômodo: "))
    largura_comodo_4 = float(input("Largura do quarto cômodo: "))
    comprimento_comodo_4 = float(input("Comprimento do quarto cômodo: "))

    area_total = str((largura_comodo_1 * comprimento_comodo_1) + (largura_comodo_2 * comprimento_comodo_2) + (
                largura_comodo_3 * comprimento_comodo_3) + (largura_comodo_4 * comprimento_comodo_4))
    print("Área total: " + area_total + " m2")


def conversao():
    cotacao_dolar = float(input("DIGITE A COTACAO ATUAL DO DOLAR: "))
    quantos_reais_deseja_converter = float(input("QUANTOS REAIS DESEJA CONVERTER? "))
    valor_total = str(quantos_reais_deseja_converter / cotacao_dolar)
    print("O valor convertido e: " + valor_total + " dolares")


def novo_salario():
    salario_atual = float(input("Qual o salário atual: "))
    percentual_reajuste = float(input("Percentual reajuste: "))
    salario_total = str(salario_atual + ((percentual_reajuste / 100) * salario_atual))
    print("Seu salário agora é: " + salario_total + " reais")


def ficar_rico():
    salario_mensal = float(input("DIGITE O SALARIO MENSAL: "))
    despesas = float(input("DIGITE AS DESPESAS MENSAIS: "))
    valor_a_calcular = salario_mensal - despesas
    qtd_anos = str((1000000 / valor_a_calcular) // 12)
    print("A QUANTIDADE DE ANOS PARA A BUFUNFA RENDER UM MILHAO E: " + qtd_anos + " anos")


def ler_valor_inteiro():
    valor = int(input("DIGITE O INTEIRO AI: "))
    print(str(valor - 2) + " " + str(valor - 1) + " " + str(valor) + " " + str(valor + 1) + " " + str(valor + 2))


def idade():
    nome = str(input("Digite seu nome: "))
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    fez_aniversario = str(input("Ja fez aniversario? s/n "))
    if fez_aniversario == "s":
        print(nome + " tem " + str(2021 - ano_nascimento) + " anos")
    else:
        print(nome + " tem " + str((2021 - ano_nascimento) - 1) + " anos")


def ultima():
    largura_sala = float(input("Largura da sala: "))
    comprimento_sala = float(input("Comprimento da sala: "))
    largura_cadeira = float(input("Largura da cadeira: "))
    comprimento_cadeira = float(input("Comprimento da cadeira: "))
    largura_real = largura_sala - (largura_sala * 0.5)
    comprimento_real = (comprimento_sala - (comprimento_sala * 0.2)) - 1.5
    area_final = largura_real * comprimento_real
    area_final_carteira = largura_cadeira * comprimento_cadeira
    qtd_cadeiras = area_final // area_final_carteira
    print("A QUANTIDADE DE CADEIRAS SUPORTADA É: " + str(qtd_cadeiras) + " DE CADEIRAS")


def primeira_palavra(palavra):
    aux = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            break
        elif palavra[i] != " ":
            aux += palavra[i]


    print(aux)


def descobre_zeros(a):
    aux = str(a)
    contador = 0
    for i in reversed(aux):
        if i == "0":
            contador += 1
        else:
            break
    print(contador)

def lista_sem_um_numero(a,b): ## ([1,2,3,3,4,5], 3) ==  [3,3,4,5]
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

def corrige(a):
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

assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site"
assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi'
assert between_markers('No hi', '[b]', '[/b]') == 'No hi'
assert between_markers('No <hi>', '>', '<') == ''
print(between_markers("No <hi> one",">","<"))










