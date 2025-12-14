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
