print("Progama que veriifca se o cpf e valido \n")
# variavel que guarda o cpf pelo usuario
cpf_usuario = input("digite o seu cpf")
# esssa variavel foi criada para calcular o peso de 10 ate 2
peso10 = 10
# a variavel resultado guarda soma das  multiplicaçoes entre os digitos do cpf e os pesos 
resultado = 0 

# para obter os 9 digitos do cpf foi nescessario usar uma estrutuara for de 0 a 9
for i in range(0,9):
    # exibindo um digito do cpf por vez em tela
    print(cpf_usuario[i])
    print(int(cpf_usuario[i])*peso10)
    # para calcular um digito por vez com foi nescessario conveter cada digito em numero inteiro depois somamos os resultados obtidos armazenando na variavel 
    resultado+=int(cpf_usuario[i])*peso10
    peso10-=1
    # todas as vezes q o laço for rodas sera substituido o valor 1 da varialvel peso10
    print(resultado)
    # exibindo o resultado encontrado 
resto= resultado % 11  
# a variavel resto guarda o resto da divisao 
# se o resto da divisao for menor que 2 entao o primeiro digito sera 0(zero); caso contrario o devemos subtrair 11 pelo valor encontrado em resto 
if(resto < 2):
    
    print("primeiro digito é 0\n")

else: 
    print("primeiro digito é "+str(11-resto))  