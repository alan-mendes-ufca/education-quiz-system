DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS multiple_choice_question;
DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS quiz_result;

CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL UNIQUE);

CREATE TABLE multiple_choice_question ( id INTEGER PRIMARY KEY AUTOINCREMENT, proposition TEXT NOT NULL UNIQUE, theme TEXT NOT NULL, difficulty_points INTEGER NOT NULL, options json NOT NULL, correct_option_index INTEGER NOT NULL);

CREATE TABLE quiz ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, questions json NOT NULL);

CREATE TABLE quiz_result ( id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, quiz_id INTEGER NOT NULL, score_achieved INTEGER NOT NULL, time_taken REAL NOT NULL, responses_history json NOT NULL, FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (quiz_id) REFERENCES quiz(id));

CREATE TABLE user_answer( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    quiz_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    is_correct BOOLEAN NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quiz(id),
    FOREIGN KEY (question_id) REFERENCES multiple_choice_question(id)
);
