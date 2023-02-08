# Bilbiotecas usadas
import datetime


# =======================================================
#                  EXECUTANDO CLASSES
# =======================================================

# Importando as classes do meu arquivo classes
from classes import *

# ======= Objeto 1 =======
lucas = Funcionario('Lucas',15000)
lucas.get_data()
# Retorna: {'Nome': 'Lucas', 'Salario': 6700.0}


# ======= Objeto 2 =======
marcos = Admin('Marcos', 35000)
marcos.get_data()
# Retorna: {'Nome': 'Marcos', 'Salario': 15000.0}

# Testando método de classe

novo_valor_aumento = 1.05
Funcionario.definir_novo_aumento(novo_valor_aumento)
# Sempre que uma nova instância for criada, ela receberá o aumento de 1.05


year_today = datetime.date.today().year
month_today = datetime.date.today().month
day_today = datetime.date.today().day

# Testando função estática
valida_dia_util = Funcionario.dia_util(
    datetime.date(
        year_today,
        month_today,
        day_today
    )
)

if valida_dia_util:
    print('Trabalho e estudo')
else:
    print('Descanse')
    
# -------------------------------------------------------



# =======================================================
#             TRABALHANDO COM *ARGS E *KWARGS
# =======================================================

from args_kwargs import *

meu_metodo_soma(10,40)
# Retorna 50

meu_metodo_longo(10, 20, 40, 5, 3)
# Retorna 78

lista_para_somar = [2,56,3,45,54,32,5,42,3]
soma_de_lista(lista=lista_para_somar)
# Retorna  242


x = soma_com_args('Teste','Tá difícil estudar',5,6,[123,21,4])
print(x)
print(type(x))
# Retorna ('Teste', 'Tá difícil estudar', 5, 6, [123, 21, 4])


metodo_kwargs(3,'string','Sem palavra chave',5,'Trata como lista', nome='Lucas', idade=22)