def calcular_faturamento_liquido(vendas_brutas, taxa_imposto, custos_operacionais):
    # Calcula o imposto sobre as vendas
    valor_imposto = vendas_brutas * taxa_imposto
    # Calcula o faturamento líquido deduzindo impostos e custos
    faturamento_liquido = vendas_brutas - valor_imposto - custos_operacionais
    return faturamento_liquido

def verificar_bonus(faturamento, meta):
    # Verifica se o faturamento atingiu a meta para liberar o bônus
    if faturamento >= meta:
        breakpoint
        print("Meta atingida! Bônus liberado.")
    else:
        print("Meta não atingida.")

# PROGRAMA PRINCIPAL
vendas_loja =  100000
imposto = 0.10          # 15%
custos = 200000
meta_ano = 600000     # Meta estipulada
print("Iniciando análise financeira...")

faturamento_final = calcular_faturamento_liquido(vendas_loja, imposto, custos)
print(f"Faturamento Líquido Calculado: R$ {faturamento_final}")

verificar_bonus(faturamento_final, meta_ano)
breakpoint
