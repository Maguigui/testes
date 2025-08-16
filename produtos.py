letra = "s"
while letra == "s":
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto R$ "))
    qtd_produto = int(input("Digite a quantidade do produto: "))

    with open("produto.txt", "a") as arquivo:
        arquivo.write(f"{nome_produto} | {valor_produto} | {qtd_produto} \n")
    letra = input("Deseja adicionar outro produto? [s/n]").lower()
    if letra not in ["s", "n"]:
        print('Opção inválida, Digite "S" para sim e "N" para não')
        