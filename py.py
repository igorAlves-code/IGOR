def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisão por zero."

def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    operacao = input("Digite o número da operação (1/2/3/4): ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite números válidos.")
        return

    if operacao == '1':
        print(f"O resultado da soma é: {somar(num1, num2)}")
    elif operacao == '2':
        print(f"O resultado da subtração é: {subtrair(num1, num2)}")
    elif operacao == '3':
        print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
    elif operacao == '4':
        print(f"O resultado da divisão é: {dividir(num1, num2)}")
    else:
        print("Operação inválida! Escolha entre 1, 2, 3 ou 4.")

calculadora()