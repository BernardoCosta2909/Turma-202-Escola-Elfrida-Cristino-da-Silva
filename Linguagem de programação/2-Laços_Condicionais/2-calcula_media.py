#crie um programa que pede para o usuario 
#digitar 3 notas de um aluno. Em seguida o programa
#deve calcular a media e mostrar na tela

while True:
 nota_1 = float(input("digite o valor da nota: "))
 nota_2 = float(input("digite o valor da nota: "))
 nota_3 = float(input("digite o valor da nota: "))

 media = (nota_1 + nota_2 + nota_3) / 3
 
 print("a media do aluno é: ", media)

 if media >= 6:
    print("O aluno foi APROVADO")

 else:
   print("O aluno foi REPROVADO")

 if media >= 8: print("O aluno foi um ALUNO DESTAQUE")

 if media < 5: print("O aluno precisa de REFORÇO")

 if media <= 0: print("Não sobrou nada pra esse Beta")

 if media >= 10: print("Esse é o Alfa Sigma de xique-xique,Bahia")

 saida = str(input("se deseja sair digite 'sair', se não aperte a tecla enter: "))
 if saida == "sair": break

 
 

 