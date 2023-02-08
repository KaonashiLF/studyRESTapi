

def meu_metodo_soma(arg1, arg2):
    return arg1 + arg2



def meu_metodo_longo(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5



def soma_de_lista(lista):
    return sum(lista)


# O *args recebe uma quantidade de elementos desconhecidos e os trata como se fosse uma lista.


# Método com parâmetro *args recebe os valores e os trata como uma lista e retorna uma tupla quando tem string

# Se os argumentos recebidos forem string e número, não é possível fazer soma. Neste caso, retorna uma tupla com os valores inputados
def soma_com_args(*args):
    return args



# Os métodos genéricos geralmente recebem *args e *kwargs

#Args = Arguments
# ---------------------------
# Os argumentos de args não precisam ter a palavra chave. Pode ser string, lista, número etc.,por exemplo:
# 'Teste','Tá difícil estudar',5,6,[123,21,4]

#KWargs = Key Words Arguments
# ---------------------------
# Os argumentos de Kwargs precisam ter a palavra chave, por exemplo:
# nome='Lucas', idade=22

# =======================================================
# IMPORTANTE: Sempre é necessário colocar os ARGUMENTOS de args (pode ser lista, string, número etc.) antes do *kwargs.
# =======================================================
def metodo_kwargs(*args, **kwargs): # recebe **
    
    # Retorna originalmente em formato de tupla com todos os inputs do usuário
    print(args)
    
    # Retorna em formato de dicionário, com palavra chave
    print(kwargs)
    
    