import string
import random

# manipulação de arquivo
nome_arquivo = str(input("Digite o nome do arquivo que você desenha guardar a senha\n"))
nome_arquivo = nome_arquivo, '.txt'
nome_arquivo = ''.join(nome_arquivo)
arquivo = open(nome_arquivo, 'x')
arquivo.close()
# inputs do usuário

quantidade_letras = int(input("Quantas letras você quer em sua senha?\n")) + 1
quantidade_numeros = int(input("Quantos números você quer em sua senha?\n")) + 1
quantidade_especiais = int(input("Quantos caracteres especiais você quer em sua senha?\n")) + 1

# variáveis essenciais
lista = []
contador1 = 1
contador2 = 1
contador3 = 1

# geração de letras aleatórias
while contador1 < quantidade_letras:
    letras = random.choice(string.ascii_lowercase)
    lista.append(letras)
    contador1 = contador1 + 1

# converção em str
str_lista = "".join(lista[1:9])

# convertendo para maiúscula
maiusluca_inicial = lista[0].upper()

# senha final
senha = [maiusluca_inicial, str_lista]

# loop para estar adicionando numeros/connversão para str
while contador2 < quantidade_numeros:
    num = str(random.randrange(0, 9))
    senha.append(num)
    contador2 = contador2 + 1

# loop para adiconar caracteres especiais/connversão para str
while contador3 < quantidade_especiais:
    lista_especial = ['!', '@', '#', '$', '%', '&',
                      '*', '.', ',', '<', '>', '/', '?']
    aleorio_especiais = random.choice(lista_especial)
    senha.append(aleorio_especiais)
    contador3 = contador3 + 1

saida = ''.join(senha)
# saida final
print(f"A lista tem {len(lista)} letras e os seguintes caracteres: {saida}")

arquivo = open(nome_arquivo, 'a')
arquivo.write(f'Senha:{saida}')
arquivo.close()
    