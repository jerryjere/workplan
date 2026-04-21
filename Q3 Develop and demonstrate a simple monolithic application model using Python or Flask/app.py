from flask import Flask, request, jsonify

app = Flask(__name__)
students = {}
next_id = 1

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'roll' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    student = {'id': next_id, 'name': data['name'], 'roll': data['roll']}
    students[next_id] = student
    next_id += 1
    return jsonify(student), 201

@app.route('/students/<int:sid>', methods=['DELETE'])
def delete_student(sid):
    if sid not in students:
        return jsonify({'error': 'Student not found'}), 404

    students.pop(sid)
    return jsonify({'msg': 'Deleted'})

if __name__ == '__main__':
    app.run(debug=True)