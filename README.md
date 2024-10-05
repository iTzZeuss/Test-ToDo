# Endpoints
- `/` - root endpoint. returns visual `index.html` to user.
- `/tasklist` - api endpoint. returns list of dictionaries with information about all tasks from database.
- `/taskinfo/<int:id>` - api endpoint, returns information about specified task by its `id`
- `/delete_task/<int:id>` - api enpoint, deletes information about task from database by its `id`
- `/newtask_form` - form ednpoint. returns visual `taskcreation_form.html` to user.
- `/create_task` - recieves form with `POST` method and saves info from it. form ids:
  - `header` type - text
  - `description` type - text
  - `photo` type - image file
 
