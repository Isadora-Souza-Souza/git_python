soma = 0
resposta = 'S'  


while resposta == 'S' or resposta == 's':
    num = float(input("Digite um número: "))
    soma = soma + num
    resposta = input("Deseja continuar? (S/N) ")

print(f"Soma dos números: {soma}")


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resposta = input("Deseja continuar? (S/N) ")
subtracao = num1 - num2

print(f"Subtração dos números: {subtracao}")
