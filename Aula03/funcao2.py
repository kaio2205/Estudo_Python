def desconto (preço = 0.0, taxa =0.0):
    """A funçao desconto realiza um calculo
    de desconto recebendo o valor de preço de um produto e multiplica pelo valor da taxa e exibe o resultado em tela ao final"""
    vl_desc =preço * (taxa / 100)
    vl_fin  = preço - vl_desc 
    print(f"O valor de desconto é {vl_desc} e  o valor final é {vl_fin}")
    
desconto(800,7)    