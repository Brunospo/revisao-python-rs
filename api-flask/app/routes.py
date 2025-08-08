from .controllers import TaskController, AboutController

def register_routes(app):
    tasks = TaskController()
    about = AboutController()

    @app.route('/tasks', methods = ["POST"])
    def create_task():
        return tasks.create_task()
    
    @app.route('/tasks', methods = ["GET"])
    def get_all_tasks():
        return tasks.get_all_tasks()
    
    @app.route('/tasks/<int:task_id>', methods = ["GET"])
    def get_task(task_id):
        return tasks.get_task(task_id)
    
    @app.route('/tasks/<int:task_id>', methods = ["PUT"])
    def update_task(task_id):
        return tasks.update_task(task_id)
    
    @app.route('/tasks/<int:task_id>', methods = ["DELETE"])
    def delete_task(task_id):
        return tasks.delete_task(task_id)

    @app.route('/about')
    def sobre():
        return about.get()