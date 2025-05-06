preço = float(input("Consulte o preço: "))

liquidação = (preço * 0.05)
preço_final = (preço - liquidação)

print(f"O preço em liquidação é de: R$ {preço_final}")