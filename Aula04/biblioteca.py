import os
def boasvindas():
    print("Olá seja bem vindo")
    
def anobissexto(ano=0)->bool:
    rs = True
    if(ano % 4 != 0):
        rs = False
    return rs

def  pontas_lista(lista_num=[]):
     rs = []
     rs.append(lista_num[0])
     rs.append(lista_num[len(lista_num)-1])
     return rs
 
def maior_lista(lista_num=[])->int:
    m =lista_num[0]
    for i in lista_num:
        if i > m:
            m = i 
    return m
    
    
def segundo_maior_lista(lista_num=[])->int:
     lista_ordenada = sorted(lista_num) 
     rs = 0
     lista_ordenada - 2
     rs = lista_ordenada [len(lista_ordenada) - 2]
     return rs
 
def qual_maior(lista_num=[], maior=0)->int:
    lista_ordernada = sorted(lista_num)
    rs = 0 
    rs = lista_ordernada[len(lista_ordernada)-maior] 
    return rs

def limpa_tela():
    os.system("cls")