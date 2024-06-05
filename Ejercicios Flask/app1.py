#-------------------------------------------------------------------#
#Crea una ruta en flask que responda con un mensaje de bienvenida.  #
#-------------------------------------------------------------------#

from flask import Flask

app = Flask(__name__)

@app.route('/welcome', methods = ['GET'])
def welcome():
    return 'Bienvenido Has acabado el ejercicio'

if __name__ == '__main__':
    app.run(debug=True)