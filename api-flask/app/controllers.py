from flask import request, jsonify
from models.task import Task

class TaskController:

  def __init__(self):
    self.tasks = []
    self.next_id = 1

  def create_task(self):
    data = request.get_json()
    
    title = data.get("title")
    description = data.get("description")

    if not title or not description:
      return {"error": "Título e descrição são obrigatórios"}, 400
    
    task = Task(self.next_id, title, description)

    self.tasks.append(task)

    self.next_id += 1

    return jsonify({"message": "Nova tarefa criada com sucesso", "id": task.id}), 201
  
  def get_all_tasks(self):
    return jsonify({"tasks": [task.to_dict() for task in self.tasks], "total_tasks": len(self.tasks)}), 200
  
  def get_task(self, task_id):
    for task in self.tasks:
      if task.id == task_id:
        return jsonify({"task": task.to_dict()}), 200
    return {"error": "Tarefa não encontrada"}, 404
  
  def update_task(self, task_id):
    for task in self.tasks:
      if task.id == task_id:
        data = request.get_json()

        task.title = data.get("title")
        task.description = data.get("description")
        task.completed = data.get("completed")

        return jsonify({"message": "Tarefa atualizada com sucesso"}), 200
    return {"error": "Tarefa não encontrada"}, 404
  
  def delete_task(self, task_id):
    for task in self.tasks:
      if task.id == task_id:
        self.tasks.remove(task)

        return jsonify({"message": "Tarefa apagada com sucesso"}), 200
    return {"error": "Tarefa não encontrada"}, 404

class AboutController:
  def get(self):
    return "Página sobre"