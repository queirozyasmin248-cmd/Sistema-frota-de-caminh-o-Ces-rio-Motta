estoque = [
    {"codigo": 101, "nome": "Teclado", "quantidade": 8, "preco": 75.0},
    {"codigo": 102, "nome": "Mouse", "quantidade": 15, "preco": 40.0},
    {"codigo": 103, "nome": "Monitor", "quantidade": 4, "preco": 850.0}
]

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("O código deve ser um número inteiro!")
        return
        
    # CORREÇÃO: Percorre a lista para verificar se o código já existe nos dicionários
    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Esse código já existe!")
            return

    nome = input("Nome do produto: ").strip()
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Digite valores numéricos válidos!")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return
    for produto in estoque:
        # CORREÇÃO: Alterado de produto["valor"] para produto["preco"]
        print(
            "Código:", produto["codigo"], 
            "| Nome:", produto["nome"], 
            "| Quantidade:", produto["quantidade"], 
            "| Preço: R$", produto["preco"]
        )

def pesquisar_produto():
    print("\n--- PESQUISAR PRODUTO ---")
    try:
        codigo = int(input("Digite o código: "))
    except ValueError: # CORREÇÃO: Alterado de TypeError para ValueError
        print("O código precisa ser um número!")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Produto encontrado:", produto["nome"])
            print("Quantidade:", produto["quantidade"])
            print("Preço: R$", produto["preco"])
            encontrado = True
            break # Interrompe o loop ao encontrar
            
    # CORREÇÃO: Mensagem exibida apenas se passou por todo o estoque e não achou
    if not encontrado:
        print("Produto não encontrado!")

def registrar_entrada():
    print("\n--- ENTRADA DE MERCADORIA ---")
    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido!")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == codigo:
            encontrado = True
            try:
                quantidade = int(input("Quantidade recebida: "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que zero!")
                    return
            except ValueError:
                print("A quantidade deve ser um número inteiro!")
                return
            
            # CORREÇÃO: Alterado de subtração (-) para adição (+)
            produto["quantidade"] = produto["quantidade"] + quantidade
            print("Entrada registrada com sucesso!")
            break

    if encontrado == False:
        print("Produto não encontrado!")

def relatorio_estoque():
    print("\n--- RELATÓRIO DO ESTOQUE ---")
    total_unidades = 0
    valor_total = 0
    for produto in estoque:
        total_unidades = total_unidades + produto["quantidade"]
        # CORREÇÃO: Multiplica a quantidade pelo preço unitário
        valor_total = valor_total + (produto["quantidade"] * produto["preco"])
        
    print("Quantidade total de unidades:", total_unidades)
    print("Valor total do estoque: R$", valor_total)

def menu():
    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Registrar entrada")
        print("5 - Relatório de estoque")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            registrar_entrada()
        elif opcao == "5":
            relatorio_estoque()
        elif opcao == "6": # CORREÇÃO: Alterado de "7" para "6"
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

menu()
