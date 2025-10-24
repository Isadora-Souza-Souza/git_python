#Isadora Luiza Ferreira de Souza

votos = {
    "Candidato A": 0,
    "Candidato B": 0
}

for i in range(5):
    voto = input("Digite o nome do candidato (Candidato 'A' / Candidato 'B'): ")

    if voto in votos:
        votos[voto] +=1
    else:
        while voto not in votos:
            print("Candidato inválido! ")
            voto = input("Digite o nome do candidato (Candidato 'A' / Candidato 'B'): ")    

print(f"Resultado final da votação: ")
for candidato, total in votos.items():
    print(f"{candidato}: {total} votos")
if votos["Candidato A"] > votos["Candidato B"]:
    print(f"Vencedor: Candidato A. ")
else:
    print(f"Vencedor: Candidato B")

