from modelos.avaliacao import Avaliação

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._estado = False
        self.avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.estado}'
    
    @property
    def media_avaliacao(self):
        if not self.avaliacao:
            return 'Sem Avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self.avaliacao)
        quantidade_de_notas = len(self.avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def listar_restaurantes():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Estado')
        for i in Restaurante.restaurantes:
            print(f'{i._nome.ljust(25)} | {i._categoria.ljust(25)} | {str(i.media_avaliacao).ljust(25)} | {i.estado}')
    @property
    def estado(self):
        return 'X' if self._estado else 'O'
    
    def alternar_estado(self):
        self.estado = not self.estado
    
    def receber_avaliacao(self,cliente,nota):
        avaliacao = Avaliação(cliente,nota)
        self.avaliacao.append(avaliacao)