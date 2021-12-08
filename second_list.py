def first_question(a):
    if a in ["a", "e", "i", "o", "u", ]:
        print("Vogal")
        return "Vogal"
    else:
        print("Consoante")
        return "Consoante"

assert(first_question("a") == "Vogal")
assert(first_question("b") == "Consoante")
assert(first_question("u") == "Vogal")
assert(first_question("c") == "Consoante")
assert(first_question("j") == "Consoante")

def second_question(a,b):
    media = (a + b) / 2
    if media >= 7:
        print("Aprovado")
        return "Aprovado"
    elif media >= 4 and media < 7:
        print("Final")
        return "Final"
    else:
        print("Reprovado")
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

def eighth_question():
    print("só amanha")