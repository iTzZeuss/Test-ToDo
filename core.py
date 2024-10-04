from flask import Flask, render_template, jsonify
import os 
import config
import task_manager as task_mgr

app = Flask(__name__)

@app.route('/')
def main_page():
    #FORFRONTEND: returning index for user
    return render_template("index.html")

@app.route("/tasklist")
def return_tasklist():
    #FORFRONTEND: this endpoint will return list of dictionaries which contains list of all tasks from database.
    #dict keys: id, header, description, photo_path, status (completed or not)
    #example of dict: {"id":"0", "header":"Example Task", "description":"once upon a time", "photo_path":"somepath/img", "status":"completed"}

    #fetching list from database
    task_list = task_mgr.list_tasks()
    #returning
    return jsonify(task_list)

@app.route('/taskinfo/<int:id>', methods=['GET'])
def return_task_info(id):
    #FORFRONTEDL this enpoint will return single dictionary which contains information about specific task.
    #Note: include id in request
    #request example for task with id 2: alterapps.xyz/taskinfo/2

    taskinfo = task_mgr.get_task(id)
    return jsonify(taskinfo)

if __name__ == '__main__':
    # Just running the app. nothing interesting in here. Mb we will need to setup ssl here
    port = int(os.environ.get('PORT', config.DEFAULT_PORT))
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)