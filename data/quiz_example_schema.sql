INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Fundamentos de Python', 'Python', 'Quiz básico sobre sintaxe e fundamentos da linguagem Python.',
'[{"q":"Qual palavra-chave define uma função em Python?","a":["function","def","lambda","fun"],"c":1},{"q":"Qual desses tipos NÃO existe nativamente em Python?","a":["list","set","tuple","array"],"c":3},{"q":"Como se inicia um comentário em Python?","a":["//","#","--","/*"],"c":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Lógica de Programação', 'Lógica', 'Questões sobre conceitos fundamentais de algoritmos e lógica.',
'[{"q":"O que é um algoritmo?","a":["Um erro","Um conjunto de passos lógicos","Um hardware","Uma linguagem"],"c":1},{"q":"Qual estrutura representa repetição?","a":["if","switch","while","case"],"c":2},{"q":"Qual é o resultado: 2 + 2 * 2?","a":["6","8","4","10"],"c":0}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('HTML Básico', 'Web', 'Perguntas essenciais para quem está iniciando no HTML.',
'[{"q":"Qual tag define um título principal?","a":["<h1>","<header>","<title>","<head>"],"c":0},{"q":"Qual atributo define um link?","a":["ref","href","src","link"],"c":1},{"q":"Qual tag cria um parágrafo?","a":["<p>","<par>","<text>","<pg>"],"c":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('CSS Básico', 'Web', 'Questões sobre estilos e seletores CSS.',
'[{"q":"Qual propriedade muda a cor do texto?","a":["font-color","text-color","color","background"],"c":2},{"q":"Qual unidade representa pixels?","a":["%","px","em","pt"],"c":1},{"q":"Para aplicar estilo a um ID, usa-se:","a":[".id","#id","id:","id#"],"c":1}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('JavaScript Intermediário', 'JavaScript', 'Quiz voltado para quem já conhece os fundamentos de JS.',
'[{"q":"Qual tipo não é primitivo?","a":["string","number","object","boolean"],"c":2},{"q":"Qual método adiciona elemento ao fim de um array?","a":["push","pop","shift","unshift"],"c":0},{"q":"Qual símbolo representa estrita igualdade?","a":["==","===","!=","!=="],"c":1}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Banco de Dados SQL', 'Banco de Dados', 'Perguntas fundamentais sobre comandos SQL.',
'[{"q":"Qual comando cria uma tabela?","a":["INSERT","UPDATE","CREATE TABLE","ALTER"],"c":2},{"q":"Qual comando retorna dados?","a":["SELECT","GET","FETCH","RETURN"],"c":0},{"q":"Qual cláusula filtra resultados?","a":["ORDER BY","WHERE","GROUP BY","FILTER"],"c":1}]',
9);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Git e Versionamento', 'DevOps', 'Questões essenciais para trabalhar com Git no dia a dia.',
'[{"q":"Qual comando inicia um repositório?","a":["git new","git init","git start","git create"],"c":1},{"q":"Qual comando envia commits ao repositório remoto?","a":["git push","git send","git upload","git remote"],"c":0},{"q":"Qual comando cria um branch?","a":["git branch <nome>","git new branch","git create","git fork"],"c":0}]',
8);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Programação Orientada a Objetos', 'POO', 'Questões sobre classes, objetos e pilares da POO.',
'[{"q":"O que é um objeto?","a":["Um tipo de dado","Instância de uma classe","Um atributo","Um método"],"c":1},{"q":"Qual pilar representa reutilização?","a":["Herança","Polimorfismo","Encapsulamento","Abstração"],"c":0},{"q":"Métodos com o mesmo nome e comportamentos diferentes definem:","a":["Herança","Abstração","Polimorfismo","Casting"],"c":2}]',
7);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Segurança da Informação', 'Segurança', 'Quiz introdutório sobre ataques e boas práticas de segurança.',
'[{"q":"O que significa SQL Injection?","a":["Ataque via scripts JS","Inserção maliciosa de comandos SQL","Acesso físico ao servidor","Explorar falhas de rede"],"c":1},{"q":"Senha forte deve ter:","a":["Apenas letras","Apenas números","Mistura de caracteres","08 dígitos fixos"],"c":2},{"q":"HTTPS significa:","a":["Protocolo inseguro","Criptografia SSL/TLS","Servidor offline","Banco de dados"],"c":1}]',
10);

INSERT INTO quiz (title, category, description, questions, popularity) VALUES
('Algoritmos e Estruturas de Dados', 'Algoritmos', 'Questões sobre complexidade, árvores e estruturas fundamentais.',
'[{"q":"Árvore binária tem no máximo quantos filhos por nó?","a":["1","2","3","4"],"c":1},{"q":"Qual estrutura usa FIFO?","a":["Pilha","Árvore","Fila","Heap"],"c":2},{"q":"Complexidade do QuickSort médio:","a":["O(n)","O(log n)","O(n log n)","O(n²)"],"c":2}]',
9);
