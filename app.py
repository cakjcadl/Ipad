from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {'id': 1, 'title': '군 복무 공부', 'done': False},
    {'id': 2, 'title': 'Flask 배우기', 'done': False}
]

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(todo)

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = {
        'id': max([t['id'] for t in todos]) + 1 if todos else 1,
        'title': data.get('title', ''),
        'done': False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Not found'}), 404
    data = request.json
    todo['title'] = data.get('title', todo['title'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo)

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return '', 204

@app.route('/')
def hello():
    return jsonify({'message': 'Hello! Flask API is running!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)