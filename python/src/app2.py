from flask import Flask, request, jsonify
from flask_celery import make_celery
from celery.result import AsyncResult
from celery import Celery

from tasks import process_task

flask_app  = Flask(__name__)
# flask_app.config.update(
#     BROKER_URL='redis://127.0.0.1:6379',
#     CELERY_RESULT_BACKEND='redis://127.0.0.1:6379'
# )
# celery = make_celery(flask_app )

# Celery configuration
flask_app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
flask_app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

# Initialize Celery
celery = Celery(flask_app.name, backend=flask_app.config['CELERY_RESULT_BACKEND'], broker=flask_app.config['CELERY_BROKER_URL'])
# celery.conf.update(flask_app.config)

@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    progress = 0
    
    while progress < 100:
        time.sleep(0.05)
        progress += 1;
        self.update_state(state='PROGRESS',
                          meta={'progresStatus': progress})
    
    
    return {'status': 'Task completed!', 'progresStatus': progress}
    
@flask_app.route('/status/<task_id>')
def taskstatus(task_id):
    
    if task_id:
        task = AsyncResult(task_id)
        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'task_id': task.task_id,
                'status': task.status
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'progresStatus': task.info.get('progresStatus', 0),
                'status': task.info.get('status', '')
            }
            if 'result' in task.info:
                response['result'] = task.info['result']
        else:
            # something went wrong in the background job
            response = {
                'state': task.state,
                'progresStatus': task.info.get('progresStatus', 0),
                'status': task.info.get('status', ''),
                'status_info': str(task.info),  # this is the exception raised
            }
        return jsonify(response)
    
    return jsonify({
        "status": "Error",
		"message": "Task id is not provided."
    })

@flask_app.route('/longtask', methods=['GET'])
def longtask():
    task = long_task.apply_async()
    return jsonify({'task_id':task.id})
                                                  

if __name__ == "__main__":
    flask_app.run(debug=True)