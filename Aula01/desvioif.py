#  pede um numero e verifica se e par ou impar 
numero = input("digite um numero: ")

# é nescessario realizar a conversao de texto para inteiro pois a funçao input sempre retrona  o valor utilizado texto Entao utilizamos a funçao int para converter a variavel numero em valor numerico inteiro e assim realizar  os calculos necessarios

numero = int (numero) 

if( numero %2 ==0 ):
    print("O numero digitado é par")
else: 
    print("o numero digitado é impar")    