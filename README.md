# Descrição do projeto

- Sistema de API mínima que permite _criar, gerenciar e responder_ quizzes com perguntas de múltipla escolha, incluindo amostragem estatística e uso do paradigma de programação orientada a objetos.

---

# Objetivo

- Desenvolver essa sistema utilizando uma API feita com o framkework livre `flask`, cumprindo todos os objetivos descritos no documento de requisitos (https://docs.google.com/document/d/19PaqgTEIkA0t21m5EJ4H3zBNMEdZD4KC/edit) de forma _excelente_. Portanto, adquirindo conhecimentos e plenitude com o uso básico de classes e seus princípios fundamentais.

---

# Tecnologias utilizadas

## FastApi x Flask

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

## SQLite3

- Para inserir dados, por meio das classes de repositório, preciso de uma ferramenta de `Query`: a biblioteca cs50 tem uma classe `SQL` que permite fazer isso com o método `execute`.

- Por que utilizar esse módulo de consulta do cs50 ao invés de outros? porque eu já tenho familiaridade com seu uso - fator importante quando ao prazo de entrega do projeto.

---

# UML (_Princípio de responsabilidade única, arquitetura em camadas -> Arquitetura de Software_)

- **Relacionamento geral**:
  `Requisição HTTP → Rota do Flask (@app.route) → Serviço (QuizGame, AuthService, ...) → Repositório e Modelos de dados → Banco de Dados`

## Bloco 1 Modelo de dados (Encapsulamento) : _classes que apenas guardam dados_

Classe: `User` (Guarda dados)

- Atributos: \_\_user_id (privado), name, email, \_\_password_hash (privado).
- Métodos: getters e setters, constructor_dict(dict) -> User, \_\_str\_\_().
- Relacionamento/descrição: Empacota os dados do usuário, que vai ser utilizado na camada de repositório e serviço(autenticação).

Classe: `Question` (Abstrato, será importado pelas classes filhas)

- Atributos: \_\_question_id (privado), proposition, category, \_difficulty_points (protegido).
- Métodos: getters e setters, check_answer(user_answer) [abstractmethod].
- Relacionamento/descrição: Define mínimo de atributos que as questões devem ter. Sendo a classe filha MultipleChoiceQuestion responsável por adicionar mais características.

Classe: `MultipleChoiceQuestion(Question)`

- Atributos: alternatives: list, \_correct_option_index: int (protegido).
- Métodos: check_answer(user_answer_index) -> dict, from_dict(data: dict) -> MultipleChoiceQuestion, to_dict_public() -> dict, to_dict() -> dict, \_\_str\_\_().
- Relacionamento/descrição: Especializa Question com atributos específicos para múltipla escolha (opções, índice correto).

Classe: `Quiz` (Modelo)

- Atributos: \_\_quiz_id (privado), title, category, description, \_questions: list[Question] (protegido).
- Métodos: get_max_score() -> int, from_dict(d: dict) -> Quiz, questions (property retorna tuple imutável).
- Relacionamento/descrição: Serve de modelo para o quiz, empacotando características básicas do quiz. Será a classe 'configuração' que o serviço QuizGame usará para iniciar um jogo.

Classe: `QuizResult`

- Atributos: user: User, quiz: Quiz, quiz_session: int, score_achieved: int, time_taken: float, max_possible_score: int.
- Métodos: \_\_str\_\_().
- Relacionamento/descrição: Criado por QuizGame ao final de uma "partida", salvando o resultado. Por fim, será salvo no banco de dados por meio de QuizResultRepository.

Classe: `QuizSession` _(nova)_

- Atributos: \_session_id (protegido), \_user_id (protegido), \_quiz_id (protegido), \_current_question_index (protegido), \_score (protegido).
- Métodos: getters e setters, from_dict(d: dict) -> QuizSession, \_\_str\_\_().
- Relacionamento/descrição: Modelo para persistência da sessão do quiz, permitindo retomar partidas.

Classe: `UserAnswer` _(nova)_

- Atributos: \_user_id (protegido), \_quiz_id (protegido), \_question_id (protegido), selected_option: int, is_correct: bool, time_to_response: float.
- Métodos: getters e setters, \_\_str\_\_().
- Relacionamento/descrição: Encapsula o histórico de respostas do usuário para análises estatísticas.

Classe: `InvalidCredentialsError(Exception)` _(nova)_

- Atributos: herdados de Exception.
- Métodos: herdados de Exception.
- Relacionamento/descrição: Exceção customizada para erros de autenticação (login/registro).

---

## Bloco 2: Repositório (Acesso a dados): _Classes focadas apenas no CRUD_

Classe: `UserRepository`

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: create(user: User) -> User, get_by_id(user_id) -> User, get_by_email(email) -> User, update(user: User) -> User.
- Relacionamento/descrição: "Empacota" os dados de uma consulta de usuários em um objeto User. Em outros contextos também criará uma linha na tabela de usuários por meio de um objeto User fornecido pelo AuthService.

Classe: `QuestionRepository`

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: create(question: MultipleChoiceQuestion) -> Question, get_by_proposition(proposition) -> Question, get_by_category(category) -> list[Question], get_random_questions(category, count) -> list[Question].
- Relacionamento/descrição: Além do CRUD básico (persistência), ele fornece métodos de consulta especializados (ex: get_random_questions) que serão consumidos pelos serviços.

Classe: `QuizRepository` _(nova)_

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: create(quiz: Quiz) -> int, get_by_id(id) -> Quiz, get_by_title(title) -> Quiz, get_by_category(category) -> list[Quiz], get_all() -> list[Quiz], get_most_popular() -> list[Quiz].
- Relacionamento/descrição: Responsável pela persistência (CRUD) dos quizzes.

Classe: `QuizResultRepository`

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: save(result: QuizResult), get_results_by_user(user: User) -> list[QuizResult], get_results_by_quiz(quiz_id) -> list, get_results_by_session(session_id) -> dict, get_ranking() -> list.
- Relacionamento/descrição: Cadastra os resultados dos usuários no banco de dados. Será consumido posteriormente ao gerar as estatísticas (StatisticsService).

Classe: `QuizSessionRepository` _(nova)_

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: create(session: QuizSession) -> int, get_by_id(user_id, quiz_id) -> QuizSession, update_session(session: QuizSession) -> int.
- Relacionamento/descrição: Responsável pela persistência (CRUD) das sessões de quiz.

Classe: `UserAnswerRepository` _(nova)_

- Atributos: db: SQL (conexão com o banco de dados).
- Métodos: save(us_answer: UserAnswer) -> int, get_most_missed_question_by_quiz(quiz_id) -> list, get_most_missed_question_all() -> list, get_most_correct_question_by_quiz(quiz_id) -> list, get_most_correct_question_all() -> list.
- Relacionamento/descrição: Responsável pela persistência das respostas do usuário e consultas estatísticas de acertos/erros.

---

## Bloco 3: Serviços: _classes que orquestram a lógica da aplicação_

Classe: `AuthService`

- Atributos: user_repository: UserRepository.
- Métodos: register(name, email, password) -> User, login(email, password) -> User, logout() [static].
- Relacionamento/descrição: Controla as regras de negócio no que se diz respeito a autenticação (login, registro de usuário e logout).

Classe: `QuizGame`

- Atributos: quiz: Quiz, user: User, current_question_index: int, score: int, session_id: int, register_user_response_repo: UserAnswerRepository, register_quiz_result: QuizResultRepository, time: list.
- Métodos: start_game() -> Question, get_current_question() -> MultipleChoiceQuestion, register_user_response(user_response: UserAnswer) -> Question, register_time(time_to_response: float), get_total_time() -> float, finish_game(d: dict).
- Relacionamento/descrição: Controla o estado e o fluxo de uma única sessão de jogo. É responsável por avançar as perguntas, registrar as respostas do usuário e, ao final (finish_game), salvar o QuizResult no banco de dados.

Classe: `StatisticsService`

- Atributos: quiz_repo: QuizResultRepository, user_answer: UserAnswerRepository.
- Métodos: get_accuracy_rate(user: User) -> float, get_player_ranking() -> list, get_player_ranking_by_quiz(quiz_result_id) -> list, get_most_missed_question_by_quiz(quiz_result_id) -> list, get_most_missed_question_all() -> list, get_most_correct_question_by_quiz(quiz_result_id) -> list, get_most_correct_question_all() -> list.
- Relacionamento/descrição: Serviço responsável por calcular informações e estatísticas das "partidas".

# Organização de pastas e arquivos

```
.
├── data
│   ├── app.db
│   ├── examples.sql
│   └── schema.sql
├── flaskr
│   ├── app.py
│   ├── helpers.py
│   ├── __init__.py
│   ├── quiz.db
│   ├── static
│   │   ├── js
│   │   │   └── createQuestions.js
│   │   └── style.css
│   └── templates
│       ├── create_quiz.html
│       ├── index.html
│       ├── layout.html
│       ├── login.html
│       ├── quiz_run.html
│       ├── quizzes_list.html
│       ├── register.html
│       └── result.html
├── .gitignore
├── models
│   ├── __init__.py
│   ├── InvalidCredentialError.py
│   ├── MultipleChoice.py
│   ├── Question.py
│   ├── Quiz.py
│   ├── QuizResult.py
│   ├── QuizSession.py
│   ├── UserAnswer.py
│   └── User.py
├── README.md
├── repositories
│   ├── __init__.py
│   ├── QuestionRepository.py
│   ├── QuizRepository.py
│   ├── QuizResultRepository.py
│   ├── QuizSessionRepository.py
│   ├── UserAnswerRepository.py
│   └── UserRepository.py
├── requirements.txt
├── services
│   ├── AuthService.py
│   ├── __init__.py
│   ├── QuizGame.py
│   └── StatisticsService.py
└── tests
    ├── db
    │   ├── test_auth_db.sqlite
    │   └── test_statistics_db.sqlite
    ├── __init__.py
    ├── test_auth_service.py
    ├── test_creat_quiz.py
    ├── test_login.py
    ├── test_quizzes.py
    └── test_statistics_service.py

11 directories, 48 files
```

# Como rodar

## Requisitos

- Python 3.10+
- SQLite (já incluído no Python)

## Passo a passo

- Primeiramente, crie um ambiente virtual:

  ```bash
  python3 -m venv .venv
  ```

- Ative o ambiente virtual:

  ```bash
  source .venv/bin/activate
  ```

- Instale as dependências:

  ```bash
  pip install -r requirements.txt
  ```

- Inicie o banco de dados SQLite3:

  ```bash
  sqlite3 data/app.db
  ```

- Crie as tabelas no banco de dados:
  ```bash
  .read data/schema.sql
  ```
- Finalmente, rode o servidor Flask:
  ```bash
  - Defina `MY_SECRET_KEY` em `.env`.
  - Na raiz do repositório, execute: `flask run --debug` ou `flask run
  ```
- Acesse a aplicação em `http://localhost:5000`

## Rodando os testes

- Para rodar os testes, utilize o comando:

  ```bash
  cd tests
  pytest
  ```

  ## Pytest-watch

  ```bash
  ptw --runner "pytest -s -q -p no:warnings"
  ```

---

# Bugs enfrentados

## Session

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

### Explicação técnica

- Python usa **referências (ponteiro)** para objetos mutáveis (dict, list)
- `session["quiz_session"]` retorna a referência ao objeto original, **não uma cópia**
- Modificar o objeto referenciado não aciona o `__setitem__` do dict pai.

- Resumo:
  > Ao acessar a `session`, recebo um ponteiro direto para o objeto na memória RAM. Como modifico apenas o dicionário filho, o Flask não detecta a alteração (`is_modified`permanece falso) e, por isso, não atualiza o cookie do navegador, descartando a mudança ao fim da requisição.

## Nomes de variáveis

- Muitos dos bugs que eu tive foram causados por nomes de variáveis mal escolhidos. Exemplo: em algumas classes, utilizar theme, em outras category e por aí vai.
  - Solução: padronizar os nomes das variáveis em todo o projeto.

## Retorno de dados

- O `db.execute` retorna uma lista de dicionários, considerando que eu tive que adequar esses dados para classes modelos foi algo bem exautivo, validar que os atributos estavam no seus devidos lugares.
  - Solução: criar métodos de classe `from_dict` e `to_dict` para facilitar a conversão entre dicionários e objetos modelo.

## Tratamento de erros

- Mesmo utilizando tratamento de erros com `try/except`, ao estourar um erro, faltava clareza na mensagem retornada.

  - Não busquei solução para esse problema, apenas melhorei as mensagens de erro - gostaria que ela fossem mais descritivas.

- Ainda, com testes obtive o mesmo problema: erros gigantescos e difíceis de interpretar - principalmente com os lançados pela biblioteca cs50, onde utilizava o SQL para querys.

# Melhorias futuras

- blueprints para organizar as rotas do flask.
- Implementar autenticação com tokens JWT para maior segurança ou flask-login - acredito que o JWT tenha mais relevância para demostrar habilidade em entrevista.
- Manipulação imperativa do DOM com JavaScript puro.
- Melhorar a interface do usuário.
