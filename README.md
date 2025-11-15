# Education-quiz-system

Assignment 01 for the Object-Oriented Programming course: Educational quiz system.

# FastApi x Flask

- O fastapi (Estrutura de camadas) recomenda o uso de dois tipos de classes principais: Schemas (`Pydantic`) e Models (Banco de dados).

  - Schemas(/routers): "forma dos dados", _validam_ requests e responses.

    - Cardápio: pedir e receber.

  - Models(/models): classes para as tabelas no banco(`SQLAlquemy`).
    - Despensa: local de armazenamento.

  (Funções que executam ações no código - **Abordagem funcional**)

  - Services (/services): executa as regras de negócio.
    - cozinheiro: fluxo de ações.

- Com o `flask` é possível a criação de uma estrutura de projeto mais simples, suprindo todos os requisitos dados (https://docs.google.com/document/d/19PaqgTEIkA0t21m5EJ4H3zBNMEdZD4KC/edit). `Por fim, pela simplicidade o framework escolhidopara o desenvolvimetno desse projeto foi o flask.`

- Dado padrão, vamos criar uma esqueleto para as classes (https://docs.google.com/spreadsheets/d/1IfV9YpOZb5DOFYyjDnL4ypVJ2WzAEqxyRfvTDKmn29Y/edit?usp=sharing):
## UML - Refatorado (*Princípio de responsabilidade única, arquitetura em camadas -> Arquitetura de Software*)

### Bloco 1 Modelo de dados (Encapsulamento) : *classes que apenas guardam dados*

Classe: `User` (Guarda dados)
Atributos: __user_id (privado), name, email, __password_hash (privado).
Métodos: getters e setters.

Classe: `Question` (Abstrato, será importado pelas classes filhas)
Atributos: __question_id (privado), text, theme, difficulty_points.
Métodos: check_answer(user_answer).

Classe: `MultipleChoiceQuestion(Question)`
Atributos: options: list, __corretct_option_index: int.
Métodos: check_answer(user_answer_index) (implementa o método da classe-mãe).

Classe: `TrueFalseQuestion(Question)`
Atributos: __is_correct_true: bool.
Métodos: check_answer(user_answer: bool) (implementa o método da classe-mãe).

Classe: `QuestionRepo`
Atributos: themes, qtd_min_alt, qtd_max_alt, qtd_quest_solicitadas.
Métodos: creat_quest, select_quest, update_quest, duplicity_validation.

Classe: `Quiz` (Modelo)
Atributos: __quiz_id (privado), title, questions: list[Questions].
Métodos: get_questions(), get_max_score().

Classe: `QuizResult`
Atributos: user: User, quiz: Quiz, score_achieved: int, time_taken: float, responses_history: dict.

----------------------------------------------------------------------------------------------

### Bloco 2: Repositório (Acesso a dados): *Classes focadas apenas no CRUD*

Classe: `UserRepositoty`
Atributos: (conexão com o banco de dados).
Médodos: create(user: User), get_by_id(user_id) -> User, get_by_email(email) -> User, update(user: User).

Classe: `QuestionRepository`
Atributos: (conexão com o banco de dados).
Métodos: create(question: Question), get_by_theme(theme) -> list[Question], get_random_questions(theme, count) -> list[Question].

Classe: `QuizResultRepository`
Atributos: (conexão com o banco de dados).
Métodos: save(result: QuizResult), get_results_by_user(user: User) -> list[QuizResult].

----------------------------------------------------------------------------------------------

### Bloco 3: Serviços: *classes que orquestrão a lógica do aplicatio*
Classe: `AuthService`
Atributos: user_repository: UserRepository.
Métodos: login(email, password) -> User, register(name, email, password) -> User, logout().

Classe: `QuizGame`
Atributos: quiz: Quiz, user: User, current_question_index: int, user_answers: list, start_time.
Métodos: start_game(), get_current_question() -> Question, submit_answer(answer), finish_game() -> QuizResult (cria e retorna um objeto QuizResult).

Classe: `StatisticsService`
Atributos: result_repository: QuizResultRepository.
Métodos: get_accuracy_rate(user: User) -> float, get_player_ranking() -> list, get_most_missed_questions() -> list[Question].

- Todas essas classes foram modeladas pela IA apartir do **meu UML base** (pode ser acessado nesse commit: `3341d3f Initial UML`).
 Lógico que nmão simplesmente copiei e colei, fui escrevendo cada uma para entender seu conceito.

- Utilizando o flask o fluxo de repetição faria assim :
`Requisição HTTP → Rota do Flask (@app.route) → Serviço (QuizGame, AuthService) → Repositório (UserRepository) → Banco de Dados`

- Preciso estudar sobre Arquitetura de Software. CONTEÙDOS: Clean Architecture.