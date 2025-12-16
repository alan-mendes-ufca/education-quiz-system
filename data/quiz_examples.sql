INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Fundamentos de Python', 'python', 'Quiz básico sobre sintaxe e fundamentos da linguagem Python.',
'[{"id":1,"proposition":"Qual palavra-chave define uma função em Python?","category":"python","difficulty_points":10,"alternatives":["function","def","lambda","fun"],"correct_option_index":1},{"id":2,"proposition":"Qual desses tipos NÃO existe nativamente em Python?","category":"python","difficulty_points":10,"alternatives":["list","set","tuple","array"],"correct_option_index":3},{"id":3,"proposition":"Como se inicia um comentário em Python?","category":"python","difficulty_points":10,"alternatives":["//","#","--","/*"],"correct_option_index":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Lógica de Programação', 'lógica', 'Questões sobre conceitos fundamentais de algoritmos e lógica.',
'[{"id":1,"proposition":"O que é um algoritmo?","category":"lógica","difficulty_points":10,"alternatives":["Um erro","Um conjunto de passos lógicos","Um hardware","Uma linguagem"],"correct_option_index":1},{"id":2,"proposition":"Qual estrutura representa repetição?","category":"lógica","difficulty_points":10,"alternatives":["if","switch","while","case"],"correct_option_index":2},{"id":3,"proposition":"Qual é o resultado: 2 + 2 * 2?","category":"lógica","difficulty_points":10,"alternatives":["6","8","4","10"],"correct_option_index":0}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('HTML Básico', 'web', 'Perguntas essenciais para quem está iniciando no HTML.',
'[{"id":1,"proposition":"Qual tag define um título principal?","category":"web","difficulty_points":10,"alternatives":["<h1>","<header>","<title>","<head>"],"correct_option_index":0},{"id":2,"proposition":"Qual atributo define um link?","category":"web","difficulty_points":10,"alternatives":["ref","href","src","link"],"correct_option_index":1},{"id":3,"proposition":"Qual tag cria um parágrafo?","category":"web","difficulty_points":10,"alternatives":["<p>","<par>","<text>","<pg>"],"correct_option_index":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('CSS Básico', 'web', 'Questões sobre estilos e seletores CSS.',
'[{"id":1,"proposition":"Qual propriedade muda a cor do texto?","category":"web","difficulty_points":10,"alternatives":["font-color","text-color","color","background"],"correct_option_index":2},{"id":2,"proposition":"Qual unidade representa pixels?","category":"web","difficulty_points":10,"alternatives":["%","px","em","pt"],"correct_option_index":1},{"id":3,"proposition":"Para aplicar estilo a um ID, usa-se:","category":"web","difficulty_points":10,"alternatives":[".id","#id","id:","id#"],"correct_option_index":1}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('JavaScript Intermediário', 'javascript', 'Quiz voltado para quem já conhece os fundamentos de JS.',
'[{"id":1,"proposition":"Qual tipo não é primitivo?","category":"javascript","difficulty_points":10,"alternatives":["string","number","object","boolean"],"correct_option_index":2},{"id":2,"proposition":"Qual método adiciona elemento ao fim de um array?","category":"javascript","difficulty_points":10,"alternatives":["push","pop","shift","unshift"],"correct_option_index":0},{"id":3,"proposition":"Qual símbolo representa estrita igualdade?","category":"javascript","difficulty_points":10,"alternatives":["==","===","!=","!=="],"correct_option_index":1}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Banco de Dados SQL', 'banco de dados', 'Perguntas fundamentais sobre comandos SQL.',
'[{"id":1,"proposition":"Qual comando cria uma tabela?","category":"banco de dados","difficulty_points":10,"alternatives":["INSERT","UPDATE","CREATE TABLE","ALTER"],"correct_option_index":2},{"id":2,"proposition":"Qual comando retorna dados?","category":"banco de dados","difficulty_points":10,"alternatives":["SELECT","GET","FETCH","RETURN"],"correct_option_index":0},{"id":3,"proposition":"Qual cláusula filtra resultados?","category":"banco de dados","difficulty_points":10,"alternatives":["ORDER BY","WHERE","GROUP BY","FILTER"],"correct_option_index":1}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Git e Versionamento', 'devops', 'Questões essenciais para trabalhar com Git no dia a dia.',
'[{"id":1,"proposition":"Qual comando inicia um repositório?","category":"devops","difficulty_points":10,"alternatives":["git new","git init","git start","git create"],"correct_option_index":1},{"id":2,"proposition":"Qual comando envia commits ao repositório remoto?","category":"devops","difficulty_points":10,"alternatives":["git push","git send","git upload","git remote"],"correct_option_index":0},{"id":3,"proposition":"Qual comando cria um branch?","category":"devops","difficulty_points":10,"alternatives":["git branch <nome>","git new branch","git create","git fork"],"correct_option_index":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Programação Orientada a Objetos', 'poo', 'Questões sobre classes, objetos e pilares da POO.',
'[{"id":1,"proposition":"O que é um objeto?","category":"poo","difficulty_points":10,"alternatives":["Um tipo de dado","Instância de uma classe","Um atributo","Um método"],"correct_option_index":1},{"id":2,"proposition":"Qual pilar representa reutilização?","category":"poo","difficulty_points":10,"alternatives":["Herança","Polimorfismo","Encapsulamento","Abstração"],"correct_option_index":0},{"id":3,"proposition":"Métodos com o mesmo nome e comportamentos diferentes definem:","category":"poo","difficulty_points":10,"alternatives":["Herança","Abstração","Polimorfismo","Casting"],"correct_option_index":2}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Segurança da Informação', 'segurança', 'Quiz introdutório sobre ataques e boas práticas de segurança.',
'[{"id":1,"proposition":"O que significa SQL Injection?","category":"segurança","difficulty_points":10,"alternatives":["Ataque via scripts JS","Inserção maliciosa de comandos SQL","Acesso físico ao servidor","Explorar falhas de rede"],"correct_option_index":1},{"id":2,"proposition":"Senha forte deve ter:","category":"segurança","difficulty_points":10,"alternatives":["Apenas letras","Apenas números","Mistura de caracteres","08 dígitos fixos"],"correct_option_index":2},{"id":3,"proposition":"HTTPS significa:","category":"segurança","difficulty_points":10,"alternatives":["Protocolo inseguro","Criptografia SSL/TLS","Servidor offline","Banco de dados"],"correct_option_index":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Algoritmos e Estruturas de Dados', 'algoritmos', 'Questões sobre complexidade, árvores e estruturas fundamentais.',
'[{"id":1,"proposition":"Árvore binária tem no máximo quantos filhos por nó?","category":"algoritmos","difficulty_points":10,"alternatives":["1","2","3","4"],"correct_option_index":1},{"id":2,"proposition":"Qual estrutura usa FIFO?","category":"algoritmos","difficulty_points":10,"alternatives":["Pilha","Árvore","Fila","Heap"],"correct_option_index":2},{"id":3,"proposition":"Complexidade do QuickSort médio:","category":"algoritmos","difficulty_points":10,"alternatives":["O(n)","O(log n)","O(n log n)","O(n²)"],"correct_option_index":2}]',
9);

-- Perguntas de Fundamentos de Python
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual palavra-chave define uma função em Python?', 'python', 10, '["function","def","lambda","fun"]', 1),
('Qual desses tipos NÃO existe nativamente em Python?', 'python', 10, '["list","set","tuple","array"]', 3),
('Como se inicia um comentário em Python?', 'python', 10, '["//","#","--","/*"]', 1);

-- Perguntas de Lógica de Programação
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('O que é um algoritmo?', 'lógica', 10, '["Um erro","Um conjunto de passos lógicos","Um hardware","Uma linguagem"]', 1),
('Qual estrutura representa repetição?', 'lógica', 10, '["if","switch","while","case"]', 2),
('Qual é o resultado: 2 + 2 * 2?', 'lógica', 10, '["6","8","4","10"]', 0);

-- Perguntas de HTML Básico
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual tag define um título principal?', 'web', 10, '["<h1>","<header>","<title>","<head>"]', 0),
('Qual atributo define um link?', 'web', 10, '["ref","href","src","link"]', 1),
('Qual tag cria um parágrafo?', 'web', 10, '["<p>","<par>","<text>","<pg>"]', 0);

-- Perguntas de CSS Básico
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual propriedade muda a cor do texto?', 'web', 10, '["font-color","text-color","color","background"]', 2),
('Qual unidade representa pixels?', 'web', 10, '["%","px","em","pt"]', 1),
('Para aplicar estilo a um ID, usa-se:', 'web', 10, '[".id","#id","id:","id#"]', 1);

-- Perguntas de JavaScript Intermediário
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual tipo não é primitivo?', 'javascript', 10, '["string","number","object","boolean"]', 2),
('Qual método adiciona elemento ao fim de um array?', 'javascript', 10, '["push","pop","shift","unshift"]', 0),
('Qual símbolo representa estrita igualdade?', 'javascript', 10, '["==","===","!=","!=="]', 1);

-- Perguntas de Banco de Dados SQL
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual comando cria uma tabela?', 'banco de dados', 10, '["INSERT","UPDATE","CREATE TABLE","ALTER"]', 2),
('Qual comando retorna dados?', 'banco de dados', 10, '["SELECT","GET","FETCH","RETURN"]', 0),
('Qual cláusula filtra resultados?', 'banco de dados', 10, '["ORDER BY","WHERE","GROUP BY","FILTER"]', 1);

-- Perguntas de Git e Versionamento
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Qual comando inicia um repositório?', 'devops', 10, '["git new","git init","git start","git create"]', 1),
('Qual comando envia commits ao repositório remoto?', 'devops', 10, '["git push","git send","git upload","git remote"]', 0),
('Qual comando cria um branch?', 'devops', 10, '["git branch <nome>","git new branch","git create","git fork"]', 0);

-- Perguntas de Programação Orientada a Objetos
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('O que é um objeto?', 'poo', 10, '["Um tipo de dado","Instância de uma classe","Um atributo","Um método"]', 1),
('Qual pilar representa reutilização?', 'poo', 10, '["Herança","Polimorfismo","Encapsulamento","Abstração"]', 0),
('Métodos com o mesmo nome e comportamentos diferentes definem:', 'poo', 10, '["Herança","Abstração","Polimorfismo","Casting"]', 2);

-- Perguntas de Segurança da Informação
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('O que significa SQL Injection?', 'segurança', 10, '["Ataque via scripts JS","Inserção maliciosa de comandos SQL","Acesso físico ao servidor","Explorar falhas de rede"]', 1),
('Senha forte deve ter:', 'segurança', 10, '["Apenas letras","Apenas números","Mistura de caracteres","08 dígitos fixos"]', 2),
('HTTPS significa:', 'segurança', 10, '["Protocolo inseguro","Criptografia SSL/TLS","Servidor offline","Banco de dados"]', 1);

-- Perguntas de Algoritmos e Estruturas de Dados
INSERT INTO multiple_choice_question (proposition, category, difficulty_points, alternatives, correct_option_index) VALUES
('Árvore binária tem no máximo quantos filhos por nó?', 'algoritmos', 10, '["1","2","3","4"]', 1),
('Qual estrutura usa FIFO?', 'algoritmos', 10, '["Pilha","Árvore","Fila","Heap"]', 2),
('Complexidade do QuickSort médio:', 'algoritmos', 10, '["O(n)","O(log n)","O(n log n)","O(n²)"]', 2);
