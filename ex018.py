import math

angulo = float(input("Digite o ângulo: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O seno de {angulo} vale {sen :.2f}, o cosceno vale {cos :.2f} e a tangente vale {tan :.2f}")