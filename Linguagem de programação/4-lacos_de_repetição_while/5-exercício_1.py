numeros = 1
soma = 0

while numeros != 0:
 numeros = int(input("\ndigite um número inteiro: "))
 soma += numeros 
 if numeros== 0: 
   break

print("\na soma dos números é: ", soma)