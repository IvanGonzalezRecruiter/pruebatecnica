import psycopg2

def createDatabaseFunction():
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    cur.execute("""
                    CREATE TABLE IF NOT EXISTS genere (
                        name TEXT PRIMARY KEY
                    );
                    CREATE TABLE IF NOT EXISTS films (
                        name TEXT NOT NULL,
                        description TEXT,
                        genere TEXT NOT NULL,
                        year INT NOT NULL,
                        PRIMARY KEY (name, year),
                        FOREIGN KEY (genere) REFERENCES genere (name) 
                    );
                    CREATE TABLE IF NOT EXISTS images_films (
                        film_name TEXT,
                        film_year INT,
                        url_image TEXT UNIQUE,
                        name TEXT NOT NULL,
                        PRIMARY KEY(film_name, film_year, url_image),
                        FOREIGN KEY (film_name, film_year) REFERENCES films (name, year) ON DELETE CASCADE ON UPDATE CASCADE
                    );
                """)
    conn.commit()
    cur.close()
    conn.close()