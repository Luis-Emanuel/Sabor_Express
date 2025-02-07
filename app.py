import os

restaurantes = [{'nome': 'Kalzone', 'categoria': 'Saudável', 'ativo': False},
                {'nome': 'Dominus', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Kibixinha', 'categoria': 'Salgados', 'ativo': False}]

#Para o sistema
def exibir_nome_do_programa():
    print('''
    ▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
    ░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
    ▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 
    ''')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(f'{texto}\n')
    print(linha)

def volta_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu princial')
    main()

def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrar o programa')
#==================
def opcao_invalida():
    print('Opção invalida!\n')
    volta_ao_menu_principal()

def cadastra_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    #nome
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastra:')
    #categoria
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')     
    
    dados_do_restaurante = {
        'nome': nome_do_restaurante, 
        'categoria': cadastra_novo_restaurante, 
        'ativo': False
    } 
    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    volta_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} |ATIVO')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria_do_restaurante = restaurante['categoria']
        ativo_restaurante = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
        print(f'- {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {ativo_restaurante}')
    volta_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')            
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
                alterar_estado_restaurante()
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

 
