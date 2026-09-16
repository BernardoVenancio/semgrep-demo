# Book Tracker — demonstração com Semgrep

Aplicação simples desenvolvida com Flask e SQLite para uma demonstração acadêmica de análise estática de código com o Semgrep.

O sistema permite cadastrar livros, atribuir notas e resenhas, visualizar os registros salvos e pesquisar por título ou autor.

## Como executar

Clone o repositório e acesse a pasta do projeto.

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicialize o banco de dados:

```bash
python db.py
```

Esse comando cria o arquivo `instance/books.db` e adiciona alguns livros de exemplo.

Em seguida, execute a aplicação:

```bash
python app.py
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:5000
```

## Executando o Semgrep

Para analisar o projeto usando as regras disponíveis no registro do Semgrep:

```bash
semgrep scan --config auto .
```

O projeto também possui regras customizadas na pasta `semgrep/`. Para executá-las:

```bash
semgrep scan --config semgrep/rules.yml .
```

## Vulnerabilidades intencionais

### SQL Injection

A rota `/search` monta uma consulta SQL concatenando diretamente o texto informado pelo usuário. Isso permite alterar a estrutura da consulta por meio do campo de pesquisa.

Após a demonstração, a consulta pode ser corrigida utilizando parâmetros:

```python
books = db.execute(
    """
    SELECT id, title, author, rating, review
    FROM books
    WHERE title LIKE ? OR author LIKE ?
    """,
    (f"%{term}%", f"%{term}%"),
).fetchall()
```

### Secret hardcoded

O arquivo `app.py` contém uma `SECRET_KEY` escrita diretamente no código. Em uma aplicação real, esse valor não deve ser versionado e deve ser carregado de uma variável de ambiente ou de outro mecanismo seguro de configuração.

### Regras customizadas

A pasta `semgrep/` contém regras criadas para a demonstração. Elas complementam as regras prontas do Semgrep e permitem mostrar como padrões específicos podem ser identificados no código do projeto.
