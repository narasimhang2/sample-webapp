from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to simulate a database for your tasks
todos = [{"id": 1, "task": "Learn how to build a web app"}, {"id": 2, "task": "Build my first sample app!"}]

@app.route('/')
def index():
    # Renders the HTML page and passes the todos list to it
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    # Captures the text input from the HTML form
    task_content = request.form.get('task')
    if task_content:
        new_id = len(todos) + 1
        todos.append({"id": new_id, "task": task_content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Runs the application locally on http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000)
