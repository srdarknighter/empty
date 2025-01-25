from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the JSON data
with open('students.json', 'r') as file:
    students = json.load(file)

@app.route('/api')
def get_marks():
    names = request.args.getlist('name')
    result = {name: students.get(name, "Not found") for name in names}
    return jsonify(result)

if __name__ == '__main__':
    app.run()
