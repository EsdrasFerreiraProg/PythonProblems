from math import sqrt


def first_question(a):
    if a in ["a", "e", "i", "o", "u", ]:

        return "Vogal"
    else:

        return "Consoante"

assert(first_question("a") == "Vogal")
assert(first_question("b") == "Consoante")
assert(first_question("u") == "Vogal")
assert(first_question("c") == "Consoante")
assert(first_question("j") == "Consoante")

def second_question(a,b):
    media = (a + b) / 2
    if media >= 7:

        return "Aprovado"
    elif media >= 4 and media < 7:

        return "Final"
    else:

        return "Reprovado"

assert(second_question(5,5)) == "Final"
assert(second_question(7,7)) == "Aprovado"
assert(second_question(3,3)) == "Reprovado"
assert(second_question(4,0)) == "Reprovado"

def third_question(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)

    lista.sort()

    return "Maior: " + str(lista[2]) + " Menor: " + str(lista[0])

assert(third_question(1,3,5)) == "Maior: 5 Menor: 1"
assert(third_question(6,2,0)) == "Maior: 6 Menor: 0"
assert(third_question(3,1,8)) == "Maior: 8 Menor: 1"
assert(third_question(2,1,9)) == "Maior: 9 Menor: 1"

def fourth_question(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)

    lista.sort()

    return "Compre o produto com o preço de: " + str(lista[0])

assert(fourth_question(5.1,6.8,1.5)) == "Compre o produto com o preço de: 1.5"
assert(fourth_question(4.45,2.1,9.7)) == "Compre o produto com o preço de: 2.1"
assert(fourth_question(4.65,15.45,11.6)) == "Compre o produto com o preço de: 4.65"

def fifth_question(a,b,c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()

    return(str(lista[0]) + " " + str(lista[1]) + " " + str(lista[2]))

assert(fifth_question(3,1,5)) == "1 3 5"
assert(fifth_question(4,6,2)) == "2 4 6"
assert(fifth_question(9,1,4)) == "1 4 9"

def sixth_question(a):
    if a in ["M", "V", "N"]:
        if a == "M":
            return "Bom dia!"
        elif a == "V":
            return "Boa tarde!"
        elif a == "N":
            return "Boa noite!"
    else:
        return "Valor Inválido!"

assert(sixth_question("M")) == "Bom dia!"
assert(sixth_question("N")) == "Boa noite!"
assert(sixth_question("V")) == "Boa tarde!"
assert(sixth_question("a")) == "Valor Inválido!"

def seventh_question(qtd_horas, valor_por_hora):
    salario_bruto = qtd_horas * valor_por_hora
    desconto_sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11
    desconto = 0

    if salario_bruto >= 900 and salario_bruto < 1500:
        desconto = "5"
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto >= 1500 and salario_bruto < 2500:
        desconto = "10"
        desconto_ir = salario_bruto * 0.1
    elif salario_bruto >= 2500:
        desconto = "20"
        desconto_ir = salario_bruto * 0.2

    salario = salario_bruto - desconto_ir - desconto_sindicato
    return "Salário Bruto : " + str(salario_bruto) + "\n" + "IR: " + str((int(desconto)/100)*salario_bruto) + "\n" + "Sindicato: " +  str(desconto_sindicato) + "\n" + "FGTS: " + str(fgts) + "\n" + "Total de descontos: " + str(desconto_ir + desconto_sindicato) + "\n" + "Salario Liquido: " + str(salario)

assert(seventh_question(5,220)) == "Salário Bruto : 1100" + "\n" + "IR: 55.0" + "\n" + "Sindicato: 33.0" + "\n" + "FGTS: 121.0" + "\n" + "Total de descontos: 88.0" + "\n" + "Salario Liquido: 1012.0"

def eighth_question(a): #1==Domingo-#2==Segunda-#3==Terça-#4==Quarta-#5==Quinta-#6==Sexta-#7==Sábado
    if a in [1,2,3,4,5,6,7]:
        if a == 1:
            return "Domingo"
        elif a == 2:
            return "Segunda"
        elif a == 3:
            return "Terça"
        elif a == 4:
            return "Quarta"
        elif a == 5:
            return "Quinta"
        elif a == 6:
            return "Sexta"
        elif a == 7:
            return "Sábado"
    else:
        return "Valor Inválido!"


assert(eighth_question(1)) == "Domingo"
assert(eighth_question(5)) == "Quinta"
assert(eighth_question(3)) == "Terça"
assert(eighth_question(7)) == "Sábado"
assert(eighth_question(2)) == "Segunda"
assert(eighth_question(8)) == "Valor Inválido!"

def ninth_question(a,b,c):
    import math

    if a == 0:
        return "Valor de A inválido"
    delta = (b*b) - (4*a*c)


    if delta < 0:
        return "Equação não possui raízes reais!" + "\n" + "O programa será encerrado!"
    elif delta == 0:
        return "A equação possui apenas uma raiz real: " + str(-b / 2*a)
    elif delta > 0:
        return "A equação possui duas raízes reais: " + "\n" + "x1 = " + str((-b + sqrt(delta)) / (2*a)) + "\n" + "x2 = " +  str((-b - sqrt(delta)) / (2*a))

assert(ninth_question(1,3,2)) == "A equação possui duas raízes reais: " + "\n" + "x1 = " + "-1.0" + "\n" + "x2 = " +  "-2.0"

def tenth_question(a):
    if a %  4 == 0:
        return "O ano é bissexto!"
    else:
        return "Não é bissexto!"

assert(tenth_question(1988)) == "O ano é bissexto!"
assert(tenth_question(1992)) == "O ano é bissexto!"
assert(tenth_question(1996)) == "O ano é bissexto!"
assert(tenth_question(1986)) == "Não é bissexto!"

def eleventh_question(b):
    a = str(b)

    if int(a) > 1000 or int(a) < 0:
        return "Valor inválido, programa encerrando"

    if int(a) >= 0 and int(a)< 10:
        return "O numero tem " + a + " unidades"

    elif int(a) >= 10 and int(a) < 100:
        return "O número tem " + a[0] + " dezenas e " + a[1] + " unidades"
    elif int(a) >= 100 and int(a) < 1000:
        return "O número tem " + a[0] + " centenas " + a[1] + " dezenas e " + a[2] + " unidades"

assert(eleventh_question(465)) == "O número tem 4 centenas 6 dezenas e 5 unidades"
assert(eleventh_question(785)) == "O número tem 7 centenas 8 dezenas e 5 unidades"
assert(eleventh_question(326)) == "O número tem 3 centenas 2 dezenas e 6 unidades"
assert(eleventh_question(1001)) == "Valor inválido, programa encerrando"
assert(eleventh_question(-5)) == "Valor inválido, programa encerrando"

def twelveth_question(valor_do_saque):
    b = valor_do_saque

    if valor_do_saque < 10 or valor_do_saque > 600:
        return "Não é possível sacar menos que dez ou mais que 600 reais nesse caixa eletrônico"

    lista_notas = [100,50,10,5,1]
    notas_fornecidas = []

    if valor_do_saque >= 10 and valor_do_saque < 100:
        while valor_do_saque != 0:
            if valor_do_saque - 50 >= 0:
                notas_fornecidas.append(50)
                valor_do_saque -= 50

            elif valor_do_saque > 10:
                notas_fornecidas.append(10)
                valor_do_saque -= 10

            elif valor_do_saque < 10:
                if valor_do_saque - 5 > 0:
                    valor_do_saque -= 5
                    notas_fornecidas.append(5)

                elif valor_do_saque > 0 and valor_do_saque < 5:
                    valor_do_saque -= 1
                    notas_fornecidas.append(1)

    elif valor_do_saque >= 100 and valor_do_saque <= 600:

        while valor_do_saque != 0:
            if valor_do_saque - 100 >= 0:
                notas_fornecidas.append(100)
                valor_do_saque -= 100

            elif valor_do_saque < 100 and valor_do_saque >= 50:
                notas_fornecidas.append(50)
                valor_do_saque -= 50

            elif valor_do_saque < 50 and valor_do_saque >= 10:
                notas_fornecidas.append(10)
                valor_do_saque -= 10

            elif valor_do_saque <= 10:
                if valor_do_saque - 5 > 0:
                    valor_do_saque -= 5
                    notas_fornecidas.append(5)

                elif valor_do_saque > 0 and valor_do_saque < 5:
                    valor_do_saque -= 1
                    notas_fornecidas.append(1)


    return notas_fornecidas

assert(twelveth_question(99)) == [50, 10, 10, 10, 10, 5, 1, 1, 1, 1]
assert(twelveth_question(256)) == [100, 100, 50, 5, 1]
assert(twelveth_question(1500)) == "Não é possível sacar menos que dez ou mais que 600 reais nesse caixa eletrônico"
assert(twelveth_question(540)) == [100, 100, 100, 100, 100, 10, 10, 10, 10]
assert(twelveth_question(599)) == [100, 100, 100, 100, 100, 50, 10, 10, 10, 10, 5, 1, 1, 1, 1]

def thirteenth_question(a,b,c,d,e): #a,b,c,d,e são booleanos
    contador = 0
    if a == True:
        contador+=1
    if b == True:
        contador +=1
    if c == True:
        contador += 1
    if d == True:
        contador += 1
    if e == True:
        contador += 1

    if contador == 0 or contador == 1:
        return "Classificacao nao existe"
    elif contador == 2:
        return "Suspeita"
    elif contador == 3 or contador == 4:
        return "Cumplice"
    elif contador == 5:
        return "Assassino"

def fourteenth_question(numero_litros_vendidos, tipo_combustivel):
    if tipo_combustivel == "A":

        if numero_litros_vendidos <= 20:
            desconto = numero_litros_vendidos * 0.03
        elif numero_litros_vendidos >20:
            desconto = numero_litros_vendidos * 0.05

    elif tipo_combustivel == "G":
        if numero_litros_vendidos <= 20:
            desconto = numero_litros_vendidos * 0.04
        elif numero_litros_vendidos > 20:
            desconto = numero_litros_vendidos * 0.06
    else:
        return "Tipo de combustivel invalido"

    if tipo_combustivel == "A":
        preco_total = (3.4*numero_litros_vendidos) - desconto
    elif tipo_combustivel == "G":
        preco_total = (4.5 * numero_litros_vendidos) - desconto

    return str(preco_total) + " Reais"

assert(fourteenth_question(20,"G")) == "89.2 Reais"
assert(fourteenth_question(32,"A")) == "107.2 Reais"
assert(fourteenth_question(54, "F")) == "Tipo de combustivel invalido"

def last_question(quilos_de_morangos, quilos_de_macas):
    if quilos_de_morangos <= 5:
        valor_morangos = 2.50*quilos_de_morangos
    elif quilos_de_morangos > 5:
        valor_morangos = 2.20*quilos_de_morangos
    if quilos_de_macas <= 5:
        valor_macas = 1.80*quilos_de_macas
    elif quilos_de_macas > 5:
        valor_macas = 1.5*quilos_de_macas

    desconto = 0

    if quilos_de_macas + quilos_de_morangos > 8 or valor_macas + valor_morangos > 25:
        desconto = 0.1

    if desconto == 0:
        valor_total = valor_macas + valor_morangos

    elif desconto == 0.1:
        valor_total = (valor_macas + valor_morangos)*0.1 + valor_morangos + valor_macas

    return "Valor a ser pago: " + str(valor_total)

assert(last_question(5,2)) == "Valor a ser pago: 16.1"
print(last_question(5,5)) == "Valor a ser pago: 23.65"