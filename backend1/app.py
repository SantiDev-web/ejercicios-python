from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola mundo!'

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola. {nombre}!'

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    if request.method == 'POST':
        datos = request.get_json()
        suma = datos['a'] + datos['b']
        return jsonify({'resultado': suma})
    else:
        return '''
            <form method="post">
                <label for="a">A:</label>
                <input type="text" id="a" name="a"><br>
                <label for="b">B:</label>
                <input type="text" id="b" name="b"><br>
                <input type="submit" value="Sumar">
            </form>
        '''


if __name__ == '__main__':
    app.run(debug=True)