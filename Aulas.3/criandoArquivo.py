import os
# Criando arquivos com Python + Context Manager com
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreva ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Gerenciador de contexto - com (abre e fecha)
# Métodos úteis
# escrever, ler (escrever e ler)
# writelines (escrever várias linhas)
# procurar (mover o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gerar um arquivo json
# json.carregar
caminho_arquivo  =  'Aulas.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with  open ( caminho_arquivo , 'w', encoding='utf-8' ) as  arquivo : # Ja abre e fecha o arquivo.
  arquivo.write('Diogo\n')
  arquivo.write('Edereço:\n')
  arquivo.writelines(
    ('linha 3\n', 'Linha 4\n')
  )

with  open ( caminho_arquivo , 'r', encoding='utf-8' ) as  arquivo : # Ja abre e fecha o arquivo.
  print(arquivo.read())

os.unlink(caminho_arquivo) # Apaga o arquivo criado(remove tbm)
# os.rename(caminho_arquivo) renomea o Arquivo.