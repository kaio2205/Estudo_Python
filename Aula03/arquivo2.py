nome_arquivo= input("digite o nome do arquivo  ")

extensao_arquivo = input("digite a extensao do arquivo ")

conteudo = input("digite o conteudo do arquivo ")

arq =open(nome_arquivo+"."+extensao_arquivo,"a")
arq.write(conteudo)
arq.close()
