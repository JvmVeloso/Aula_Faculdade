#NUMERO 1
# nome = input("Qual é o seu nome? ")
# idade = int(input("Qual é a sua idade? "))
# peso = float(input("Qual é o seu peso? (em kg) "))
# altura = float(input("Qual é a sua altura? (em metros) "))
#
# if idade >= 18 and peso >= 60 and altura >= 1.70:
#     print(nome + ", você está apto a servir o exército.")
# else:
#     print(nome + ", você não está apto a servir o exército.")

#NUMERO 2
# frase = "Anotaram a data da maratona"
# print(frase[::-1])
# frase = frase.replace(" ", "").lower()
# if frase == frase[::-1]:
#     print("A frase é um palíndromo!")
# else:
#     print("A frase não é um palíndromo.")

#NUMERO 3
# dias = int(input("Dias: "))
# horas = int(input("Horas: "))
# minutos = int(input("Minutos: "))
#
# total_segundos = dias * 86400 + horas * 3600 + minutos * 60
#
# print("Total de segundos:", total_segundos)

#NUMERO 4
# velocidade = int(input("Insira sua velocidade média esperada em km/h: "))
# distancia = int(input("Insira a distancia da viagem em km: "))
# tempo = distancia/velocidade
#
# print("Tempo de viagem: %.2f horas"% tempo)

#NUMERO 5
# velocidade = float(input("Velocidade do carro (em km/h): "))
#
# if velocidade > 80:
#     multa = (velocidade - 80) * 5
#     print("Você foi multado por excesso de velocidade!")
#     print("Valor da multa: R$ %.2f" % multa)
# else:
#     print("Velocidade dentro do limite permitido.")

#NUMERO 6
# valor_casa = float(input("Valor da casa a comprar: R$ "))
# salario = float(input("Salário: R$ "))
# anos = int(input("Quantidade de anos a pagar: "))
# prestacao = valor_casa / (anos * 12)
# limite = salario * 0.3
# print("Valor da prestação mensal: R$ %.2f" % prestacao)
#
# if prestacao <= limite:
#     print("Empréstimo aprovado!")
# else:
#     print("Empréstimo reprovado. Valor da prestação excede 30% do salário.")

#NUMERO 7
# numero = int(input("Digite um número: "))
#
# print("Tabuada de multiplicação do", numero)
#
# for i in range(1, 11):
#     resultado = numero * i
#     print(numero, "x", i, "=", resultado)

#NUMERO 8
# dividendo = int(input("Digite o dividendo: "))
# divisor = int(input("Digite o divisor: "))
#
# while dividendo >= divisor:
#     dividendo = dividendo - divisor
#
# print("O resto da divisão é", dividendo)

#NUMERO 9
# a = int(input("Digite o comprimento do lado A: "))
# b = int(input("Digite o comprimento do lado B: "))
# c = int(input("Digite o comprimento do lado C: "))
#
# if a == b == c:
#     print("Triângulo equilátero")
# elif a == b or a == c or b == c:
#     print("Triângulo isósceles")
# else:
#     print("Triângulo escaleno")

#NUMERO 10
# def inverte_numero(numero):
#     numero_str = str(numero)
#     numero_invertido = numero_str[::-1]
#     return int(numero_invertido)

#NUMERO 11
# def contar_vogais(texto):
#     vogais = 'aeiouAEIOU'
#     num_vogais = 0
#     for letra in texto:
#         if letra in vogais:
#             num_vogais += 1
#     return f'A palavra tem {num_vogais} vogais'

#NUMERO 12
# def item_mais_frequente(lista):
#     contagem = {}
#     for item in lista:
#         if item in contagem:
#             contagem[item] += 1
#         else:
#             contagem[item] = 1
#     mais_frequente = max(contagem, key=contagem.get)
#     return f"O item mais frequente é '{mais_frequente}' e aparece {contagem[mais_frequente]} vezes"
#
# lista = [2, 7, 7, 7, '#', '#', '#', '@', 3, '#', 6]
# resultado = item_mais_frequente(lista)
# print(resultado) # Saída: O item mais frequente é '#' e aparece 4 vezes

#NUMERO 13
# palavra = input("Digite uma palavra: ").lower()
#
# if palavra == palavra[::-1]:
#     print(f"{palavra} é um palíndromo")
# else:
#     print(f"{palavra} não é um palíndromo")








