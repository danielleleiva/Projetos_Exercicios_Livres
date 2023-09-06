valor_hora = float(input("Quanto você ganha por hora?\nResposta:"))
qtd_hora = float(input("Quantas horas você trabalha por mês?\nResposta:"))

sal_bruto = int(valor_hora * qtd_hora)

inss = int(sal_bruto * 0.11)
sindicato = int(sal_bruto * 0.05)
imp_renda = int(sal_bruto * 0.08)
som_descontos = int(inss + sindicato + imp_renda)
sal_liquido = sal_bruto - som_descontos

print(f"+ Salário Bruto : R${sal_bruto},00")
print(f"- IR (11%) : R${imp_renda},00")
print(f"- INSS (8%) : R${inss},00")
print(f"- Sindicato (5%) : R${sindicato},00")
print(f"= Salário líquido : R${sal_liquido},00")