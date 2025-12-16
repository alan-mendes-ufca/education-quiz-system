/* FUNÇÕES
 *
 * ESTADO:
 * - quizState: objeto global com perguntas/alternativas
 *
 * PERGUNTAS:
 * - addAQuestion(): adiciona nova pergunta
 * - renderQuestion(q, n): cria HTML do cartão
 * - updateQuestionText(id, txt): salva texto digitado
 * - removeQuestion(id): remove pergunta
 *
 * ALTERNATIVAS:
 * - renderAlternatives(qId): cria HTML [A][B][C]
 * - addAlternative(qId): adiciona alternativa
 * - removeAlternative(qId, label): remove alternativa
 * - updateAlternativeText(qId, label, txt): salva texto
 * - setCorrectAlternative(qId, label): marca correta
 *
 * AÇÕES:
 * - collectQuizData(): transforma em JSON
 * - validateQuiz(): verifica preenchimento
 * - saveQuiz(): envia para servidor
 * - cancelQuiz(): volta página anterior
 */

let quizState = {
  questions: [],
  totalQuestions: 0,
};

function addAQuestion() {
  // Cria um novo ID único para a pergunta
  const question_id = Date.now();

  // Cria objeto da pergunta com 2 alternativas vazias
  const question = {
    id: question_id,
    proposition: "",
    category: "",
    difficulty_points: 1,
    correct_option_index: null,
    alternatives: [
      {
        label: "a",
        text: "",
      },
      {
        label: "b",
        text: "",
      },
      {
        label: "c",
        text: "",
      },
    ],
  };

  // Adiciona no quizState.questions
  quizState.questions.push(question);
  quizState.totalQuestions += 1;

  // Chama renderQuestion() para mostrar na tela
  renderQuestion(question, quizState.questions.length);
}

function renderQuestion(q, qId) {
  // Pega o container:
  const qContainer = document.getElementById("questions-container");

  // Cria o HTML do cartão (card-header + card-body), 3. Adiciona eventos onclick, onchange nos inputs

  const card = `

        <div class="card mb-3" id="question-${q.id}">

            <div class="card-header d-flex justify-content-between align-items-center">
                <strong>Question #${qId}</strong>
                <button class="btn btn-sm btn-outline-danger" onclick="removeQuestion(${
                  q.id
                })">🗑️ remove</button>
            </div>

            <div class="card-body">
                <div class="mb-3">
                    <input type="text" 
                        class="form-control" 
                        id="question-text-${q.id}"
                        placeholder="enter your proposition here"
                        onchange="updateQuestionText(${
                          q.id
                        }, this.value)" required>
                    </div>
                <label class="form-label">Alternatives</label>
                <div id="alternatives-${q.id}">
                    <!-- renderAlternatives preenche aqui -->
                </div>

                <div class="btn-group">
                    <button class="btn btn-outline-primary btn-sm dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">difficulty points</button>
                        <ul class="dropdown-menu">
                            ${(() => {
                              let temp = "";
                              for (let i = 1; i <= 3; i++) {
                                temp += `<li><a class="dropdown-item" onclick="setDifficultyPoints(${q.id}, ${i})" >${i}</a></li>`;
                              }
                              return temp;
                            })()}
                        </ul>
                    </div>

                <button class="btn btn-sm btn-outline-secondary" 
                        onclick="addAlternative(${q.id})">
                    <strong>+ add alternatives</strong>
                </button>
            </div>
        </div>
        `;

  // Insere no container
  qContainer.insertAdjacentHTML("beforeend", card);

  const question_count = document.getElementById("question-count");
  question_count.textContent = `number of questions: ${quizState.totalQuestions}`;

  // Chama renderAlternatives() para criar as alternativas
  renderAlternatives(q.id);
}

function setDifficultyPoints(qId, point) {
  if (![1, 2, 3].includes(point)) {
    throw new Error("Assigned points are out of the accepted range.");
  }
  const q = quizState.questions.find((q) => q.id == qId);
  q.difficulty_points = point;
}

function renderAlternatives(questionId) {
  // Encontra a pergunta no quizState
  const q = quizState.questions.find((q) => q.id == questionId); // Buscando as questões dentro do array e depois validando seu id.
  // Pega o container
  const c = document.getElementById("alternatives-" + questionId);
  // Limpa o container (innerHTML = '')
  c.innerHTML = "";
  // Para cada alternativa, cria o HTML com:
  //    - Radio button
  //    - Letra [A], [B], [C]...
  //    - Input de texto
  //    - Botão remover (se tiver mais de 2)
  // 5. Adiciona no container
  let count = 0;
  for (const alt of q.alternatives) {
    c.insertAdjacentHTML(
      "beforeend",
      `
                <div class="input-group mb-2">
                    <div class="input-group-text">
                        <input class="form-check-input" type="radio" name="correct-${
                          q.id
                        }" id="alt-${alt.label}-${q.id}"
                        ${count == q.correct_option_index ? "checked" : ""}
                        onchange="setCorrectAlternative(${q.id}, '${
        alt.label
      }')" required>
                    </div>
                    <span class="input-group-text">[${alt.label.toUpperCase()}]</span>
                    <input type="text" class="form-control" placeholder="Enter alternative text" value="${
                      alt.text
                    }" onchange="updateAlternativeText(${q.id}, '${
        alt.label
      }', this.value)" required>
                    
                    ${
                      q.alternatives.length > 2
                        ? `<button class="btn btn-sm btn-outline-danger" 
                    onclick="removeAlternative(${q.id}, '${alt.label}')">✕</button>`
                        : ""
                    }    
                </div>

            `
    );
    count++;
  }
}

function updateQuestionText(id, txt) {
  // 1. Encontre a pergunta no quizState
  const q = quizState.questions.find((q) => q.id == id); // Aponta para o objeto, não é uma cópia, ou se for alterado nesse escopo tambpém será alterado em quizStatus.
  // 2. Alterar a porposição
  q.proposition = txt;
}

function removeQuestion(id) {
  // 1. Confirma com o usuário: confirm('Tem certeza?')
  const userChoice = confirm("Do you really want to remove this question?");

  if (userChoice) {
    // 2. Remove do array
    quizState.questions = quizState.questions.filter((q) => q.id != id);
    // 3. Remove do DOM
    document.getElementById("question-" + id).remove();
    quizState.totalQuestions -= 1;

    const question_count = document.getElementById("question-count");
    question_count.textContent = `number of questions: ${quizState.totalQuestions}`;
  }
}

function addAlternative(id) {
  const q = quizState.questions.find((q) => q.id == id);
  // Adicionar nova alternativa a questão
  const len = q.alternatives.length;

  // REGRA DE NEGÓCIO: só é possível adicionar até 5 alternativas
  if (len == 5) {
    throw new Error("Só é possível adicionar até 5 alternativas.");
  }

  const lastLabel = q.alternatives[len - 1];
  const newLabel = String.fromCharCode(lastLabel.label.charCodeAt(0) + 1);
  q.alternatives.push({
    label: newLabel,
    text: "",
  });

  renderAlternatives(id);
}

function removeAlternative(qId, label) {
  const q = quizState.questions.find((q) => q.id == qId);
  if (q.alternatives.length <= 3) {
    throw new Error(
      "Não é possível remover, o número de alternativas deve ser maior ou igual a 3 e menor igual a 5."
    );
  }
  const rmvIndex = q.alternatives.findIndex((alt) => alt.label == label);
  if (q.correct_option_index == rmvIndex) {
    q.correct_option_index = null;
  }
  if (q.correct_option_index != null && rmvIndex < q.correct_option_index) {
    q.correct_option_index--;
  }
  q.alternatives = q.alternatives.filter((alt) => alt.label != label);
  renderAlternatives(qId);
}

function updateAlternativeText(qId, label, txt) {
  const q = quizState.questions.find((q) => q.id == qId);
  const alt = q.alternatives.find((alt) => alt.label == label);
  alt.text = txt;
}

function setCorrectAlternative(qId, label) {
  const q = quizState.questions.find((q) => q.id == qId);
  q.correct_option_index = q.alternatives.findIndex(
    (alt) => alt.label == label
  );

  renderAlternatives(qId);
}

function collectQuizData() {
  // Buscar parâmetros: title, description,
  // questões(proposition, category, diffcultry_points, alternatives,correct_option_index)

  const titleValue = document.getElementById("quiz-title").value; // retorna html, para pegar o valor inserido pelo usuário é necessário o método `.value`;
  const descriptionValue = document.getElementById("quiz-description").value;
  const quizCategoryValue = document
    .getElementById("quiz-category")
    .value.toLowerCase();

  const categoryValue = document.getElementById("quiz-category").value;
  const questions = quizState.questions;
  for (const q of questions) {
    q.category = categoryValue;
  }

  return {
    title: titleValue,
    category: quizCategoryValue,
    description: descriptionValue,
    questions: questions,
  };
}

function validateQuiz() {
  const titleValue = document.getElementById("quiz-title").value.trim();
  const descriptionValue = document
    .getElementById("quiz-description")
    .value.trim();
  const quizCategoryValue = document
    .getElementById("quiz-category")
    .value.trim();
  const categoryValue = document.getElementById("quiz-category").value.trim();

  if (!titleValue) throw new Error("Título do quiz não pode estar vazio.");
  if (!descriptionValue)
    throw new Error("Descrição do quiz não pode estar vazia.");
  if (!quizCategoryValue) throw new Error("Categoria de quiz não descrita.");
  if (!categoryValue)
    throw new Error("Categoria do quiz não pode estar vazia.");

  quizState.questions.forEach((q) => {
    // REGRA DE NEGÓCIO: verificando se alternativas corretas estão preenchidas e se esse índice é válido
    if (
      q.correct_option_index == null ||
      q.correct_option_index >= q.alternatives.length
    ) {
      throw new Error(
        "Alternativa correta não foi preenchida ou está fora do escopo das alterantivas."
      );
    }

    // verificando se todas as questões têm enunciado preenchido
    if (!q.proposition.trim()) {
      // trim é o strip do python!
      throw new Error("O quiz tem questões com enunciado não preenchido.");
    }

    // verificando se todas as questões tem alternativas preenchidas.
    q.alternatives.forEach((alt) => {
      if (!alt.label || !alt.text.trim()) {
        throw new Error(
          "O quiz tem questões com alternativas não preenchidas."
        );
      }
    });
  });
}

async function saveQuiz() {
  try {
    validateQuiz();
    const quizInfo = collectQuizData();
    console.log(quizInfo);

    const response = await fetch("/quiz/save", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(quizInfo),
    });

    if (response.ok) {
      alert("✅ Quiz salvo com sucesso!");
      window.location.href = "/quizzes"; // Redireciona após salvar
    } else {
      const error = await response.json();
      alert("❌ Erro: " + error.message);
    }
  } catch (error) {
    alert("Erro ao enviar o quiz: " + error.message);
  }
}

function cancelQuiz() {
  window.location.replace("/quizzes");
}
