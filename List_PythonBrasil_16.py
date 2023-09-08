#input do usuario
area = float(input("Forneça a área a ser pintada em metros quadrados(M²):\n"))

#varivel
qtd_litros_lata = 18

#operações
litros = float(area / 3)
latas = float(litros /qtd_litros_lata)
valor = float(latas*80)

print(f"Você deve comprar um total de {latas:.2f} latas, sendo o preço total de R${valor:.2f} ")


