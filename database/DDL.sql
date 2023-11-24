--create db, table
-- todo format file

CREATE DATABASE movies_db;

create table if not exists Movies (movie_id id AUTO_INCREMENT PRIMARY KEY, title varchar(255) NOT NULL,
    year_date YEAR(4) NOT NULL, description varchar(255), budget_in_millions int NOT NULL, PRIMARY KEY (movie_id));
    --changed genre to genre_id

create table if not exists Actors (actor_id INT AUTO_INCREMENT PRIMARY KEY,
    firstname varchar(255) NOT NULL, lastname varchar(255) NOT NULL, birthday date NOT NULL, PRIMARY KEY (actor_id));
    --changed added birthday

create table if not exists Users (user_id int NOT NULL, user_name varchar(255) NOT NULL,
    user_login varchar(255) NOT NULL, user_pass varchar(255) NOT NULL, PRIMARY KEY (user_id));

create table if not exists Ratings (user_id int NOT NULL, movie_id int NOT NULL,
    score int NOT NULL, review varchar(1024), create_date timestamp --todo default now() in sql;
    FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY(user_id) REFERENCES Users(user_id), PRIMARY KEY (user_id, movie_id));

create table if not exists MovieCharacter (movie_id int NOT NULL, actor_id int NOT NULL,
    character_name varchar(255) NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY(actor_id) REFERENCES Actors(actor_id), PRIMARY KEY (actor_id, movie_id));




--    create_genre_table = "create table if not exists Genres ( genre_id  int NOT NULL, movie_id int NOT NULL. "
--        + "genre_title varchar(255) NOT NULL, PRIMARY KEY (genre_id))"

--
--create_director_table = "create table if not exists Directors (director_id int NOT NULL, name varchar(255) NOT NULL, "
--    + "surname varchar(255) NOT NULL, birthday datetime NOT NULL, country varchar(255) NOT NULL, city varchar(255) NOT NULL,"
--    + "PRIMARY KEY (director_id)), FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),"
--










----create db, table
--
--CREATE DATABASE movies_db;
--
----#what quotes are needed?
--create_movie_table = """create table if not exists Movie ( movie_id int NOT NULL, name varchar(255) NOT NULL,
--    year_date YEAR(4) NOT NULL, genre varchar(255) NOT NULL, rate int NOT NULL, actor_id int NOT NULL,
--    PRIMARY KEY (movie_id))"""
--
--create_director_table = "create table if not exists Director (director_id int NOT NULL, name varchar(255) NOT NULL, "
--    + "surname varchar(255) NOT NULL, birthday datetime NOT NULL, country varchar(255) NOT NULL, city varchar(255) NOT NULL,"
--    + "PRIMARY KEY (director_id)), FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),"
--
--create_actor_table = "create table if not exists Actor (actor_id int NOT NULL, name varchar(255) NOT NULL, "
--    + "lastname varchar(255) NOT NULL, email varchar(255) NOT NULL, login varchar(255) NOT NULL, "
--    + "password varchar(255) NOT NULL, active int NOT NULL, PRIMARY KEY (actor_id)), "
--    + "FOREIGN KEY(movie_id) REFERENCES Movie(movie_id),"
--
--create_user_table = "create table if not exists Users (user_id int NOT NULL, user_name varchar(255) NOT NULL,"
--    + "user_surname varchar(255) NOT NULL, user_email varchar(255) NOT NULL, user_login varchar(255) NOT NULL, "
--    + "user_pass varchar(255) NOT NULL, active int NOT NUL, birthday datetime NOT NULL, "
--    + "FOREIGN KEY(movie_id) REFERENCES Movie(movie_id), PRIMARY KEY (user_id))"
--
--create_genre_table = "create table if not exists Genres ( genre_id  int NOT NULL, movie_id int NOT NULL. "
--    + "genre_title varchar(255) NOT NULL, PRIMARY KEY (genre_id))"
--
--create_rates_table = "create table if not exists Ratings (rating int NOT NULL, movie_id int NOT NULL, "
--    + "actor_id int NOT NULL, FOREIGN KEY(movie_id) REFERENCES Movie(movie_id), "
--    + "FOREIGN KEY(actor_id) REFERENCES Actor(actor_id), PRIMARY KEY (rate_id))"