# 📚 Educational Quiz System

Sistema web para criar, gerenciar e responder quizzes de múltipla escolha, com estatísticas e ranking de jogadores.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Tecnologias](#-tecnologias)
- [Como Rodar](#-como-rodar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Arquitetura (UML)](#-arquitetura-uml)
- [Testes](#-testes)
- [Bugs e Soluções](#-bugs-e-soluções)
- [Melhorias Futuras](#-melhorias-futuras)

---

## 🎯 Sobre o Projeto

Sistema de API que permite **criar, gerenciar e responder** quizzes com perguntas de múltipla escolha, incluindo:

- ✅ Autenticação de usuários (login/registro)
- ✅ Criação de quizzes personalizados
- ✅ Catálogo de quizzes por categoria
- ✅ Sistema de pontuação e ranking
- ✅ Estatísticas de desempenho

**Objetivo acadêmico:** Demonstrar conhecimento em Programação Orientada a Objetos, seguindo princípios de responsabilidade única e arquitetura em camadas.

---

## 🛠 Tecnologias

| Tecnologia      | Descrição                           |
| --------------- | ----------------------------------- |
| **Flask**       | Framework web leve para Python      |
| **SQLite3**     | Banco de dados relacional embarcado |
| **CS50 SQL**    | Biblioteca para queries SQL         |
| **Pytest**      | Framework de testes automatizados   |
| **Bootstrap 5** | Framework CSS para interface        |
| **Werkzeug**    | Hashing seguro de senhas            |

---

## 🚀 Como Rodar

### Requisitos

- Python 3.10+
- SQLite (já incluído no Python)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/alan-mendes-ufca/education-quiz-system
cd education-quiz-system

# Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
sqlite3 data/app.db < data/schema.sql

# Configure a variável de ambiente
echo "MY_SECRET_KEY=sua_chave_secreta" > .env

# Inicie o servidor
flask run --debug

# Por fim
Acesse: **http://localhost:5000**

```

---

## 📁 Estrutura do Projeto

```
education-quiz-system/
├── flaskr/                    # Aplicação Flask
│   ├── app.py                 # Rotas e configuração
│   ├── helpers.py             # Funções auxiliares
│   ├── static/                # CSS e JavaScript
│   └── templates/             # Templates HTML (Jinja2)
│
├── models/                    # Camada de Modelos (dados)
│   ├── User.py
│   ├── Quiz.py
│   ├── Question.py
│   ├── MultipleChoice.py
│   ├── QuizResult.py
│   ├── QuizSession.py
│   └── UserAnswer.py
│
├── repositories/              # Camada de Repositórios (CRUD)
│   ├── UserRepository.py
│   ├── QuizRepository.py
│   ├── QuestionRepository.py
│   ├── QuizResultRepository.py
│   ├── QuizSessionRepository.py
│   └── UserAnswerRepository.py
│
├── services/                  # Camada de Serviços (regras de negócio)
│   ├── AuthService.py
│   ├── QuizGame.py
│   └── StatisticsService.py
│
├── data/                      # Banco de dados
│   ├── schema.sql
│   └── app.db
│
└── tests/                     # Testes automatizados
```

---

## 🏗 Arquitetura (UML)

### Arquitetura em Camadas

O projeto segue uma **arquitetura em camadas** que separa responsabilidades e facilita manutenção:

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE APRESENTAÇÃO                   │
│         (Flask Routes + Templates Jinja2 + JS)              │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    CAMADA DE SERVIÇOS                       │
│        (AuthService, QuizGame, StatisticsService)           │
│              Regras de negócio e orquestração               │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                   CAMADA DE REPOSITÓRIO                     │
│    (UserRepository, QuizRepository, QuestionRepository...)  │
│                  Persistência e CRUD                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    CAMADA DE MODELOS                        │
│       (User, Quiz, Question, QuizResult, UserAnswer...)     │
│                 Encapsulamento de dados                     │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                    BANCO DE DADOS                           │
│                      (SQLite3)                              │
└─────────────────────────────────────────────────────────────┘
```

**Princípios aplicados:**

- **Responsabilidade Única (SRP):** Cada classe tem uma única responsabilidade
- **Encapsulamento:** Modelos protegem dados com atributos privados/protegidos

### Fluxo de uma Requisição

```
Requisição HTTP → @app.route → Service → Repository → Model → DB
```

---

### Camada 1: Modelos (Encapsulamento)

Classes que guardam dados com getters/setters e validações:

| Classe                   | Descrição                                          | Relacionamentos                    |
| ------------------------ | -------------------------------------------------- | ---------------------------------- |
| `User`                   | Dados do usuário (id, name, email, password_hash)  | Usado por AuthService, QuizGame    |
| `Question`               | Classe abstrata base para questões                 | Herdada por MultipleChoiceQuestion |
| `MultipleChoiceQuestion` | Questão de múltipla escolha com alternativas       | Compõe Quiz (1:N)                  |
| `Quiz`                   | Configuração do quiz (título, categoria, questões) | Contém lista de Questions          |
| `QuizResult`             | Resultado final de uma partida                     | Referencia User e Quiz             |
| `QuizSession`            | Estado da sessão durante o jogo                    | Referencia User e Quiz             |
| `UserAnswer`             | Resposta individual do usuário                     | Referencia User, Quiz e Question   |

---

### Camada 2: Repositórios (CRUD)

Classes focadas em persistência de dados. Cada repositório encapsula operações SQL para uma entidade:

| Classe                  | Métodos principais                                   | Modelo relacionado |
| ----------------------- | ---------------------------------------------------- | ------------------ |
| `UserRepository`        | create, get_by_id, get_by_email, update              | User               |
| `QuizRepository`        | create, get_by_id, get_by_category, get_most_popular | Quiz               |
| `QuestionRepository`    | create, get_by_category, get_random_questions        | MultipleChoice     |
| `QuizResultRepository`  | save, get_results_by_user, get_ranking               | QuizResult         |
| `QuizSessionRepository` | create, get_by_id, update_session                    | QuizSession        |
| `UserAnswerRepository`  | save, get_most_missed_question_all                   | UserAnswer         |

---

### Camada 3: Serviços (Regras de Negócio)

Classes que orquestram a lógica da aplicação, utilizando repositórios e modelos:

| Classe              | Responsabilidade                   | Dependências                                           |
| ------------------- | ---------------------------------- | ------------------------------------------------------ |
| `AuthService`       | Login, registro e logout           | UserRepository                                         |
| `QuizGame`          | Fluxo de uma sessão de jogo        | Quiz, User, UserAnswerRepository, QuizResultRepository |
| `StatisticsService` | Cálculo de estatísticas e rankings | QuizResultRepository, UserAnswerRepository             |

---

## 🧪 Testes

```bash
# Navegue para a pasta de testes
cd tests

# Execute todos os testes
pytest

# Com watch mode (reexecuta ao salvar)
ptw --runner "pytest -s -q -p no:warnings"
```

---

## 🐛 Bugs e Soluções

### 1. Session não persistindo alterações

**Problema:** Modificar valores aninhados na session do Flask não salvava as alterações.

```python
# ❌ Não funciona
session["quiz_session"]["current_question"] += 1

# ✅ Solução: reatribuir o dicionário
session_data = session["quiz_session"]
session_data["current_question"] += 1
session["quiz_session"] = session_data
```

**Explicação:** O Flask só detecta modificações quando `__setitem__` é chamado diretamente na session.

### 2. Inconsistência em nomes de variáveis

**Problema:** Usar `theme` em alguns lugares e `category` em outros causava bugs.

**Solução:** Padronizar nomenclatura em todo o projeto.

### 3. Conversão de dados do banco

**Problema:** `db.execute` retorna lista de dicionários, não objetos.

**Solução:** Criar métodos `from_dict()` e `to_dict()` nos modelos.

---

## 🔮 Melhorias Futuras

- [ ] **Flask Blueprints** para organizar rotas
- [ ] **JWT ou Flask-Login** para autenticação mais robusta
- [ ] **Testes de integração** mais abrangentes
- [ ] **Interface melhorada** com melhor UX

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.

---

<div align="center">
  <strong>Desenvolvido por Alan Mendes</strong>
</div>
