DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS user_answer;
DROP TABLE IF EXISTS multiple_choice_question;
DROP TABLE IF EXISTS quiz;
DROP TABLE IF EXISTS quiz_session;
DROP TABLE IF EXISTS quiz_result;
CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password_hash TEXT NOT NULL UNIQUE);

CREATE TABLE multiple_choice_question ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    proposition TEXT NOT NULL UNIQUE, 
    theme TEXT NOT NULL, 
    difficulty_points INTEGER NOT NULL, 
    alternatives TEXT NOT NULL, 
    correct_option_index INTEGER NOT NULL
);

CREATE TABLE quiz ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL, 
    category TEXT NOT NULL,
    description TEXT NOT NULL, 
    questions TEXT NOT NULL,
    popularity INT,
    created_in TEXT DEFAULT (datetime('now'))
    );

CREATE TABLE quiz_result ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL, 
    quiz_id INTEGER NOT NULL, 
    session_id INTEGER NOT NULL,
    score_achieved INTEGER NOT NULL, 
    time_taken REAL NOT NULL,
    max_possible_score INT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES quiz_session(id) 
    FOREIGN KEY (user_id) REFERENCES user(id), 
    FOREIGN KEY (quiz_id) REFERENCES quiz(id));

CREATE TABLE user_answer( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    selected_option INTEGER NOT NULL,
    is_correct BOOLEAN NOT NULL,
    time_to_response FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id), 
    FOREIGN KEY (quiz_id) REFERENCES quiz(id),
    FOREIGN KEY (question_id) REFERENCES multiple_choice_question(id)
);

CREATE TABLE quiz_session(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    current_question INTEGER NOT NULL,
    score INTEGER NOT NULL,
    times TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (quiz_id) REFERENCES quiz(id)
);

CREATE TRIGGER increment_quiz_popularity
AFTER INSERT ON quiz_session
FOR EACH ROW
BEGIN
    UPDATE quiz 
    SET popularity = popularity + 1 
    WHERE id = NEW.quiz_id;
END;