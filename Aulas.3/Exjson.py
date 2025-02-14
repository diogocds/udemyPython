import json

pessoa  = {
    'nome' : 'Luiz Otávio 2' ,
    'sobrenome' : 'Miranda' ,
    'enderecos' : [
        { 'rua' : 'R1' , 'número' : 32 },
        { 'rua' : 'R2' , 'número' : 55 },
    ],
    'altura' : 1.8 ,
    'numeros_preferidos' : ( 2 , 4 , 6 , 8 , 10 ),
    'dev' : True ,
    'nada' : None ,
}
# Escreve para Arquivo Json
with  open ( 'Aulas.json' , 'w' , encoding = 'utf8' ) as  arquivo :
    json.dump(
        pessoa ,
        arquivo ,
        ensure_ascii= False,
        indent= 2,
    )
# Ler do Arquivo Json
with  open ( 'Aulas.json' , 'r' , encoding = 'utf8' ) as  arquivo :
    pessoa  =  json.load( arquivo )
    print(pessoa)
    print(type(pessoa))
    print ( pessoa [ 'nome' ])

