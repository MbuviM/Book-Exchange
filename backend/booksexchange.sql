CREATE DATABASE bookexchange;

USE bookexchange;

-- Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    profile_pic VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Books table
CREATE TABLE Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    image VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Exchange table
CREATE TABLE Exchange(
    book_id INT NOT NULL,
    requester_id INT NOT NULL,
    owner_id INT NOT NULL,
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY(book_id) REFERENCES Books(book_id),
    FOREIGN KEY(requester_id ) REFERENCES Users(user_id),
    FOREIGN KEY(owner_id ) REFERENCES Users(user_id),
    status VARCHAR(255) NOT NULL,
    requested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Reviews table
CREATE TABLE Reviews(
    reviewer_id INT NOT NULL,
    reviewee_id INT NOT NULL,
    exchange_id INT NOT NULL,
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    review TEXT NOT NULL,
    rating INT NOT NULL,
    FOREIGN KEY(reviewer_id) REFERENCES Users(user_id),
    FOREIGN KEY(reviewee_id) REFERENCES Users(user_id),
    FOREIGN KEY(exchange_id) REFERENCES Exchange(request_id),
    comments TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



