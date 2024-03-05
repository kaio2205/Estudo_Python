def cria_arquivo(none= "", ext="" ,cont="")->str:
    """a funçao cria arquivo recebe o nome do arquivo a extensao e por fim ao para inserir algo para inserir no arquivo e criar este arquivo no diretorio local"""
    f = open(none +"."+ext,"a")
    f.write(cont)
    f.close()
    return "arquivo criado com sucesso\n"
print(cria_arquivo("garrafa","csv","texto;mensagem;ola"))