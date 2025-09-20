import requests

cep = input("Digite o seu CEP: ")
via_cep = f"https://viacep.com.br/ws/{cep}/json/"

requisicao = requests.get(via_cep)

print(requisicao)
print(f"CEP: {requisicao.json()['cep']}")
print(f"RUA: {requisicao.json()['logradouro']}")
print(f"BAIRRO: {requisicao.json()['bairro']}")
print(f"CIDADE: {requisicao.json()['localidade']}")
print(f"ESTADO: {requisicao.json()['estado']}")
print(f"REGIÃO: {requisicao.json()['regiao']}")
print(f"DDD: {requisicao.json()['ddd']}")