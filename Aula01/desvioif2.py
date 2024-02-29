n1 = input ("digite a primeira nota do aluno: ")
n2 = input ("digite a segunda nota do aluno: ")
n3 = input ("digite a terceira nota do aluno: ")
n4 = input ("digite a quarta nota do aluno: ")
rs = (int(n1)+int(n2)+int(n3)+int(n4)) /4
print("a sua media é "+str(rs)+",entao voce esta: ")
# se o aluno tver uma media acima ou igual a 7 entao estara aprovado senao se a media for abaixo ou igual a 4 entao estara reprovado e por fim caso contrio estara em recuperaçao 

if (rs >= 7):
    print("aprovado")
elif(rs <= 4):
    print("reprovado")
else:
    print("recuperaçao")        