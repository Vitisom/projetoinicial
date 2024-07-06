class Pessoa:
    def __init__(self, nome='', idade=0, proffisao=''):
        self._nome = nome
        self.idade = int(idade)
        self.profissao = proffisao
    def __str__(self):
        return f'olá {self._nome} vc já tem {self.idade} e é {self.profissao}' if self.profissao else f'olá {self._nome} vc já tem {self.idade} e é Desempregado'
    def aniversario(self):
        self.idade += 1
    @property
    def saudacao(self):
        if self.profissao:
            return f'Feliz Aniversário {self._nome}! e tem {self.idade} anos, e é {self.profissao}'
        else:
            return f'Feliz Aniversário {self._nome}! e tem {self.idade} anos, e é Desempregado'

pessoa1 = Pessoa('João Silva da Rosa', 23, 'Pedreiro')
print(str(pessoa1))
input('\nFalta um dia para seu aniversário!\n')
pessoa1.aniversario()
print(pessoa1.saudacao)