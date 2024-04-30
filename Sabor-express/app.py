import os
restaurantes = [{"nome":"Papizza", "categoria":"Italiano", "ativo":False}, 
                {"nome":"Coma a vontade", "categoria":"Self service", "ativo":True},
                {"nome":"Churrascada de cria", "categoria": "Self service", "ativo":True},
                {"nome": "Japaki", "catagoria": "Lanchonete", "ativo": False}]

def exibir_nome_do_programa():
    print("𝒮𝒶𝒷ℴ𝓇 ℰ𝓍𝓅𝓇ℯ𝓈𝓈\n")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4.Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando app")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante{nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria": categoria,"ativo": False }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso! ")
    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system('cls')
    exibir_subtitulo('Listando os restaurantes\n') 
    print(f"{"nome do restaurante".ljust(23)} | {"categoria".ljust(20)} | status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "ativado" if restaurante['ativo'] else "desativado"
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def alternar_estado_restaurante():
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
           restaurante_encontrado = True
           restaurante["ativo"] = not restaurante["ativo"]
           mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante ["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
           print(mensagem)      
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado") 
    voltar_ao_menu_principal();

        


def escolher_opcao():
    try:   
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                listar_restaurantes()
            elif opcao_escolhida == 3:
                alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                finalizar_app()
            else:
                print('Opção inválida!')
    except:
            print('Opção inválida!')

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

if __name__ == "__main__":
    main()











