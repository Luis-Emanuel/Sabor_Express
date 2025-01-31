import os


def exibir_nome_do_programa():
    print('''
    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 
    ''')

def finalizar_app():
    os.system('cls')
    print('Encerrar o programa\n')

def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def escolher_opcao():
    opcao_escolha = int(input('Escolha uma opção:'))
    if opcao_escolha == 1:
        print('1. Cadastrar restaurante')
    elif opcao_escolha == 2:
        print('2. Listar restaurante')
    elif opcao_escolha == 3:
        print('3. Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


