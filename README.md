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
## UML

Classe: QuestionRepo
Atributos: themes, qtd_min_alt, qtd_max_alt, qtd_quest_solicitadas.
Métodos: creat_quest, select_quest, update_quest, duplicity_validation.
- Utilizada principalmente para consultas de perguntas no banco de dados e retorno de uma seleção(dicionário com as questões, alternativas, peso por nível de dificuldade e o índice da alternativa correta) das mesmas.

Classe: Quiz
Atributos: title, selected_q = Questions(), max_possible_punctuation, template, time_limit.
Métodos: generate_template, calc_max_punc, player_punct, count_time, import_configs.
- Principal responsável pelo fluxo do jogo.

Classe: Log
Atributos: puntuation, time_to_reply, responses_history.
- Dados brutos (json ou banco de dados).

Class: Statistics
Atributos: accuracy_rate, theme_accuracy_rate, players_ranking, most_missed_questions, user_progress.
Métodos: total_correct_answers, correct_answers_by_topic, user_ranking_correct_answers, ranking_incorrect_answers, progress_tracking.
- Usando os dados brutos, constrói-se as estatísticas.

Class: UserRepo
Atributos: id, name, password, email.
Métodos: creat_user, select_user, update_user, delete_user.

Class: Auth
Atributos: login, loggout