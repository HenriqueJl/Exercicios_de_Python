n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = ((n1 + n2) / 2)
print("A nota média foi de {}".format(m))

if(m <= 7):{
print('O aluno está reprovado.')
} 
else:{
print('O aluno foi aprovado!')

}
    
"""
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = ((n1 + n2) / 2)
print("A nota média foi de {}".format(m))

print("Aluno aprovado" if(m>=7) else "Aluno reprovado")
"""
