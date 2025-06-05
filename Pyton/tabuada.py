# i=int(input("Digite o numero a ser multiplicado: "))
# for x in range(11):
#     print(f"{i}*{x}= {i*x}")
# =================================================================================
# numero1, numero2 = map(int, input("Digite o dois numeros: ").split())
# for n in range(numero1+1, numero2):
#     print(n, end=' ')
# for n in range(numero1+1, numero2):
#     print(n)
#==================================================================================
# soma = 0
# numero = int(input("Informe a quantidade de numeros voce quer digitar: "))
# for i in range(numero):
#     n1 = int(input("Informe o numero: "))

# menor = 9999999999    
# maior = -999999999
# soma = 0
# numero = int(input("Informe a quantidade de números que você quer digitar: "))

# for i in range(numero):
#     n1 = int(input("Informe o número: "))
#     soma += n1

#     if i <= menor:
#         menor  = 1
    
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2:0])

#--------------------------------------------------------------------------

# n_pessoas = int(input("Informe quantas pessoas vão falar sua idade: "))
# soma = 0
# for n in range(n_pessoas):
#     idade = float(input("Informe sua idade: "))
#     soma += idade
# media = soma/n_pessoas
# print("A media é", media)
# if media > 0 and media <= 25:
#     print("Turma jovem")
# elif media > 26 and media < 60:
#     print("Turma adulta")
# elif media > 60:
    # print("Turma idosa")

#--------------------------------------------------------------------------------

pessoas_votaram = int(input("Informe a quantidade de votos: "))
bolsonaro = 0
lula = 0
ciro = 0
for v in range(pessoas_votaram):
    print("22 - Bolsonaro")
    print("13 - Lula")
    print("12 - Ciro")
    
    voto = input("Informe seu voto: ")

    if voto == "22":
         bolsonaro += 1
    elif voto == "13":
         lula += 1
    elif voto == "12":
         ciro += 1
    else:
         print("voto invalido, vote novamente")
if bolsonaro > lula and bolsonaro > ciro:
     print("Bolsonaro vencedor com", bolsonaro, "votos")
elif lula > bolsonaro and lula > ciro:
     print("Lula vencedor com", lula, "votos")
elif ciro > bolsonaro and ciro > lula:
     print("Ciro vencedor com", ciro, "votos")




 

 
