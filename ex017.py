import math

c_oposto = float(input("Qual a medida do cateto oposto? "))
c_adj = float(input("Qual é a medida do cateto adjacente? "))

hip = (math.hypot(c_oposto, c_adj))

print(f"A hopotenusa do triângulo retângulo descrito é: {hip :.1f}")
