from flask import Flask, request, jsonify

app = Flask(__name__)

#Lista de libros (Simulando una base de datos)

books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'read': True},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'read': False}
]

#Obtener todos los libros

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

#Obtener un libro especifico por su id:

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id']== book_id), None)
    if book is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify(book)

#Crear un libro nuevo:

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        return jsonify({'error':'El libro debe tener un titulo'}), 400
    new_book ={
        'id':books [-1] ['id']+ 1 if books else 1,
        'title': request.json['title'],
        'author':request.json.get('author', ""),
        'read': request.json.get('read',False)
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Actualizar un libro existente
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    if not request.json:
        return jsonify({'error': 'La solicitud debe ser JSON'}), 400
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    book['read'] = request.json.get('read', book['read'])
    return jsonify(book)
# Eliminar un libro
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)