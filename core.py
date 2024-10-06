from flask import Flask, render_template, jsonify, request, redirect, url_for
import os 
import config
import task_manager as task_mgr
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def main_page():
    #FORFRONTEND: returning index for user
    return render_template("index.html")

@app.route("/tasklist")
def return_tasklist():
    #FORFRONTEND: this route will return list of dictionaries which contains list of all tasks from database.
    #dict keys: id, header, description, photo_path, status (completed or not)
    #example of dict: {"id":"0", "header":"Example Task", "description":"once upon a time", "photo_path":"somepath/img", "status":"completed"}

    #fetching list from database
    task_mgr.connect_db()
    task_list = task_mgr.list_tasks()
    #returning
    return jsonify(task_list)

@app.route('/taskinfo/<int:id>', methods=['GET'])
def return_task_info(id):
    #FORFRONTEDL this route will return single dictionary which contains information about specific task.
    #Note: include id in request
    #request example for task with id 2: alterapps.xyz/taskinfo/2

    task_mgr.connect_db()
    taskinfo = task_mgr.get_task(id)

    return jsonify(taskinfo)

@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    #FORFRONTEND this route will delete item specified by the url
    #Note: inclide id in request
    #request example for task with id 2: alterapps.xyz/delete_task/2

    task_mgr.connect_db()
    task_mgr.delete_task(id)

    return 200

@app.route('/newtask_form')
def return_form():
    #FORFRONTEND returns taskcreation_form.html to user
    return render_template("taskcreation_form.html")

@app.route("/create_task", methods=["POST"])
def create_task():
    #FORFRONTEND gets information from form.
    #IDs needed:
    #task_header - text
    #task_description - text
    #task_photo - any photo type (png/jpg)
    #Saves info to database and redirects back to main page

    header = request.form.get("task_header")
    description = request.form.get("task_description")
    photo = request.files["task_photo"]

    #saving photo with name uuid4 into /static/photos folder
    filename = str(uuid4()) + photo.filename.split('.')[1]
    filepath = os.path.join(config.PHOTOS_FOLDER_PATH, filename)
    photo.save(filepath)

    #saving info into database
    task_mgr.connect_db()
    task_mgr.add_task(header, description, filepath, False)

    #redirecting
    return redirect(url_for("main_page"))

if __name__ == '__main__':
    # Just running the app. nothing interesting in here. Mb we will need to setup ssl here
    port = int(os.environ.get('PORT', config.DEFAULT_PORT))
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)