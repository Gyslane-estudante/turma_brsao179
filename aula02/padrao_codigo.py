nome_usuario = "Gyslane"
idade_atual = 22
carrinho_compras = ["livro", "caneta", "caderno"]

def calcular_desconto(valor_original, percentual_desconto):
    desconto = valor_original * (percentual_desconto / 100)
    valor_com_desconto = valor_original - desconto
    return valor_com_desconto