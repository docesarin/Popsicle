estoque = {}

def adicionar_produto():
    codigo = input("Digite o código do produto: ")
    
    if codigo in estoque:
        print("Já existe um produto com esse código.")
        return
    
    nome = input("Digite o nome do produto: " )
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    estoque[codigo] = {"nome": nome, "preco": preco, "quantidade": quantidade}
    print(f"O produto {nome} foi adicionado ao estoque.")
    
def mostrar_produtos():
    if not estoque:
        print("Nenhum produto adicionado ao estoque.")
    else:
        print("\nProdutos no estoque:")
        for codigo, produto in estoque.items():
            print(f"Código: {codigo} | Nome: {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
        print()
        
def remover_produto():
    codigo = input("Digite o código do produto a ser removido: ")
    if codigo in estoque:
        produto_removido = estoque.pop(codigo)
        print(f"Produto '{produto_removido['nome']}' removido com sucesso!")
    else:
        print("Código não encontrado! Nenhum produto removido.")
        
def menu():
    while True:
        print("\nSistema de Gerenciamento de Estoque")
        print("1. Adicionar Produto")
        print("2. Mostrar Produtos")
        print("3. Remover Produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            mostrar_produtos()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o programa
menu()