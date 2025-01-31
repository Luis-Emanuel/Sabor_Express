import os

restaurantes = ['Face Lanches', 'Kalzone']

def exibir_nome_do_programa():
    print('''
    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 
    ''')

def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrar o programa')

def volta_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu princial')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    volta_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def cadastra_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastra:')
    restaurantes.append(nome_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    volta_ao_menu_principal()

def listar_restaurantes():
    print('Listando os restaurantes')
    for restaurante in restaurantes:
        print(f'-> {restaurante}')
    volta_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolha = int(input('Escolha uma opção:'))
        while opcao_escolha < 0:
            print('OPÇÃO INVALIDA!')
            opcao_escolha = int(input('Informe um valor positivo:'))
        match opcao_escolha:
            case 1:
                cadastra_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('3. Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

 
