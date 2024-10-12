# Endpoints
- `/` - root endpoint. returns visual `index.html` to user.
- `/tasklist` - api endpoint. returns list of dictionaries with information about all tasks from database.
- `/taskinfo/<int:id>` - api endpoint, returns information about specified task by its `id`
- `/delete_task/<int:id>` - api enpoint, deletes information about task from database by its `id`
- `/newtask_form` - form ednpoint. returns visual `taskCreation.html` to user.
- `/create_task` - recieves form with `POST` method and saves info from it. form ids:
  - `task_header` type - text
  - `task_description` type - text
  - `task_photo` type - image file
- `/done/<int:id>` - api endpoint that changes specified task's status to True (or in other words marks it as done)
- `/notdone/<int:id>` - api endpoint that changes specified task's status to False (or in other words marks it as not done)
- `/search_task` - api endpoint that gets parametr `query` and based on it finds similar tasks in the database. Returns dictionary with task informations
- `/edittask_form` - returns visual `taskEdit.html` to user
- `/view_task` - returns visual `taskView.html` to user
- `/get_img_url/<int:id>` - api enpoint return url to image for task with specified in url id
### Note: Default status of the task is False (or not done)