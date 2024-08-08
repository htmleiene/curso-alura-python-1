import os

restaurantes = [{'nome':'Mania', 'categoria':'Café', 'ativo':False}, 
                {'nome':'Planet', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Lanchonete', 'ativo':False}]

def exibir_nome_do_programa():
    '''Esta função exibe o nome do nosso programa'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Esta função exibe todas as opções que nossa aplicação possui para o usuário escolher'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Esta função finaliza o app'''
    exibir_subtitulo('Finalizar App')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Esta função é exibida caso algum input da função escolher_opcao seja inválido
    e retorna ao menu com a função voltar_ao_menu
    '''
    print('Opção inválida! \n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''Para cada função irá exibir seu subtitulo com decoração 
    Inputs:
    - texto: string - O texto que será exibido como subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu()

def listar_restaurantes():
    '''Esta função lista todos os restaurantes cadastrados na função cadastrar_restaraunte

    Outputs:
    - Nome do restaurante (nome_restaurante)
    - Categoria (categoria)
    - Ativo (ativo): o Status dos restaurantes
    '''

    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- { nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def mudar_status():
    '''Altera o status para ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da alteração

    '''

    exibir_subtitulo('Mude o status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativo com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário

    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            mudar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()