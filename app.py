import os

restaurantes = ['Face Lanches', 'Kalzone']

def exibir_nome_do_programa():
    print('''
    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 
    ''')
def limpar_terminal():
    os.system('cls')

def finalizar_app():
    limpar_terminal()
    print('Encerrar o programa\n')

def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção invalida!')
    input('Digite uma tecla para voltar ao menu princial')
    main()

def cadastra_novo_restaurante():
    limpar_terminal()
    print('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastra:')
    restaurantes.append(nome_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu princial')
    main()

def escolher_opcao():
    try:
        opcao_escolha = int(input('Escolha uma opção:'))
        if opcao_escolha == 1:
            cadastra_novo_restaurante()
        elif opcao_escolha == 2:
            print('2. Listar restaurante')
        elif opcao_escolha == 3:
            print('3. Ativar restaurante')
        elif opcao_escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_terminal()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

 
