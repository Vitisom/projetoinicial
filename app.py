from modelos.classe1 import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gustavo', 10)
restaurante_praca.receber_avaliacao('Gabriel', 7)
restaurante_praca.receber_avaliacao('Murilo', 4)
restaurante_praca.receber_avaliacao('Lorenzo', 7)
restaurante_praca.receber_avaliacao('Miguel', 4)
restaurante_praca = Restaurante('Pizza Canoas', 'entregas')
restaurante_praca.receber_avaliacao('Gustavo', 10)
restaurante_praca.receber_avaliacao('Gabriel', 9)
restaurante_praca.receber_avaliacao('Murilo', 8)
restaurante_praca.receber_avaliacao('Lorenzo', 8)
restaurante_praca.receber_avaliacao('Miguel', 9)
restaurante_praca = Restaurante('Hamburgeria do Sérgio', 'Brazil')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()