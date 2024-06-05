#------------------------------------------------------------------------------------#
#Crea una ruta que reciba un parámetro en la URL y devuelva un saludo personalizado  #
#------------------------------------------------------------------------------------#

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>', methods=['GET'])
def saymyName(name):
    return f'Hola, {name}, has acabado el ejercicio!'

if __name__ == '__main__':
    app.run(debug=True)