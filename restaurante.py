from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper() 
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome do restaurante'.ljust(25)} | {'categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | 
              | {str(restaurante.media_avaliacoes).ljust} |  {restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurantes = [restaurante_praca, restaurante_pizza]

Restaurantes.listar_restaurantes()


def receber_avaliacao(self, cliente, nota):
    if    0 < nota <= 5 :
        avaliacao = avaliacao(cliente, note)
        self._avaliacao.append(avaliacao)
@property
def media_avaliacoes(self):
        if not self._avaliacao:
            return '.'  
        soma_das_notas = sum(avaliacao._nota for avaliacao in self_avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas)
        return media         