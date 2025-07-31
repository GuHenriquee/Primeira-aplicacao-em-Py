import os

restaurantes = [{'nome': 'Praca', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
                ]

def exibir_nome():
    print('1. Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    limpar_tela('App finalizado')

def voltar_menu():
    input('Digite um tecla para voltar para o menu principal: ')
    main()

def limpar_tela(texto: str):
    os.system('cls')
    print(texto)

def opcao_invalida():
    print('Opção invalida')
    voltar_menu()

def cadastra_novo_restaurante():
    limpar_tela('Cadastro de novos restaurantes')

    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite a categoria do restaurante: ')

    dados_restaurante = {'nome':nome_restaurante, 'categoria': categoria, 'ativo': False }

    restaurantes.append(dados_restaurante)
    if nome_restaurante:
        print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso')
        voltar_menu()

def listar_restaurantes():
    limpar_tela('Lista de restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante ['categoria']
        ativo = restaurante ['ativo']
        print(f'{nome_restaurante} | {categoria} | {ativo}')

    voltar_menu()

def alternar_restaurante():
    limpar_tela('Alterando status do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante ['ativo']:
                mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' 
            else:
                f'O restaurante {nome_restaurante} foi desativado com sucesso'
                print(mensagem)

        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')    
    voltar_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastra_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_restaurante()
        elif opcao_escolhida ==4:
            finalizar_app()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == '__main__':
    main()