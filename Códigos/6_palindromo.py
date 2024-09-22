# Solicitação de uma palavra ou frase ao usuário
palavra = input("Informe uma palavra ou frase: ")

# Remoção dos espaços e transformação da palavra para letras minúsculas (caso tenha letras maiúsculas)
palavra_limpa = palavra.replace(" ", "").lower()

# Verificação de que se a palavra é um palíndromo, juntamente com a impressão do resultado
if palavra_limpa == palavra_limpa[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
