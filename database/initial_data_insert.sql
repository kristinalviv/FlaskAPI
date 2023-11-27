--todo update insert statements due to new DDL and for all 5 tables --DONE

--if reformat is needed - press option+command and view if result ok.....

INSERT INTO Movies (title, year_date, description, budget_in_millions)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9),
    ("Casablanca", 1942, "Romance", 1.0),
    ("Avengers: Endgame", 2019, "Action", 858.8),
    ("Night of the Living Dead", 1968, "Horror", 2.5),
    ("The Godfather", 1972, "Crime", 135.6),
    ("Haider", 2014, "Action", 4.2),
    ("Inception", 2010, "Adventure", 293.7),
    ("Evil", 2003, "Horror", 1.3),
    ("Toy Story 4", 2019, "Animation", 434.9),
    ("Air Force One", 1997, "Drama", 138.1),
    ("The Dark Knight", 2008, "Action",535.4),
    ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
    ("The Lion King", 1994, "Animation", 423.6),
    ("Pulp Fiction", 1994, "Crime", 108.8),
    ("Kai Po Che", 2013, "Sport", 6.0),
    ("Beasts of No Nation", 2015, "War", 1.4),
    ("Andadhun", 2018, "Thriller", 2.9),
    ("The Silence of the Lambs", 1991, "Crime", 68.2),
    ("Deadpool", 2016, "Action", 363.6),
    ("Drishyam", 2015, "Mystery", 3.0);



INSERT INTO Actors
(first_name, last_name, birthday)
VALUES
    ("Chaitanya", "Baweja", '1963-01-01'),
    ("Mary", "Cooper", '1966-01-01'),
    ("John", "Wayne", '1983-10-13'),
    ("Thomas", "Stoneman", '1973-11-01'),
    ("Penny", "Hofstadter", '1977-09-12'),
    ("Mitchell", "Marsh", '1976-05-01'),
    ("Wyatt", "Skaggs", '1988-04-28'),
    ("Andre", "Veiga", '2000-11-15'),
    ("Sheldon", "Cooper", '1992-12-09'),
    ("Kimbra", "Masters", '1952-08-04'),
    ("Kat", "Dennings", '1963-07-10'),
    ("Bruce", "Wayne", '1978-09-03'),
    ("Domingo", "Cortes", '1988-11-09'),
    ("Rajesh", "Koothrappali", '2010-12-01'),
    ("Ben", "Glocker", '2002-11-21'),
    ("Mahinder", "Dhoni", '1997-09-10'),
    ("Akbar", "Khan", '1960-04-09'),
    ("Howard", "Wolowitz", '1945-09-11'),
    ("Pinkie", "Petit", '1978-08-05'),
    ("Gurkaran", "Singh", '1997-07-09'),
    ("Amy", "Farah Fowler", '1987-05-23'),
    ("Marlon", "Crafford", '1999-11-30');



INSERT INTO Ratings
(score, movie_id, user_id, review, create_date)
VALUES
    (6.4, 17, 5, 'much liked', '2002-11-21'),
    (5.6, 19, 1, 'Just awful...', '2010-12-01'), (6.3, 22, 14, 'Worth it', '2009-11-03'),
    (5.1, 21, 17, 'Wow:))' '2017-05-13'), (5.0, 5, 5, 'nice for view at the late evening:)', '2003-05-22'),
    (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4), (8.5, 24, 12, 'recommended for sure'),
    (9.9, 14, 9, 'amazing for kids!!!!', '2020-05-11'), (8.7, 26, 14), (9.9, 6, 10),
    (5.1, 30, 6, 'Incredible!!', '2003-05-22'), (5.4, 18, 16, 'You would never guess the end...', '2010-09-28'),
    (6.2, 6, 20), (7.3, 21, 19), (8.1, 17, 18, 'for one time watch'), (5.0, 7, 2),
    (9.8, 23, 3), (8.0, 22, 9, 'definitely recommend', '2022-09-10'), (8.5, 11, 13, 'My top list first!!)', '2023-05-03'),
    (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19, 'Most romantic film ever', '2019-12-02'), (5.2, 18, 15), (9.7, 13, 3),
    (5.8, 18, 8), (5.8, 30, 15, 'You should see it'), (9.5, 30, 20, 'I cried for whole film', '2010-12-01'),
    (8.4, 21, 18), (6.2, 23, 16, 'Short story long(', '2010-12-01'), (7.0, 10, 18),
    (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22, 'Just awful...', '2010-12-01'), (9.9, 15, 13),
    (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17, 'The best ever actors...', '2010-12-01'),
    (6.4, 5, 10), (8.1, 5, 21, 'Loved the songs', '2010-12-01'), (5.7, 22, 1), (6.3, 28, 4),
    (9.8, 13, 1);


INSERT INTO Users
(user_name, user_login, user_pass)
VALUES
    ("Sonya", "son123", '1111'),
    ("Oleksii", "ol123_n", '2222'),
    ("Yurii", "yur_098765", 'pass_1'),
    ("Andrew", "123andrew", 'pass_2'),
    ("Olha", "0000_olha", 'new_p_s'),
    ("Vitalii", "vit_vit", 'top_secret'),
    ("Denys", "denya555", 'super_secret'),
    ("Ihor", "@Ihor", '67890Ihor'),
    ("Sasha", "sanya", 'sanya___1'),
    ("Nataliia", "natalii", 'natalii_N'),
    ("Nazar", "nazN", 'naz_12345'),
    ("Andriy", "andriy_Y", '1234567_an'),
    ("Vita", "vita_", 'vita_22'),
    ("Mykola", "admin", 'Mykola_12'),
    ("Viktor", "tourist", 'Vik_tor_333'),
    ("Anna", "anna_A", '999_anna'),
    ("Ihor", "@ihor", 'ihor_pass'),
    ("Ivan", "ivan_us", '098765#ivan'),
    ("Lev", "levV", 'lev_123_pass'),
    ("Nazar", "nazar_23", 'nazar_23!');


INSERT INTO MovieCharacter
(movie_id, actor_id, character_name)
VALUES
    (17, 8, 'Jerry'),
    (1, 10, 'Cinderella'),
    (30, 4, 'Joe'),
    (3, 11, 'Nicolas'),
    (5, 5, 'Mask'),
    (7, 5, 'Vinni'),
    (9, 5, 'Samantha'),
    (13, 7, 'Tom'),
    (14, 1, 'Anthony'),
    (4, 21, 'Rob'),
    (22, 9, 'William'),
    (25, 12, 'Marry'),
    (16, 15, 'Oliver'),
    (19, 3, 'Homer'),
    (28, 14, 'Tom'),
    (23, 16, 'Rachel'),
    (12, 18, 'Vinni'),
    (6, 2, 'Anthonina'),
    (11, 22, 'Ros');