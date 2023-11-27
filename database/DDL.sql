create DATABASE movies_db;
CREATE TABLE if not exists Movies
(
  movie_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  year_date YEAR(4) NOT NULL,
  description VARCHAR(255),
  budget_in_millions int NOT NULL
)
;
CREATE TABLE if not exists Actors
(
  actor_id INT AUTO_INCREMENT PRIMARY KEY,
  firstname VARCHAR(255) NOT NULL,
  lastname VARCHAR(255) NOT NULL,
  birthday date NOT NULL,
  PRIMARY KEY(actor_id)
)
;
CREATE TABLE if not exists Users
(
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(255) NOT NULL,
  user_login VARCHAR(255) NOT NULL,
  user_pass VARCHAR(255) NOT NULL
)
;
CREATE TABLE if not exists Ratings
(
  user_id int NOT NULL,
  movie_id int NOT NULL,
  score int NOT NULL,
  review VARCHAR(1024),
  create_date DATE DEFAULT GETDATE(),
  FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id),
  FOREIGN KEY(user_id) REFERENCES USERS(user_id),
  PRIMARY KEY(user_id, movie_id)
)
;
CREATE TABLE if not exists MovieCharacter
(
  movie_id int NOT NULL,
  actor_id int NOT NULL,
  character_name VARCHAR(255) NOT NULL,
  FOREIGN KEY(movie_id) REFERENCES MOVIE(movie_id),
  FOREIGN KEY(actor_id) REFERENCES ACTORS(actor_id),
  PRIMARY KEY(actor_id, movie_id)
)
;