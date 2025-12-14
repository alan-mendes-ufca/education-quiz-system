# Education-quiz-system

---

# Descrição do projeto

- Sistema de API mínima que permite _criar, gerenciar e responder_ quizzes com perguntas de múltipla escolha, incluindo amostragem estatística e uso do paradigma de programação orientada a objetos.

---

# Objetivo

- Desenvolver essa sistema utilizando uma API feita com o framkework livre `flask`, cumprindo todos os objetivos descritos no documento de requisitos (https://docs.google.com/document/d/19PaqgTEIkA0t21m5EJ4H3zBNMEdZD4KC/edit) de forma _excelente_. Portanto, adquirindo conhecimentos e plenitude com o uso básico de classes e seus princípios fundamentais.

---

# FastApi x Flask

- O fastapi (Estrutura de camadas) recomenda o uso de dois tipos de classes principais: Schemas (`Pydantic`) e Models (Banco de dados).

  - Schemas(/routers): "forma dos dados", _validam_ requests e responses.

    - Cardápio: pedir e receber.

  - Models(/models): classes para as tabelas no banco(`SQLAlquemy`).

    - Despensa: local de armazenamento.

  - Quanto a perspectiva das regras de negócio, são recomendados, na verdade, funções. O que entra em conflito com os requisitos do projeto. Segue as recomendações:
  - Services (/services): executa as regras de negócio.

    - cozinheiro: fluxo de ações.

- Quanto ao `flask`, é possível a criação de uma estrutura de projeto mais simples, suprindo todos os requisitos dados pelo professor (https://docs.google.com/document/d/19PaqgTEIkA0t21m5EJ4H3zBNMEdZD4KC/edit). `Por fim, pela *simplicidade* o framework escolhido para o desenvolvimetno desse projeto foi o flask.`

- Esqueleto, leigo, das classes: https://docs.google.com/spreadsheets/d/1IfV9YpOZb5DOFYyjDnL4ypVJ2WzAEqxyRfvTDKmn29Y/edit?usp=sharing.

---

## UML - Refatorado (_Princípio de responsabilidade única, arquitetura em camadas -> Arquitetura de Software_)

- **Relacionamento geral**:
  `Requisição HTTP → Rota do Flask (@app.route) → Serviço (QuizGame, AuthService, ...) → Repositório e Modelos de dados → Banco de Dados`

### Bloco 1 Modelo de dados (Encapsulamento) : _classes que apenas guardam dados_

Classe: `User` (Guarda dados)

- Atributos: \_\_user_id (privado), name, email, \_\_password_hash (privado).
- Métodos: getters e setters.
- Relacionamento/descrição: Empacota os dados do usuário, que vai ser utilizado na camada de repositório e serviço(autenticação).

Classe: `Question` (Abstrato, será importado pelas classes filhas)

- Atributos: \_\_question_id (privado), proposition, theme, difficulty_points.
- Métodos: check_answer(user_answer).
- Relacionamento/descrição: Define mínimo de atributos que as questões devem ter. Sendo a classe filha MultipleChoiceQuestion responsável por adicionar mais características.

Classe: `MultipleChoiceQuestion(Question)`

- Atributos: options: list, \_\_correct_option_index: int.
- Métodos: check_answer(user_answer_index) (implementa o método da classe-mãe).
- Relacionamento/descrição: Especializa Question com atributos específicos para múltipla escolha (opções, índice correto).

Classe: `Quiz` (Modelo)

- Atributos: \_\_quiz_id (privado), title, \_\_questions: list[Question] (privado).
- Métodos: get_questions(), get_max_score().
- Relacionamento/descrição: Serve de modelo para o quiz, empacotando características básicas do quiz. Será a classe 'configuração' que o serviço QuizGame usará para iniciar um jogo.

Classe: `QuizResult`

- Atributos: user: User, quiz: Quiz, score_achieved: int, time_taken: float, responses_history: dict.
- Relacionamento/descrição: criado por QuizGame ao final de uma "partida", salvando o resultado. Por fim, será salvo no bando de dados por meio de QuizResultRepository.

---

### Bloco 2: Repositório (Acesso a dados): _Classes focadas apenas no CRUD_

Classe: `UserRepositoty`

- Atributos: (conexão com o banco de dados).
- Médodos: create(user: User), get_by_id(user_id) -> User, get_by_email(email) -> User, update(user: User).
- Relacionamento/descrição: "Empacota" os dados de uma consulta de usuários em um objeto User. Em outros contexto também criará uma linha na tabela de usuários por meio de um objeto User fornecido pelo AuthService.

Classe: `QuestionRepository`

- Atributos: (conexão com o banco de dados).
- Métodos: create(question: Question), get_by_theme(theme) -> list[Question], get_random_questions(theme, count) -> list[Question].
- Relacionamento/descrição: Além do CRUD básico (persistência), ele fornece métodos de consulta especializados (ex: get_random_questions) que serão consumidos pelos serviços."

Classe: `QuizResultRepository`

- Atributos: (conexão com o banco de dados).
- Métodos: save(result: QuizResult), get_results_by_user(user: User) -> list[QuizResult].
- Relacionamento/descrição: Cadastra os resultados dos usuário no banco de dados. Será consumido posteriormente ao gerar as estatísticas (StatisticsService).

---

### Bloco 3: Serviços: _classes que orquestrão a lógica da aplicação_

Classe: `AuthService`

- Atributos: user_repository: UserRepository.
- Métodos: login(email, password) -> User, register(name, email, password) -> User, logout().
- Relacionamento/descrição: Controla as regras de negócio no que se diz respeito a autenticação(login, registro de usuário e logout).

Classe: `QuizGame`

- Atributos: quiz: Quiz, user: User, current_question_index: int, user_answers: list, start_time.
- Métodos: start_game(), get_current_question() -> Question, submit_answer(answer), finish_game() -> QuizResult (cria e retorna um objeto QuizResult).
- Relacionamento/descrição: Controla o estado e o fluxo de uma única sessão de jogo. É responsável por avançar as perguntas, registrar as respostas do usuário e, ao final (finish_game), criar e retornar o objeto QuizResult

Classe: `StatisticsService`

- Atributos: result_repository: QuizResultRepository.
- Métodos: get_accuracy_rate(user: User) -> float, get_player_ranking() -> list, get_most_missed_questions() -> list[Question].
- Relacionamento/descrição: Serviço responsável por calcular informações, estatísticas das "partidas".

---

# Organização de pastas e arquivos

```
. (root)
├── README.md
├── app.py
├── requirements.txt
│
├── templates/ # refere-se as interfaces do sistema.
│   └── index.html
|   └── ...
|
├── data/ # Configuração do banco sqlite
│   └── app.db
│
├── models/ # classes que guardam informações de entidades específicas.
│   ├── __init__.py # trata diretório como um módulo.
│   ├── MultipleChoice.py
│   ├── Question.py
│   ├── Quiz.py
│   ├── QuizResult.py
│   └── User.py
|
├── repositories/ # classes resposáveis pela persistência de dados.
│   ├── __init__.py
│   ├── QuestionRepository.py
│   ├── QuizResultRepository.py
│   └── UserRepository.py
│
├── services/ # classes responsáveis pelas regras de negócio.
│   ├── __init__.py
|   ├── AuthService.py
│   ├── QuizGame.py
│   └── StatisticsService.py
│
└── tests/ # validam o funcionamento da aplicação.
    ├── __init__.py
    └── ...

```

## Como rodar

- `flask run --debug`

---

## Ambiente Virtual (venv)

### Por que usar?

O `venv` (Virtual Environment) cria uma caixa isolada para o seu projeto.

- As bibliotecas do projeto ficam na pasta do projeto (`.venv`), não espalhadas pelo seu sistema operacional.

### Como usar

1. **Criar o ambiente virtual**:

   ```bash
   python3 -m venv .venv
   ```

2. **Ativar o ambiente**:

   ```bash
   source .venv/bin/activate
   ```

   _(Você verá `(.venv)` aparecer no início da linha do terminal)_

3. **Instalar as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Sair do ambiente (quando terminar)**:
   ```bash
   deactivate
   ```

---

## SQLite3

- o banco de dados utilizado é o SQLite3, devido ao fato de que ele ser um banco de dados leve e que não requer uso do Docker.

### 1. Iniciar o Banco de Dados

```bash
sqlite3 app.db
```

### 2. Criando as tabelas

- o schema das tabelas criadas pode ser visualizado por meio do comando `.schema` e por meio do arquivo `schema.sql`.

### 3. CRUD de dados

- Para inserir dados, por meio das classes de repositório, preciso de uma ferramenta de `Query`: a biblioteca cs50 tem uma classe SQL que permite fazer isso com o método `execute`.

- Por que utilizar esse módulo de consulta do cs50 ao invés de outros? porque eu já tenho familiaridade com seu uso.

```python
from cs50 import SQL

# Inicializa a conexão com o banco de dados
db = SQL("sqlite:///data/app.db")

# Insere um novo usuário
db.execute("INSERT INTO user (name, email, password_hash) VALUES (?, ?, ?)", "nome", "email", "senha")
```

# Pytest-watch

- `ptw --runner "pytest -s -q -p no:warnings"`

# Debugando

- Ao decorrer do projeto me deparei com muitos bugs, alguns bestas e outros mais complexos...daqueles que cansam a mente.
- Descobri que é possível debugar o código flask com breakpoints.

  - Adicione `.vscode/launch.json`

    ```json
    {
      "version": "0.2.0",
      "configurations": [
        {
          "name": "Flask Debug",
          "type": "debugpy",
          "request": "launch",
          "module": "flask",
          "env": {
            "FLASK_APP": "flaskr/app.py",
            "FLASK_ENV": "development",
            "FLASK_DEBUG": "1"
          },
          "args": ["run"],
          "jinja": true
        }
      ]
    }
    ```

# Bug enfrentado com session

- session é um dicionário que referência os cookies do navegador e guarda informações da sessão, ao utiliza-lo tive um problema: eu atualizava um de seus parâmetros, mas posteriormente ele retornava para a versão anterior.
- por que isso acontecia? A sessão não estava sendo marcada como modificada!

```python

  # O flask não marca a sessão como modificada quando você altera valores dentro de um dicionário aninhado.
  session["quiz_session"]["current_question"] += 1
  # Solução:
  session.modified =  True

  # Solução 2: Reatribuir o dicionário completo
  session_data = session["quiz_session"]
  session_data["current_question"] += 1
  session["quiz_session"] = session_data  # Reatribui, chamando __setitem__
```

- session herda as características de um dicionário normal `class session(dict)`, mas adiciona um recurso que `detecta  quando ele foi modificado`. Por fim, quando o dicionário não é alterado diretamente, somente um atributo de um dict filho, esse método `__setitem__` nunca é chamado.

## Explicação técnica

- Python usa **referências (ponteiro)** para objetos mutáveis (dict, list)
- `session["quiz_session"]` retorna a referência ao objeto original, **não uma cópia**
- Modificar o objeto referenciado não aciona o `__setitem__` do dict pai.

- Resumo:
  > Ao acessar a `session`, recebo um ponteiro direto para o objeto na memória RAM. Como modifico apenas o dicionário filho, o Flask não detecta a alteração (`is_modified`permanece falso) e, por isso, não atualiza o cookie do navegador, descartando a mudança ao fim da requisição.
