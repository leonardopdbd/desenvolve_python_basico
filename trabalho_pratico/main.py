import csv

# Função para carregar usuários de um arquivo CSV
def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', mode='r') as file:
        leitor = csv.DictReader(file)
        for row in leitor:
            usuarios[row['id']] = {
                'nome': row['nome'],
                'senha': row['senha'],
                'permissao': row['permissao']
            }
    return usuarios

# Função para salvar usuários em um arquivo CSV
def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        campos = ['id', 'nome', 'senha', 'permissao']
        escritor = csv.DictWriter(file, fieldnames=campos)
        escritor.writeheader()
        for id, info in usuarios.items():
            escritor.writerow({'id': id, **info})

# Função para carregar produtos de um arquivo CSV
def carregar_produtos():
    produtos = []
    with open('produtos.csv', mode='r') as file:
        leitor = csv.DictReader(file)
        for row in leitor:
            produtos.append({
                'codigo': row['codigo'],
                'nome': row['nome'],
                'preco': float(row['preco']),
                'quantidade': int(row['quantidade'])
            })
    return produtos

# Função para salvar produtos em um arquivo CSV
def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='') as file:
        campos = ['codigo', 'nome', 'preco', 'quantidade']
        escritor = csv.DictWriter(file, fieldnames=campos)
        escritor.writeheader()
        for produto in produtos:
            escritor.writerow(produto)

# Função para adicionar um novo usuário
def adicionar_usuario(usuarios):
    id = input("Digite o ID do usuário: ")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha do usuário: ")
    permissao = input("Digite a permissão do usuário (gerente/funcionario): ")
    usuarios[id] = {'nome': nome, 'senha': senha, 'permissao': permissao}
    salvar_usuarios(usuarios)

# Função para listar todos os usuários
def listar_usuarios(usuarios):
    for id, info in usuarios.items():
        print(f"ID: {id}, Nome: {info['nome']}, Permissão: {info['permissao']}")

# Função para atualizar um usuário
def atualizar_usuario(usuarios):
    id = input("Digite o ID do usuário a ser atualizado: ")
    if id in usuarios:
        nome = input("Digite o novo nome do usuário: ")
        senha = input("Digite a nova senha do usuário: ")
        permissao = input("Digite a nova permissão do usuário (gerente/funcionario): ")
        usuarios[id] = {'nome': nome, 'senha': senha, 'permissao': permissao}
        salvar_usuarios(usuarios)
    else:
        print("Usuário não encontrado.")

# Função para remover um usuário
def remover_usuario(usuarios):
    id = input("Digite o ID do usuário a ser removido: ")
    if id in usuarios:
        del usuarios[id]
        salvar_usuarios(usuarios)
    else:
        print("Usuário não encontrado.")

# Função para adicionar um novo produto
def adicionar_produto(produtos):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos(produtos)

# Função para listar todos os produtos
def listar_produtos(produtos):
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

# Função para atualizar um produto
def atualizar_produto(produtos):
    codigo = input("Digite o código do produto a ser atualizado: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = input("Digite o novo nome do produto: ")
            produto['preco'] = float(input("Digite o novo preço do produto: "))
            produto['quantidade'] = int(input("Digite a nova quantidade do produto: "))
            salvar_produtos(produtos)
            return
    print("Produto não encontrado.")

# Função para remover um produto
def remover_produto(produtos):
    codigo = input("Digite o código do produto a ser removido: ")
    for i, produto in enumerate(produtos):
        if produto['codigo'] == codigo:
            del produtos[i]
            salvar_produtos(produtos)
            return
    print("Produto não encontrado.")

# Função principal do programa
def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    while True:
        print("\n--- Menu ---")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n--- Gerenciar Usuários ---")
            print("1. Adicionar Usuário")
            print("2. Listar Usuários")
            print("3. Atualizar Usuário")
            print("4. Remover Usuário")
            escolha_usuario = input("Escolha uma opção: ")
            if escolha_usuario == '1':
                adicionar_usuario(usuarios)
            elif escolha_usuario == '2':
                listar_usuarios(usuarios)
            elif escolha_usuario == '3':
                atualizar_usuario(usuarios)
            elif escolha_usuario == '4':
                remover_usuario(usuarios)
            else:
                print("Opção inválida.")
        elif escolha == '2':
            print("\n--- Gerenciar Produtos ---")
            print("1. Adicionar Produto")
            print("2. Listar Produtos")
            print("3. Atualizar Produto")
            print("4. Remover Produto")
            escolha_produto = input("Escolha uma opção: ")
            if escolha_produto == '1':
                adicionar_produto(produtos)
            elif escolha_produto == '2':
                listar_produtos(produtos)
            elif escolha_produto == '3':
                atualizar_produto(produtos)
            elif escolha_produto == '4':
                remover_produto(produtos)
            else:
                print("Opção inválida.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
