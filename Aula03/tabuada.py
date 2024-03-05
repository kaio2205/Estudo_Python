def montar_tabuada(numero=0):
    print("o progama pede numero pra fazer a tabuada")
    arq = open ("tabuata.txt", "a")
    for i in range (1,11):
        arq.write(str(numero) + "x" + str(i) + "=" + str(numero*i)+"\n")
    arq.close()
n = input("digite um numero")
montar_tabuada(int(n))        

