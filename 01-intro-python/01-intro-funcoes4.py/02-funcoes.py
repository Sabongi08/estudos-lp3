# Função 

# Quero somar uma lista de números 
# usar a função sun()

# Quero calcular a média dos alunos()
# 1. tem no python?
# 2. alguém já programou (copiar ou adcionar depedencia)
# 3. declarar 

# 1. Declaração 
# def nome_funcao(parametro1, parametro2):
#     return valor

# 2. Chamada

print('olá')
sum([1,3,5])
# nome_funcao('dad', 1)


# Função sem retorno e sem parâmetros
def imprimir_mensagem():
    print('vixiiii')

    imprimir_mensagem()
    imprimir_mensagem()

# Função sem retorno com parâmetros
# parâmetros vs argumentos 
# aqui tem um parametro, ou seja, nome
def saudacoes(nome):
    print(f'Bom dia (nome)')

# argumento para o parametro nome 'Maria'
saudacoes ('Maria')    

# argumento('Maria') para parametro nome 
nome_completo = 'José da Silva'
saudacoes (nome_completo)  


# Função com retorno e sem parâmetros
def obter_mensagem ();
    return 'vixiiiii'

mensagem = obter_mensagem ()
print(mensagem)

mensagem = obter_mensagem ()
print (obter_mensagem())

#só a função nn vai imprimir nd


# Função com retormo com parÂmetros (mlr)
def gerar_saudacao (nome):
    return f'bom dia!{nome}'

print (gerar_saudacao('Pedro'))
print (gerar_saudacao('Debs'))

#retorno   parametros 
# não      não 
# não      sim
# sim      não
# sim      sim (adequado)(função pura, smp vai devolver o msm resultado)

# imprimir saudacao
# saudacao = frase + nome 
# "Bom dia Pedro"
# "Boa tarde José"
# "Boa noite Rose"

# para ser dinamico precisa do parametro 

def saudacao(nome, frase):
    print(f'{frase} {nome}')

saudacao( 'João', 'Bom dia')


def saudacao(nome, frase):
    return (f'{frase} {nome}')
print(saudacao( 'João', 'Bom dia'))
# enviar email saudacao
# criar uma carta em pdf 

#Entrada
notas_alunos = [
    [9.0,7.0, 3.0 ],
    [2.0,6.0, 3.0 ],
    [5.0,5.0, 7.0 ],

]

# saída [5.5, 1.0, 6.5]

def calcular_media (notas):
    return sum(notas) /len(notas)

def calcular_media_alunos(notas_alunos):
    medias = [] #vai parar nessa lista

    for notas in notas_alunos:
        # [9.0,7.0, 3.0 ] 
        media = calcular_media (notas)
        medias.append (media) #ele irá adicionar um elemento no final da lista

    return medias 
# return [calcular_media(notas) for notas in notas_alunos]
todas_as_notas = [
    [9.0,7.0, 3.0 ],
    [2.0,6.0, 3.0 ],
    [5.0,5.0, 7.0 ],

]

def imprimir_medias (notas_alunos):
    medias= calcular_media_alunos(notas_alunos)
    print (medias)

def enviar_media_por_email (notas_alunos):
    medias = calcular_media_alunos (notas_alunos)
    # logica de enviar por email as medias

imprimir_medias(todas_as_notas)
enviar_media_por_email(todas_as_notas)


# Argumentos nomeados (ordem mlr)
def saudacao (nome, frase):
    return f'{frase} {nome}'

print (saudacao ('Joao', 'Bom dia'))
print (saudacao ( nome = 'Joao', 'Bom dia'))

# parametros com valor padarão (default)
def saudacao (nome, frase):
    return f'{frase} {nome}'

print(saudacao('Joao'))

# 
 
