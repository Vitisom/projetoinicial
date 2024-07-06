import os

restaurantes = [{'nome':'Pizza Lakezin', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Lamborgine do C.J', 'categoria':'Brasileira', 'ativo':True}]

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    texto = f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Estado'}'
    print(texto)
    print('-' * (len(texto) + 4))
    for i in restaurantes:
        nome = i['nome']
        categ = i['categoria']
        ativo = 'Online' if i['ativo'] else 'Offline'
        print(f'- {nome.ljust(20)} | {categ.ljust(20)} | {ativo}')
    
    resetar_menu()

def exibir_subtitulo(text):
    os.system('cls')
    print('*' * (len(text)))
    print(text)
    print('*' * (len(text)))
    print('\n')

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite um nome para o novo restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante: {nome_restaurante} foi cadastrado com sucesso!')
    resetar_menu()

def ativar_restaurante():
    exibir_subtitulo('Qual restaurante deseja que fique online?')
    for i in restaurantes:
        print(i['nome'])
    restaurante = input('\nDigite o nome do restaurante: ')
    encontraado = False
    for ii in restaurantes:
        if restaurante == ii['nome']:
            encontraado = True
            ii['ativo'] = not ii['ativo']
            mensagem = f'o restaurante foi ativado' if ii['ativo'] else f'o restaurante foi desativado'
            print(mensagem)
    if not encontraado:
        print('o restaurante não foi encontrado')
    resetar_menu()

def resetar_menu():
    input('\nDigite uma tecla para voltar ao menu')
    main()

def exibir_titulo():
    print('''
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─██████████████─██████████████─██████████████───██████████████─████████████████──────██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
    ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██░░██████████─██░░██████░░██─██░░██████░░██───██░░██████░░██─██░░████████░░██──────██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
    ─██░░██─────────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─██░░██────██░░██──────██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
    ─██░░██████████─██░░██████░░██─██░░██████░░████─██░░██──██░░██─██░░████████░░██──────██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
    ─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██──────██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██████████░░██─██░░██████░░██─██░░████████░░██─██░░██──██░░██─██░░██████░░████──────██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
    ─────────██░░██─██░░██──██░░██─██░░██────██░░██─██░░██──██░░██─██░░██──██░░██────────██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
    ─██████████░░██─██░░██──██░░██─██░░████████░░██─██░░██████░░██─██░░██──██░░██████────██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
    ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
    ─██████████████─██████──██████─████████████████─██████████████─██████──██████████────██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def opcao_invalida():
    print('opção inválida')
    resetar_menu()

def finalizar_app():
    os.system('cls')
    print('finalizado')

def escolher_opc():
    try:
        opcao = int(input('\nEscolha uma das opções: '))

        match(opcao):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except(ValueError):
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    print('1. Cadastrar', '2. Listar', '3. Ativar', '4. Sair', sep='\n')
    escolher_opc()

if __name__ == '__main__':
    main()