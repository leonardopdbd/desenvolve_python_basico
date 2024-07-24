Introdução
O sistema foi modelado para uma empresa fictícia de gerenciamento de estoque e usuários, permitindo um controle eficiente e seguro dos dados de usuários e produtos. A empresa atende principalmente gerentes e funcionários, cada um com permissões específicas para acessar e modificar dados. A empresa oferece produtos diversos, como itens de tecnologia, vestuário, alimentos, entre outros.

Implementação
Usuário

Estrutura de Dados:

Os usuários são armazenados em um dicionário Python onde a chave é o ID do usuário e o valor é outro dicionário contendo o nome, senha e permissão do usuário.
Arquivo de Registro:

O arquivo de registro de usuários (usuarios.csv) é um arquivo CSV que possui as seguintes colunas: id, nome, senha, permissao.
Funcionalidades:

Adicionar Usuário (Create): Adiciona um novo usuário ao sistema, solicitando ao administrador as informações necessárias.
Listar Usuários (Read): Exibe todos os usuários cadastrados no sistema.
Atualizar Usuário (Update): Permite a modificação dos dados de um usuário existente.
Remover Usuário (Delete): Remove um usuário do sistema com base em seu ID.
Produto

Estrutura de Dados:

Os produtos são armazenados em uma lista de dicionários, onde cada dicionário representa um produto com os atributos: código, nome, preço e quantidade.
Arquivo de Registro:

O arquivo de registro de produtos (produtos.csv) é um arquivo CSV que possui as seguintes colunas: codigo, nome, preco, quantidade.
Funcionalidades:

Adicionar Produto (Create): Adiciona um novo produto ao sistema, solicitando as informações necessárias ao administrador.
Listar Produtos (Read): Exibe todos os produtos cadastrados no sistema.
Atualizar Produto (Update): Permite a modificação dos dados de um produto existente.
Remover Produto (Delete): Remove um produto do sistema com base em seu código.
Conclusão
Durante o desenvolvimento do sistema, algumas dificuldades encontradas incluíram a manipulação de arquivos CSV e a garantia de que as entradas do usuário fossem válidas e consistentes. Uma escolha bem-sucedida foi a utilização de dicionários para armazenar dados de usuários, pois permitiu um acesso rápido e eficiente.

O que faltou fazer foi a implementação de um sistema de autenticação robusto e a validação mais rigorosa dos dados de entrada, além de testes automatizados para garantir a qualidade do código. Se fosse refeito, a aplicação poderia incluir uma interface gráfica para facilitar o uso e melhorar a experiência do usuário.
