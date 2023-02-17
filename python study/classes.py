

# ============================
# Criação de classe
# ============================


# Classe funcionário que terá funções básicas de um funcionário de uma empresa
class Funcionario():
    
    # Sempre que um objeto desta CLASSE for instanciado, ele precisará conter os parâmetros de nome e salario
    
    # 4% de aumento
    # Toda instância irá acessar esta variável aumento
    aumento = 1.04
    
    
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario
        
    def get_data(self):
        dados = {'Nome':self.nome, 'Salario':self.salario}
        return dados
    
    # Função para aplicar aumento
    def aplicar_aumento(self):
        self.salario = self.salario * self.aumento
    
    # ============================
    # Método de classe
    # ============================
    
    
    # Este é um tipo de método que é aplicado na CLASSE e não nos objetos, ou seja, se eu quero definir um aumeneto de 5%, eu faço "instancia" desta CLASSE aplicando 1.05 (parâmetro novo_aumento) e TODOS os objetos instanciados após a chamada deste método terão o aumento de 5%
    
    # Todo método de classe recebe cls pois a "execução" está sendo aplicada na classe. Nos métodos normais recebem self pois indica um característica do objeto.
    
    @classmethod
    def definir_novo_aumento(cls, novo_aumento): 
        
        cls.aumento = novo_aumento
        
        
        
    # ============================
    # Método estático
    # ============================ 
    
    # Não recebe nenhum parâmetro
    # Neste caso abaixo, a função estática tem relação com o funcionário (dia de trabalho), mas não exige nenhum argumento da classe
    
    @staticmethod
    def dia_util(dia):
        # segunda-feira = 0
        # domingo = 6
        
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True
        



# ============================
# Herança de uma outra classe
# ============================

class Admin(Funcionario):
    
    # No init, admin deverá receber como argumento os parâmetros de funcionario (nome e salario) e os outros parâmetros caso tenha
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)
        
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome


