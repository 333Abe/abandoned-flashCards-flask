DROP TABLE IF EXISTS cards;

CREATE TABLE cards (
    id INT PRIMARY KEY,
    question VARCHAR(300) NOT NULL,
    answer VARCHAR(300) NOT NULL,
    prev_asked_date DATETIME DEFAULT NULL,
    prev_response BOOLEAN NOT NULL DEFAULT FALSE,
    topic VARCHAR(50) NOT NULL,
    subtopic VARCHAR(50) NOT NULL
)
