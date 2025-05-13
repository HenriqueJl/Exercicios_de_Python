km_percorrido = float(input("Quantos Km formam percorridos? "))
dia_alugado = float(input("Quantos dias você alugou o carro? "))

preço_total = (dia_alugado * 60) + (km_percorrido * 0.15)

print(f"O preço total dos dias alugado é de R${preço_total :.2f}")
