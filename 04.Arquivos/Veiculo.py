import csv 
 
#armazena o endereço do csv em uma váriavel
dados = "veiculos.csv"

#Pedindo para abrir o arquivo em modo de leitura e guardar na váriavel
with open(dados, "r") as arquivo: 
    leitor = csv.DictReader(arquivo, delimiter=",")

for linha in leitor:
    print(linha)