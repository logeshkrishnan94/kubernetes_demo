import celery.states as states
from flask import Flask
from flask import url_for, jsonify
from worker import app

dev_mode = True
flask_app = Flask(__name__)

@flask_app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = app.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@flask_app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = app.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@flask_app.route('/health_check')
def health_check() -> str:
        return jsonify("OKAY")


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port='5001')
