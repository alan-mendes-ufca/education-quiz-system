INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Fundamentos de Python', 'Python', 'Quiz básico sobre sintaxe e fundamentos da linguagem Python.',
'[{"id":1,"proposition":"Qual palavra-chave define uma função em Python?","theme":"Python","difficulty_points":10,"alternatives":["function","def","lambda","fun"],"correct_option_index":1},{"id":2,"proposition":"Qual desses tipos NÃO existe nativamente em Python?","theme":"Python","difficulty_points":10,"alternatives":["list","set","tuple","array"],"correct_option_index":3},{"id":3,"proposition":"Como se inicia um comentário em Python?","theme":"Python","difficulty_points":10,"alternatives":["//","#","--","/*"],"correct_option_index":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Lógica de Programação', 'Lógica', 'Questões sobre conceitos fundamentais de algoritmos e lógica.',
'[{"id":1,"proposition":"O que é um algoritmo?","theme":"Lógica","difficulty_points":10,"alternatives":["Um erro","Um conjunto de passos lógicos","Um hardware","Uma linguagem"],"correct_option_index":1},{"id":2,"proposition":"Qual estrutura representa repetição?","theme":"Lógica","difficulty_points":10,"alternatives":["if","switch","while","case"],"correct_option_index":2},{"id":3,"proposition":"Qual é o resultado: 2 + 2 * 2?","theme":"Lógica","difficulty_points":10,"alternatives":["6","8","4","10"],"correct_option_index":0}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('HTML Básico', 'Web', 'Perguntas essenciais para quem está iniciando no HTML.',
'[{"id":1,"proposition":"Qual tag define um título principal?","theme":"Web","difficulty_points":10,"alternatives":["<h1>","<header>","<title>","<head>"],"correct_option_index":0},{"id":2,"proposition":"Qual atributo define um link?","theme":"Web","difficulty_points":10,"alternatives":["ref","href","src","link"],"correct_option_index":1},{"id":3,"proposition":"Qual tag cria um parágrafo?","theme":"Web","difficulty_points":10,"alternatives":["<p>","<par>","<text>","<pg>"],"correct_option_index":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('CSS Básico', 'Web', 'Questões sobre estilos e seletores CSS.',
'[{"id":1,"proposition":"Qual propriedade muda a cor do texto?","theme":"Web","difficulty_points":10,"alternatives":["font-color","text-color","color","background"],"correct_option_index":2},{"id":2,"proposition":"Qual unidade representa pixels?","theme":"Web","difficulty_points":10,"alternatives":["%","px","em","pt"],"correct_option_index":1},{"id":3,"proposition":"Para aplicar estilo a um ID, usa-se:","theme":"Web","difficulty_points":10,"alternatives":[".id","#id","id:","id#"],"correct_option_index":1}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('JavaScript Intermediário', 'JavaScript', 'Quiz voltado para quem já conhece os fundamentos de JS.',
'[{"id":1,"proposition":"Qual tipo não é primitivo?","theme":"JavaScript","difficulty_points":10,"alternatives":["string","number","object","boolean"],"correct_option_index":2},{"id":2,"proposition":"Qual método adiciona elemento ao fim de um array?","theme":"JavaScript","difficulty_points":10,"alternatives":["push","pop","shift","unshift"],"correct_option_index":0},{"id":3,"proposition":"Qual símbolo representa estrita igualdade?","theme":"JavaScript","difficulty_points":10,"alternatives":["==","===","!=","!=="],"correct_option_index":1}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Banco de Dados SQL', 'Banco de Dados', 'Perguntas fundamentais sobre comandos SQL.',
'[{"id":1,"proposition":"Qual comando cria uma tabela?","theme":"Banco de Dados","difficulty_points":10,"alternatives":["INSERT","UPDATE","CREATE TABLE","ALTER"],"correct_option_index":2},{"id":2,"proposition":"Qual comando retorna dados?","theme":"Banco de Dados","difficulty_points":10,"alternatives":["SELECT","GET","FETCH","RETURN"],"correct_option_index":0},{"id":3,"proposition":"Qual cláusula filtra resultados?","theme":"Banco de Dados","difficulty_points":10,"alternatives":["ORDER BY","WHERE","GROUP BY","FILTER"],"correct_option_index":1}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Git e Versionamento', 'DevOps', 'Questões essenciais para trabalhar com Git no dia a dia.',
'[{"id":1,"proposition":"Qual comando inicia um repositório?","theme":"DevOps","difficulty_points":10,"alternatives":["git new","git init","git start","git create"],"correct_option_index":1},{"id":2,"proposition":"Qual comando envia commits ao repositório remoto?","theme":"DevOps","difficulty_points":10,"alternatives":["git push","git send","git upload","git remote"],"correct_option_index":0},{"id":3,"proposition":"Qual comando cria um branch?","theme":"DevOps","difficulty_points":10,"alternatives":["git branch <nome>","git new branch","git create","git fork"],"correct_option_index":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Programação Orientada a Objetos', 'POO', 'Questões sobre classes, objetos e pilares da POO.',
'[{"id":1,"proposition":"O que é um objeto?","theme":"POO","difficulty_points":10,"alternatives":["Um tipo de dado","Instância de uma classe","Um atributo","Um método"],"correct_option_index":1},{"id":2,"proposition":"Qual pilar representa reutilização?","theme":"POO","difficulty_points":10,"alternatives":["Herança","Polimorfismo","Encapsulamento","Abstração"],"correct_option_index":0},{"id":3,"proposition":"Métodos com o mesmo nome e comportamentos diferentes definem:","theme":"POO","difficulty_points":10,"alternatives":["Herança","Abstração","Polimorfismo","Casting"],"correct_option_index":2}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Segurança da Informação', 'Segurança', 'Quiz introdutório sobre ataques e boas práticas de segurança.',
'[{"id":1,"proposition":"O que significa SQL Injection?","theme":"Segurança","difficulty_points":10,"alternatives":["Ataque via scripts JS","Inserção maliciosa de comandos SQL","Acesso físico ao servidor","Explorar falhas de rede"],"correct_option_index":1},{"id":2,"proposition":"Senha forte deve ter:","theme":"Segurança","difficulty_points":10,"alternatives":["Apenas letras","Apenas números","Mistura de caracteres","08 dígitos fixos"],"correct_option_index":2},{"id":3,"proposition":"HTTPS significa:","theme":"Segurança","difficulty_points":10,"alternatives":["Protocolo inseguro","Criptografia SSL/TLS","Servidor offline","Banco de dados"],"correct_option_index":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Algoritmos e Estruturas de Dados', 'Algoritmos', 'Questões sobre complexidade, árvores e estruturas fundamentais.',
'[{"id":1,"proposition":"Árvore binária tem no máximo quantos filhos por nó?","theme":"Algoritmos","difficulty_points":10,"alternatives":["1","2","3","4"],"correct_option_index":1},{"id":2,"proposition":"Qual estrutura usa FIFO?","theme":"Algoritmos","difficulty_points":10,"alternatives":["Pilha","Árvore","Fila","Heap"],"correct_option_index":2},{"id":3,"proposition":"Complexidade do QuickSort médio:","theme":"Algoritmos","difficulty_points":10,"alternatives":["O(n)","O(log n)","O(n log n)","O(n²)"],"correct_option_index":2}]',
9);

-- Perguntas de Fundamentos de Python
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual palavra-chave define uma função em Python?', 'Python', 10, '["function","def","lambda","fun"]', 1),
('Qual desses tipos NÃO existe nativamente em Python?', 'Python', 10, '["list","set","tuple","array"]', 3),
('Como se inicia um comentário em Python?', 'Python', 10, '["//","#","--","/*"]', 1);

-- Perguntas de Lógica de Programação
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('O que é um algoritmo?', 'Lógica', 10, '["Um erro","Um conjunto de passos lógicos","Um hardware","Uma linguagem"]', 1),
('Qual estrutura representa repetição?', 'Lógica', 10, '["if","switch","while","case"]', 2),
('Qual é o resultado: 2 + 2 * 2?', 'Lógica', 10, '["6","8","4","10"]', 0);

-- Perguntas de HTML Básico
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual tag define um título principal?', 'Web', 10, '["<h1>","<header>","<title>","<head>"]', 0),
('Qual atributo define um link?', 'Web', 10, '["ref","href","src","link"]', 1),
('Qual tag cria um parágrafo?', 'Web', 10, '["<p>","<par>","<text>","<pg>"]', 0);

-- Perguntas de CSS Básico
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual propriedade muda a cor do texto?', 'Web', 10, '["font-color","text-color","color","background"]', 2),
('Qual unidade representa pixels?', 'Web', 10, '["%","px","em","pt"]', 1),
('Para aplicar estilo a um ID, usa-se:', 'Web', 10, '[".id","#id","id:","id#"]', 1);

-- Perguntas de JavaScript Intermediário
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual tipo não é primitivo?', 'JavaScript', 10, '["string","number","object","boolean"]', 2),
('Qual método adiciona elemento ao fim de um array?', 'JavaScript', 10, '["push","pop","shift","unshift"]', 0),
('Qual símbolo representa estrita igualdade?', 'JavaScript', 10, '["==","===","!=","!=="]', 1);

-- Perguntas de Banco de Dados SQL
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual comando cria uma tabela?', 'Banco de Dados', 10, '["INSERT","UPDATE","CREATE TABLE","ALTER"]', 2),
('Qual comando retorna dados?', 'Banco de Dados', 10, '["SELECT","GET","FETCH","RETURN"]', 0),
('Qual cláusula filtra resultados?', 'Banco de Dados', 10, '["ORDER BY","WHERE","GROUP BY","FILTER"]', 1);

-- Perguntas de Git e Versionamento
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Qual comando inicia um repositório?', 'DevOps', 10, '["git new","git init","git start","git create"]', 1),
('Qual comando envia commits ao repositório remoto?', 'DevOps', 10, '["git push","git send","git upload","git remote"]', 0),
('Qual comando cria um branch?', 'DevOps', 10, '["git branch <nome>","git new branch","git create","git fork"]', 0);

-- Perguntas de Programação Orientada a Objetos
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('O que é um objeto?', 'POO', 10, '["Um tipo de dado","Instância de uma classe","Um atributo","Um método"]', 1),
('Qual pilar representa reutilização?', 'POO', 10, '["Herança","Polimorfismo","Encapsulamento","Abstração"]', 0),
('Métodos com o mesmo nome e comportamentos diferentes definem:', 'POO', 10, '["Herança","Abstração","Polimorfismo","Casting"]', 2);

-- Perguntas de Segurança da Informação
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('O que significa SQL Injection?', 'Segurança', 10, '["Ataque via scripts JS","Inserção maliciosa de comandos SQL","Acesso físico ao servidor","Explorar falhas de rede"]', 1),
('Senha forte deve ter:', 'Segurança', 10, '["Apenas letras","Apenas números","Mistura de caracteres","08 dígitos fixos"]', 2),
('HTTPS significa:', 'Segurança', 10, '["Protocolo inseguro","Criptografia SSL/TLS","Servidor offline","Banco de dados"]', 1);

-- Perguntas de Algoritmos e Estruturas de Dados
INSERT INTO multiple_choice_question (proposition, theme, difficulty_points, alternatives, correct_option_index) VALUES
('Árvore binária tem no máximo quantos filhos por nó?', 'Algoritmos', 10, '["1","2","3","4"]', 1),
('Qual estrutura usa FIFO?', 'Algoritmos', 10, '["Pilha","Árvore","Fila","Heap"]', 2),
('Complexidade do QuickSort médio:', 'Algoritmos', 10, '["O(n)","O(log n)","O(n log n)","O(n²)"]', 2);
