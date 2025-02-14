# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Todo mundo quer dominar o mundo - Lágrimas por medos
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

tarefas = []
tarefas_refazer = []

def listar(tarefas):
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa digitada')
        return
    tarefas.append(tarefa)

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
    'refazer': lambda: refazer(tarefas, tarefas_refazer),
    'clear': lambda: os.system('clear'),
    'adicionar': lambda: adicionar(tarefa, tarefas),
}
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()

    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     continue
    # elif tarefa == 'cls':
    #     os.system('cls')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     continue
