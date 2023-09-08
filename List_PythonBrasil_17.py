print (f"Bem vindo a loja de tintas LeivaTintas!\n")

valor_lata = 80
valor_galao = 25

qtd_metros = float(input(f"Poderia escrever a área em metros quadrados que deseja pintar?\n"))
qtd_litros_cal = float(qtd_metros / 6)
qtd_litros_necessaria = (qtd_litros_cal*0.1) + qtd_litros_cal

qtd_latas_18L = qtd_litros_necessaria / 18 
qtd_latas_18L_int = round(qtd_latas_18L + 0.5)

qtd_galoes_3L = qtd_litros_necessaria / 3.6
qtd_galoes_3L_int = round(qtd_galoes_3L + 0.5)

#Comprando apenas 18 litros:
print(f"Você deverá comprar um total de {qtd_latas_18L_int} latas de tinta de 18 Litros.")

#Comprando apenas 3,6 litros:
print(f"Você deverá comprar um total de {qtd_galoes_3L_int} galões de tinta de 3,6 Litros")

#Comprando misturado:
qtd_a = qtd_litros_cal / 18
qtd_a1 = round(qtd_a + 0.5)
print(qtd_a1)


