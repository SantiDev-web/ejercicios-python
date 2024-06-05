#------------------------------------------------------------------------------------#
#               Crea una ruta que devuelva datos en formato JSON                     #
#------------------------------------------------------------------------------------#

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods = ['GET'])
def get_data():
    data={
        'items':['coches', 'barcos', 'aviones']
    }
    return jsonify(data)

if __name__ =='__main__':
    app.run(debug=True)
