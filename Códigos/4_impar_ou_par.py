# Solicitação ao usuário um número inteiro
numero = int(input("Informe um número inteiro: "))

# Verificação se o número é par ou ímpar, juntamente com a impressão do resultado
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
