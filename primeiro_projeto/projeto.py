tarefas = []

def menu():
  while True:
    print("\n Menu gerenciador de lista de tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
      nome_tarefa = input("Digite o nome da tarefa: ")
      adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
      visualizar_tarefa(tarefas)

    elif escolha == "3":
      visualizar_tarefa(tarefas)
      indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
      if indice_tarefa < 1 or indice_tarefa > len(tarefas):
        print('Tarefa não encontrada')
        continue

      novo_nome = input("Digite o novo nome da tarefa: ")
      atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
      visualizar_tarefa(tarefas)
      indice_tarefa = int(input("Digite o número da tarefa que deseja completar: "))
      if indice_tarefa < 1 or indice_tarefa > len(tarefas):
        print('Tarefa não encontrada')
        continue

      completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
      deletar_tarefas_completadas(tarefas)
      visualizar_tarefa(tarefas)

    elif escolha == "6":
      break

def adicionar_tarefa(tarefas, nome_tarefa):
  tarefas.append({"Tarefa": nome_tarefa, "Completada": False})
  print(f"Tarefa {nome_tarefa} adicionada com sucesso!")
  return

def visualizar_tarefa(tarefas):
  for indice, tarefa in enumerate(tarefas):
    check = "✓" if tarefa["Completada"] else " "
    nome_tarefa = tarefa["Tarefa"]
    print(f"{indice + 1}. [{check}] {nome_tarefa}")
  return
  
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
  indice_ajustado = indice_tarefa - 1
  tarefas[indice_ajustado]['Tarefa'] = novo_nome

  print(f'Tarefa {indice_tarefa} atualizada para {novo_nome}')
  return

def completar_tarefa(tarefas, indice_tarefa):
  indice_ajustado = indice_tarefa - 1
  tarefas[indice_ajustado]["Completada"] = True

  print(f'Tarefa {indice_tarefa} completa')
  return

def deletar_tarefas_completadas(tarefas):
  tarefas[:] = [t for t in tarefas if not t["Completada"]]
  print("Tarefas completadas foram deletadas")
  return
menu()