print("Este progama analisa os valore digitados de 0 a 6 e diz o dia da semana:")
digito = input("entre com u numero de 0 a 6 \n")

match digito:
    case '0':
        print("Domingo")
    case '1':
        print("Segunda")  
    case '2':
        print("Terça") 
    case '3':
        print("Quarta")   
    case '4':
        print("Quinta") 
    case '5':
        print("Sexta")   
    case '6':
        print("Sabado")    
    case _:
        print("Valor incorreto. tente outra vez otario \n")
              