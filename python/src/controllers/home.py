from flask import Blueprint, jsonify
from src.task import long_running_task

from src.extensions import celery
from celery.result import AsyncResult
# from celery.contrib.abortable import AbortableAsyncResult
# from celery.task.control import revoke

home = Blueprint("home", __name__)

@home.route("/")
def index():
    """Add a new task and start running it after 10 seconds."""
    return (
        jsonify(
            {"Hello": "Full metal"}
        ),
        202,
    )
    

@home.route("/task", methods=['GET'])
def longtask():
    task = long_running_task.apply_async()
    return (
        jsonify({'message': 'Task has been scheduled', 'task_id':task.id}), 
        202,
    )
    
@home.route("/task/status/<task_id>", methods=['GET'])
def taskstatus(task_id):
    if task_id:
        task = AsyncResult(task_id)

        if task.status == "REVOKED":
            response = {
                'state': task.state,
                'task_id': task.task_id,
                "message": "Task has been terminated"
            }
        
        elif task.state == 'PENDING':
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
        
        elif task.state != 'ABORTED':
            response = {
                'state': task.state
            }
            
        else:
            # something went wrong in the background job
            response = {
                'state': task.state,
                'progresStatus': task.info.get('progresStatus', 0),
                'status': task.status,
                'status_info': str(task.info),  # this is the exception raised
            }
        return jsonify(response)
    
    return jsonify({
        "status": "Error",
		"message": "Task id is not provided."
    })
    
@home.route("/task/terminate/<task_id>", methods=['GET'])
def taskterminate(task_id):
    if task_id:
        try:
            celery.control.revoke(task_id,terminate=True,signal='SIGUSR1')
            # abort_task.abort()
            
            # aborted_task = AbortableAsyncResult(task_id).abort()
            
            return jsonify({
                "status": "Success",
				"message": "Task successfully terminated."
            })
            
        except Exception as e:
            return jsonify({
                "status": "Error",
                "message": "Task Id does not exists."
            })
    
    return jsonify({
        "status": "Error",
		"message": "Task id is not provided."
    })
    
@home.route("/task/pause/<task_id>", methods=['GET'])
def taskpause(task_id):
    if task_id:
        try:
            celery.Task.update_state(self=celery, task_id=task_id, state='PAUSING')
            return jsonify({
                "status": "Success",
				"message": "Task successfully paused."
            })
            
        except Exception as e:
            return jsonify({
                "status": "Error",
                "error": e,
                "message": "Some error occured"
            })
    
    return jsonify({
        "status": "Error",
		"message": "Task id is not provided."
    })
    
@home.route("/task/resume/<task_id>", methods=['GET'])
def taskresume(task_id):
    if task_id:
        try:
            celery.Task.update_state(self=celery, task_id=task_id, state='RESUME')
            return jsonify({
                "status": "Success",
				"message": "Task successfully resumed."
            })
            
        except Exception as e:
            return jsonify({
                "status": "Error",
                "message": "Task Id does not exists."
            })
    
    return jsonify({
        "status": "Error",
		"message": "Task id is not provided."
    })