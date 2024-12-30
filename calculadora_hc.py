resp="Sim"
print("Olá, Seja bem vindo a Calculadora do Homem das Cavernas!! Só fazemos operações com dois números, mas já fica melhor que contar com pedras e gravetos.")
print("Por favor informe quais os dois números que deseja trabalhar, um de cada vez")

while resp=="Sim":
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  print("Informe qual operação deseja realizar:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  operaçao = int(input("Digite o número da operação desejada: "))

  if operaçao == 1:
    soma = num1 + num2
    print("O resultado da soma é: ", soma)
  elif operaçao == 2:
    subtracao = num1 - num2
    print("O resultado da subtração é: ", subtracao)
  elif operaçao == 3:
    multiplicacao = num1 * num2
    print("O resultado da multiplicação é: ", multiplicacao)
  elif operaçao == 4:
    divisao = num1 / num2
    print("O resultado da divisão(",num1,"/",num2, ") é = ", divisao)
    print("Deseja inverter os números da divisão? Responda Sim ou Não")
    inv = input()
    if inv == "Sim":
      divisao = num2 / num1
      print("O resultado da divisão(",num2,"/",num1, ") é = ", divisao)
  else:
    print("Operação inválida")

  print("Deseja fazer outra operação? Responda Sim ou Não")
  resp = input()
