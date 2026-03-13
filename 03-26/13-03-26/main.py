from manager import TaskManager
import os

def menu():
    # Instancia o gerenciador (ele já carrega o JSON se existir)
    manager = TaskManager()

    while True:
        os.system('clear')
        print("\n--- MENU DE TAREFAS ---")
        print("1. Nova Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa por ID")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            title = input("Título: ")
            desc = input("Descrição: ")
            # O status já tem o padrão "Pendente" no seu código
            manager.new_task(title, desc)

        elif opcao == "2":
            manager.list_task()
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "3":
            manager.conclude_task()

        elif opcao == "4":
            # Para remover, o usuário digita o ID (ex: 00002)
            id_para_remover = input("Digite o ID da tarefa para remover (ex: 00001): ")
            manager.remove_task(id_para_remover)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
