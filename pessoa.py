#Solicitando os dados para o cadastro
nome_completo = input("Digite o nome: ")
email = input ("Digite o email: ")

#Criando o arquivo pesssoa.txt para gravação dos dados
arquivo = open("pessoa.txt", "a")
arquivo.write(f"{nome_completo} | {email}\n")
arquivo.close()