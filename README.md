
# API de Gerenciamento de Produtos e Clientes
## Instalar as dependências:

```shell
make install
```

## Subir o docker-compose:

```shell
make docker
```

## Subir o servidor:

```shell
make run
```

## Rodar os testes:

```shell
make test
```

## Este é o gerenciamento de  produtos em uma loja. Ela permite a criação, leitura, atualização e exclusão de produtos.

## Endpoints
### Criação de Produto
- URL: /products/
- Método: POST
- Código de Status: 201 - Created
- Descrição: Cria um novo produto com os dados fornecidos.
- Parâmetros do Corpo da Requisição:

```shell
name (string): Nome do produto (obrigatório)
quantity (int): Quantidade do produto em estoque (obrigatório, maior que zero)
price (float): Preço do produto (obrigatório, maior que zero)
```

### Obtenção de Produto
- URL: /products/{id}
- Método: GET
- Código de Status: 200 - OK
- Descrição: Retorna os detalhes de um produto específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do produto
```

### Listagem de Produtos
- URL: /products/
- Método: GET
- Código de Status: 200 - OK
- Descrição: Retorna uma lista de todos os produtos disponíveis.

### Atualização de Produto
- URL: /products/{id}
- Método: PATCH
- Código de Status: 200 - OK
- Descrição: Atualiza os detalhes de um produto específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do produto
```

- Parâmetros do Corpo da Requisição:

```shell
name (string): Novo nome do produto
quantity (int): Nova quantidade do produto em estoque
price (float): Novo preço do produto
```

### Exclusão de Produto
- URL: /products/{id}
- Método: DELETE
- Código de Status: 204 - No Content
- Descrição: Remove um produto específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do produto
```
---

## Endpoints
### Criação de CLientes
- URL: /clients/
- Método: POST
- Código de Status: 201 - Created
- Descrição: Cria um novo cliente com os dados fornecidos.
- Parâmetros do Corpo da Requisição:

```shell
name (string): Nome do cliente (obrigatório)
quantity (int): Quantidade de produtos em estoque (obrigatório, maior que zero)
product_id (UUID): Id do produto associado (obrigatório, maior que zero)
```

### Obtenção de Clientes
- URL: /clients/{id}
- Método: GET
- Código de Status: 200 - OK
- Descrição: Retorna os detalhes de um cliente específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do cliente
```

### Listagem de Clientes
- URL: /clients/
- Método: GET
- Código de Status: 200 - OK
- Descrição: Retorna uma lista de todos os clientes disponíveis.

### Atualização de Cliente
- URL: /clients/{id}
- Método: PATCH
- Código de Status: 200 - OK
- Descrição: Atualiza os detalhes de um cliente específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do cliente
```

- Parâmetros do Corpo da Requisição:

```shell
quantity (int): Nova quantidade do produto em estoque
```

### Exclusão de Cliente
- URL: /pclients/{id}
- Método: DELETE
- Código de Status: 204 - No Content
- Descrição: Remove um cliente específico com base no ID fornecido.
- Parâmetros da URL:

```shell
id (UUID): ID único do cliente
```

### Tratamento de Erros
- 400 - Bad Request: Solicitação inválida devido a dados ausentes ou inválidos.
- 404 - Not Found: O produto solicitado não foi encontrado.
- 422 - Unprocessable Entity: Erro de validação nos dados fornecidos.
- 500 - Internal Server Error: Erro interno do servidor ao processar a solicitação.
- Esta API permite interagir com os produtos da loja de forma fácil e segura. Certifique-se de fornecer os dados corretos ao fazer solicitações e verifique as mensagens de erro para entender qualquer problema que possa surgir durante a interação com a API.