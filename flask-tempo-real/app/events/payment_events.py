from app.extensions import socketio

@socketio.on("connect")
def handle_connect():
  print("Client conected to server")

@socketio.on("disconnect")
def handle_disconnect():
  print("Client has desconected to the server")

def notify_payment_confirmed(payment_id):
  socketio.emit(f"payment_confirmed_{payment_id}")

