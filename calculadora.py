soma = 0
resposta = 'S'  

while resposta == 'S' or resposta == 's':
    num = float(input("Digite um número: "))
    soma = soma + num
    resposta = input("Deseja continuar? (S/N) ")

print(f"Soma dos números: {soma}")
