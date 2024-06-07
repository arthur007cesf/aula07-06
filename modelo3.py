# 1. Inserir um decorator @property

class Restaurante:
    restaurante=[]
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False  
        Restaurante.restaurntes.append(self)
    
        
    @property
   
    def ativo(self):
        return "⊠" if self._ativo else "☐"
    @classmethod
    def __str__(self):
        return f"{self.nome.ljust(20)}|{self.categoria.ljust(20)}|{self.ativo.ljust(20)}"

# 2. Criando uma instancia da classe Restaurante com construtor

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Fast Food')  

# 3. Consumindo os objetos criado

restaurantes = [restaurante_praca]

for restaurante in restaurantes:
    #print(restaurante.nome, restaurante.categoria)
    #print(vars(restaurante))
    #print("")
    #print(vars(restaurante))
    #print('')
    print(restaurante)
