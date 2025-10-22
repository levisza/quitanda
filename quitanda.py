estoque = {}
#CADASTRO DE ITENS
def cadastro_itens():
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        print("Produto ja cadastrado")
        return
    quantidade = int(input("Digite a Quantidade: "))
    estoque[produto] = quantidade

#CONSULTA DE ITENS
def consultar_estoque():
    for key, value in estoque.items():
        print(f'Item = {key}, Quantidade = {value}' )
    if not estoque:
        print("Estoque Vazio")

#VALIDAÇÃO DE USUARIO/MENU
while True:
    print ("---QUITANDA ANHANGUERA---")
    usuario = input("Insira seu Usuario: ")
    senha = int(input("Insira sua Senha: "))
    if usuario == "joao" and senha == 1234:
            print("Acesso Liberado")
            while True:
                    digito_usuario = input("=== MENU ===\n1 - Cadastro de Itens\n2 - Estoque\n3 - Sair\nDigite uma Opcao: ")
                    if digito_usuario == "1":
                           cadastro_itens()
                    elif digito_usuario == "2":
                           consultar_estoque()
                    elif digito_usuario == "3":
                            break        
    else:
        print ("Acesso Negado")
