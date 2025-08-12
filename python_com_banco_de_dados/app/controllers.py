from flask import request, jsonify
from models.user import User
from flask_login import login_user, current_user, logout_user
from app import db

class UserController:

  def login(self):
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("password")

    if username and password:
      user = User.query.filter_by(username = username).first()    

      if user and user.password == password:
        login_user(user)
        return {"message": "Autenticação realizada com sucesso"}

    return {"message": "Credenciais invalidas"}, 400
  
  def logout(self):
    logout_user()
    return jsonify({"message": "Usuario deslogado"})
  
  def create_user(self):
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("password")

    if username and password:
      user = User.query.filter_by(username = username).first()

      if user:
        return jsonify({"message": "Usuário ja cadastrado"})
      
      user = User(username = username, password = password)
      db.session.add(user)
      db.session.commit()
      return jsonify({"message": "Usuário cadastrado com sucesso"})
      
    return {"message": "Dados invalidos"}, 400
  
  def get_user(self, user_id):
    user = User.query.get(user_id)

    if user:
      return jsonify({"id": user.id, "username": user.username})
    
    return jsonify({"message": "Usuario não encontrado"}), 404
  
  def update_user(self, user_id):
    user = User.query.get(user_id)
    data = request.get_json()
    password = data.get("password")

    if not user:
      return jsonify({"message": "Usuario não encontrado"}), 404

    if (user.id == current_user.id or current_user.username == "admin") and password:
      user.password = password
      db.session.commit()
      return jsonify({"message": f"Usuario {user.username} atualizado com sucesso"})
    else:
      return jsonify({"message": "Sem permissão para alterar"}), 401
  
  def delete_user(self, user_id):
    user = User.query.get(user_id)

    if not user:
      return jsonify({"message": "Usuario não encontrado"}), 404

    if current_user.username == "admin": #usuario nao pode deletar ele mesmo, da erro
      db.session.delete(user)
      db.session.commit()
      return jsonify({"message": f"Usuario delete com sucesso"})
    else:
      return jsonify({"message": "Sem permissão para deletar"}), 401