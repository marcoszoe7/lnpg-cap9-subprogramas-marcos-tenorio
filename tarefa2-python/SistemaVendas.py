# Versão tarefa2 - monolítica

produto = input("Produto: ")
qnt  = int(input("Quantidade: "))
preco = float(input("Preço unitário: R$ "))

subtotal = qnt * preco

if subtotal > 500:
    desconto = subtotal * 0.10
elif subtotal > 200:
    desconto  = subtotal * 0.05
else:
    desconto = 0

total = subtotal - desconto

print ("\n === CUPOM FISCAL EMITIDO ===")
print(f"Produto: {produto}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total: R${total:.2f}")























