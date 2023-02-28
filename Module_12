CREATE DATABASE whatabook;


CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'R45fhIps45';


GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';


CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


    

INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');


    

INSERT INTO book(book_name, author, details)
    VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Two Towers', 'J.R.Tolkien', "The second part of The Lord of The Rings");

INSERT INTO book(book_name, author)
    VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');

INSERT INTO book(book_name, author)
    VALUES('Dune: Deluxe Edition', 'Frank Herbert');

INSERT INTO book(book_name, author)
    VALUES("Charlotee's Web", 'E.B. White');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');


    

INSERT INTO user(first_name, last_name) 
    VALUES('Thorin', 'Oakenshield');

INSERT INTO user(first_name, last_name)
    VALUES('Bilbo', 'Baggins');

INSERT INTO user(first_name, last_name)
    VALUES('Frodo', 'Baggins');



INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Thorin'), 
        (SELECT book_id FROM book WHERE book_name = 'The Hobbit or There and Back Again')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bilbo'),
        (SELECT book_id FROM book WHERE book_name = 'The Fellowship of the Ring')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Frodo'),
        (SELECT book_id FROM book WHERE book_name = 'The Return of the King')
    );
