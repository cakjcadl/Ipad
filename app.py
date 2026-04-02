from flask import Flask, request, jsonify

app = Flask(__name__)

# 임시 할일 저장소 (메모리)
todos = [
    {'id': 1, 'title': '군 복무 공부', 'done': False},
    {'id': 2, 'title': 'Flask 배우기', 'done': False}
]

# GET: 모든 할일 조회
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET: 특정 할일 조회
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(todo)

# POST: 새 할일 생성
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

# PUT: 할일 수정
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({'error': 'Not found'}), 404
    
    data = request.json
    todo['title'] = data.get('title', todo['title'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo)

# DELETE: 할일 삭제
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return '', 204

# 루트 경로
@app.route('/')
def hello():
    return jsonify({'message': 'Hello! Flask API is running!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
