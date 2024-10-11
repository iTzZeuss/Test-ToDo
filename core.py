from flask import Flask, render_template, jsonify, request, redirect, url_for
import os 
import config
import task_manager as task_mgr
import image_manager as image_mgr

app = Flask(__name__)

#TODO: when mobile designs implemented return necessary designs to specified devices. use user agent headers for that.
#Also create edit form endpoints for editing tasks

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
    #FORFRONTEND: this route will return single dictionary which contains information about specific task.
    #Note: include id in request
    #request example for task with id 2: alterapps.xyz/taskinfo/2

    task_mgr.connect_db()
    taskinfo = task_mgr.get_task(id)

    return jsonify(taskinfo)

@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    #FORFRONTEND: this route will delete item specified by the url
    #Note: inclide id in request
    #request example for task with id 2: alterapps.xyz/delete_task/2

    task_mgr.connect_db()

    task_info = task_mgr.get_task(id)
    #delete the photo
    image_mgr.delete_from_cloudinary(task_info["photo_path"])

    #delete other stuff
    task_mgr.delete_task(id)

    return 200

@app.route('/newtask_form')
def return_createform():
    #FORFRONTEND: returns taskCreation.html to user
    return render_template("taskCreation.html")

@app.route('/edittask_form')
def return_editform():
    #FORFRONTEND: returns taskEdit.html to user
    return render_template("taskEdit.html")

@app.route('/view_task')
def return_view():
    #FORFRONTEND: returns taskView.htmll to user
    return render_template("taskView.html")

@app.route("/create_task", methods=["POST"])
def create_task():
    # FORFRONTEND: gets information from form.
    # IDs needed:
    # task_header - text
    # task_description - text
    # task_photo - any photo type (png/jpg)

    header = request.form.get("task_header")
    description = request.form.get("task_description")
    photo = request.files["task_photo"]

    # Uploading the photo to Cloudinary
    uploaded_url, public_id = image_mgr.upload_to_cloudinary(photo)

    if uploaded_url:
        # Saving info into the database with the URL and public_id
        task_mgr.connect_db()
        task_mgr.add_task(header, description, public_id, False)

        # Redirecting
        return redirect(url_for("main_page"))
    else:
        # Handle the error case (e.g., return an error message)
        return "Error uploading photo", 400

@app.route("/done/<int:id>", methods=["POST"])
def mark_as_done(id):
    #FORFRONTEND: this route changes specified task status to True
    task_mgr.connect_db()
    task_mgr.mark_task_done(id)

    return 200

@app.route("/notdone/<int:id>", methods=["POST"])
def mark_as_notdone(id):
    #FORFRONTEND: this route changes specified task status to False
    task_mgr.connect_db()
    task_mgr.mark_task_notdone(id)

    return 200

@app.route("/search_task")
def search_for_task():
    #FORFRONTEND: returns dictionary with information about tasks that have similar words to search query parametr in task parametrs like header and description
    #Parametrs:
    #   string:query
    #Note: it is neccesary parametr

    query = request.args.get('query')  # example: /search?query=flask

    if not query:
        return jsonify({"error": "Missing 'query' parameter"}), 400  # Return 400 Bad Request

    # Continue processing if 'query' is present
    task_mgr.connect_db()
    search_results = task_mgr.search_tasks(query)
    return jsonify(search_results)

@app.route("/get_img_url/<int:id>")
def image_url_by_id(id):
    #FORFRONTEND: returns url to the task's image. specify id in the url

    task_mgr.connect_db()
    task_image_id = task_mgr.get_task(id)["photo_path"]

    return config.CLOUD_RESOURCE_URL_TEMPLATE + task_image_id


if __name__ == '__main__':
    # Just running the app. nothing interesting in here. Mb we will need to setup ssl here
    port = int(os.environ.get('PORT', config.DEFAULT_PORT))
    app.run(host='0.0.0.0', port=port, debug=config.DEBUG)