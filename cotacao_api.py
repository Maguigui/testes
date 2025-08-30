import requests

awesome_api = ("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
requisicao = requests.get (awesome_api)
print (requisicao)

dolar_real = float(requisicao.json()['USDBRL']['bid'])
euro_real = float(requisicao.json()['EURBRL']['bid'])
btc_real =  float(requisicao.json()['BTCBRL']['bid'])

valor_real = float(input("Digite o valor em R$ "))

print (f"R${valor_real:.2f} em dolar ${valor_real / dolar_real:.2f}")
print (f"R${valor_real:.2f} em euro €{valor_real / euro_real:.2f}")
print (f"R${valor_real:.2f} em bitcoin BTC {valor_real / btc_real:.2f}")