# Versão tarefa2 - modularizada

def ler_pruduto():
    produto = input("Produto: ")
    qnt  = int(input("Quantidade: "))
    preco = float(input("Preço unitário: R$ "))
    return produto, qnt, preco

def calcular_subtotal(qnt, preco):
    return qnt * preco

def calcular_desconto(subtotal):
    if subtotal > 500:
        return subtotal * 0.10
    elif subtotal > 200:
        return subtotal * 0.05
    return 0

def calcular_total(subtotal, desconto):
    return subtotal - desconto

def imprimir_cupom(produto, subtotal, desconto, total):
    print("\n=== CUPOM FISCAL ===")
    print(f"Produto:   {produto}")
    print(f"Subtotal:  R$ {subtotal:.2f}")
    print(f"Desconto:  R$ {desconto:.2f}")
    print(f"Total:     R$ {total:.2f}")

def main():
    produto, qnt, preco = ler_pruduto()
    subtotal = calcular_subtotal(qnt, preco)
    desconto = calcular_desconto(subtotal)
    total = calcular_total(subtotal, desconto)
    imprimir_cupom(produto, subtotal, desconto, total)

main()








