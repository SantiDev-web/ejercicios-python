#------------------------------------------------------------------------------------#
#           Crea una ruta que maneje parámetros de consulta en la URL.               #
#------------------------------------------------------------------------------------#

from flask import Flask, request

app = Flask(__name__)

@app.route('/query', methods =['GET'])
def query():
    name = request.args.get('name')
    return f'Query: {name}'

if __name__=='__main__':
    app.run(debug=True, port=5000)
    