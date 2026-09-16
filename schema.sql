DROP TABLE IF EXISTS books;

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    rating INTEGER CHECK (rating IS NULL OR (rating >= 0 AND rating <= 10)),
    review TEXT
);

INSERT INTO books (title, author, rating, review) VALUES
    ('O Hobbit', 'J. R. R. Tolkien', 9, 'Uma aventura clássica.'),
    ('1984', 'George Orwell', 8, 'Distopia marcante.'),
    ('Dom Casmurro', 'Machado de Assis', 9, 'Clássico brasileiro.');
