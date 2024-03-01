print("Este progama analisa os valore digitados de 0 a 9 mostram se voce pode rodar como o carro")
digito = input("entre com u numero de 0 a 9  \n")

match digito:
    case '1'| '2':
        print("placa final 1 e 2 nao pode rodar Segunda feira\n")  
    case '3'|'4':
        print("placa final 3 e 4 nao pode rodar Terça feira\n")  
    case '5'|'6':
        print("placa final 5 e 6 nao pode rodar Quarta feira\n") 
    case '7'|'8':
        print("placa final 7 e 8 nao pode rodar Quinta feira\n")   
    case '0'|'9':
        print("placa final 0 e 9 nao pode rodar Sexta feira \n") 
    
        
              