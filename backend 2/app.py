from flask import Flask, request, jsonify

app = Flask(__name__)

#Lista de tareas (simulando una base de datos en memoria)

tasks =[
    {'id': 1, 'title': 'Comprar leche', 'description': 'comprar 2 litros de leche', 'done': False},
    {'id': 2, 'title': 'Hacer Ejercicio', 'description': '30 minutos de ejercicio', 'done': False}
]

#obtener todas las tareas

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

#Obtener una tarea especifica por su ID

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    return jsonify(task)

#Crear una nueva tarea

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'error': 'La tarea debe tener un titulo'}), 400
    new_task ={
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

#Actualizar una tarea existente

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id) , None)
    if task is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    if not request.json:
        return jsonify({'error': 'La solicitud debe ser JSON'}), 400
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify(task)

#Eliminar una tarea

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id']!= task_id]
    return jsonify({'result':True})

if __name__=='__main__':
    app.run(debug=True)