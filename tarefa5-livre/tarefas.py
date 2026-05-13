
#Gerenciamento de Tarefas:

tarefas = []

def exibir_menu():
   print("\n=== GERENCIADOR DE TAREFAS ===")
   print("1 - Adicionar tarefa")
   print("2 - Listar tarefas")
   print("3 - Concluir tarefas")
   print("4 - Remover tarefas")
   print("5 - Buscar tarefa")
   print("0 - SAIR ")

def adicionar_tarefa(titulo, prioridade):
    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print ("\n === LISTA DE TAREFAS ===")
    for i, t in enumerate(tarefas):
        if t["concluida"]:
            status = "Concluida"
        else:
            status = "Pendente"
        print(f"{i+1}. [{status}] | {t['titulo']} | Prioridade: {t['prioridade']}")


def concluit_tarefa(indice):
    if indice <0 or indice >= len(tarefas):
        print("Tarefa não encontrada")
        return False
    tarefas[indice]["concluida"]  = True
    print(f"Tarefa '{tarefas[indice]['titulo']}' concluida!")
    return True

def remover_tarefa(indice):
    if indice < 0 or indice >= len(tarefas):
        print("Tarefa não encontrada!")
        return False
    titulo = tarefas[indice]["titulo"]
    tarefas.pop(indice)
    print(f"Tarefa '{titulo}' removida!")
    return True

def buscar_tarefa(palavra):
    encontradas = []
    for t in tarefas:
        if palavra.lower() in t["titulo"].lower():
            encontradas.append(t)
    return encontradas

def main():
    while True:
        exibir_menu()
        opcao = input("Escolher: ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            titulo = input("Titulo da tarefa: ")
            prioridade = input("Priodirade (alta/media/baixa): ")
            adicionar_tarefa(titulo, prioridade)
        
        elif opcao == "2":
            listar_tarefas()
        
        elif opcao == "3":
            listar_tarefas()
            indice = int(input("Numero da tarefa para concluir: "))
            concluit_tarefa(indice)

        elif opcao == "4":
            listar_tarefas()
            indice = int(input("Numero da tarefa que deseja remover: "))
            remover_tarefa(indice)
        
        elif opcao == "5":
            palavra = input("Digite palavra para buscar: ")
            resultado = buscar_tarefa(palavra)
            if len(resultado) == 0:
                print("Nenhuma tarefa encontrada.")
            else:
                for t in resultado:
                    print(f"- {t['titulo']} | Prioridade: {t['prioridade']}")

        else:
            print("Opcao invalida!")

main()











