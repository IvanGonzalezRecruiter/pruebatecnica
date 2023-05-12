from flask import Flask, request, jsonify
from flask_cors import CORS
from database_model import createDatabaseFunction
from database_querys import insertGenerosFunction, insertFilmFunction, viewGenero, viewFilmsFunction, insertImagesFilmFunction, viewImagesFilmsFunction, deleteFilmFunction, viewOneFilmFunction
app = Flask(__name__)
app.secret_key = 'f3167129525f2a20696b7de80ff37401c963b55871119ed7ddec510809d5fa5530fa40bdf5041484a52a3932a4cad6e542e3c5199ef4cca9aa7c7e52f69c3e76'
CORS(app)

createDatabaseFunction()

@app.route('/', methods=['GET'])
def Inicio():
    if request.method == 'GET':
        return "hola"

@app.route('/create-genero', methods=['POST'])
def createGenero():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        genero = request.json
        insertGenerosFunction(genero["genero"])
        return "genero insertado"
    else:
        return 'Content-Type not supported! make sure that you send content type: application/json header in your post'
    
@app.route('/view-genero', methods=['GET'])
def viewGeneros():
    generos = viewGenero()
    return generos
    
@app.route('/create-film', methods=['POST'])
def createFilm():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        film = request.json
        nombre = film["name"]
        descripcion = film["description"]
        genero = film["genere"]
        year = film["year"]
        insertFilmFunction(nombre, descripcion, genero, year)
        return "film insertado"
    else:
        return 'Content-Type not supported! make sure that you send content type: application/json header in your post'

@app.route('/view-films', methods=['GET'])
def viewFilms():
    films = viewFilmsFunction()
    return films

@app.route('/create-image', methods=['POST'])
def createImagen():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        imagen = request.json
        nombrePelicula = imagen["film_name"]
        yearPelicula = imagen["film_year"]
        url = imagen["url_image"]
        name = imagen["name"]
        insertImagesFilmFunction(nombrePelicula, yearPelicula, url, name)
        return "imagen insertada"
    else:
        return 'Content-Type not supported! make sure that you send content type: application/json header in your post'

@app.route('/view-images-films', methods=['GET'])
def viewAllImagesFilms():
    images = viewImagesFilmsFunction()
    return images

@app.route('/delete-film', methods=['DELETE'])
def deleteFilm():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        film = request.json
        nombrePelicula = film["name"]
        yearPelicula = film["year"]
        deleteFilmFunction(nombrePelicula, yearPelicula)
        return "pelicula eliminada"
    else:
        return 'Content-Type not supported! make sure that you send content type: application/json header in your post'

@app.route('/get-film/<filmname>/<year>', methods=['GET'])
def getOneFilm(filmname, year):
    film = viewOneFilmFunction(filmname, year)
    return film
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)