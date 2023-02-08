# Decoradores utilizam a biblioteca functools

# Decoradores basicamente tem poder de transformar uma função
# Pode ser utilizado para acesso de usuário, por exemplo

import functools



def meu_decorador(funcao):
    @functools.wraps(funcao)
    
    def func_que_roda_funcao():
        print('*************Embrulhando função no decorador!*************')
        funcao()
        print('*************Fechando o embrulho*************')
    return func_que_roda_funcao


@meu_decorador
def minha_funcao():
    print('Eu sou uma função e serei embrulhada e executada dentro de outra função.')
    

minha_funcao()
