import psycopg2

def insertGenerosFunction(nombreGenero):
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = """INSERT INTO genere (name) VALUES (%s);"""
    cur.execute(sql, (nombreGenero,))
    conn.commit()
    cur.close()
    conn.close()

def viewGenero():
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = """SELECT * FROM genere;"""
    cur.execute(sql)
    generos = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return generos

def insertFilmFunction(name, description, genere, year):
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""INSERT INTO films (name, description, genere, year) VALUES (%s, %s, %s, %s)""")
    data = (name, description, genere, year)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()    

def viewFilmsFunction():
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""SELECT f.*, if.url_image, if.name AS image_name FROM images_films if RIGHT JOIN films f ON f.name=if.film_name AND f.year=if.film_year ORDER BY f.name, f.year;""")
    cur.execute(sql)
    films = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return films

def insertImagesFilmFunction(nombrePelicula, yearPelicula, url, name):
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""INSERT INTO images_films (film_name, film_year, url_image, name) VALUES (%s, %s, %s, %s)""")
    data = (nombrePelicula, yearPelicula, url, name)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

def viewImagesFilmsFunction():
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""SELECT * FROM images_films""")
    cur.execute(sql)
    imagesFilms = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return imagesFilms

def deleteFilmFunction(nombreFilm, yearFilm):
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""DELETE FROM films WHERE name=%s AND year=%s""")
    data = (nombreFilm, yearFilm)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()

def viewOneFilmFunction(name, year):
    conn = psycopg2.connect(database = "prueba_tecnica_ivan", 
                        user = "ivan", 
                        host= 'localhost',
                        password = "123456789",
                        port = 5432)
    cur = conn.cursor()
    sql = ("""SELECT f.*, if.url_image, if.name AS image_name FROM images_films if RIGHT JOIN films f ON f.name=if.film_name AND f.year=if.film_year WHERE f.name=%s AND f.year=%s;""")
    data = (name, year)
    cur.execute(sql, data)
    film = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return film
