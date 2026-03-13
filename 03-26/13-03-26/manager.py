import json
import os
from task import Task

class TaskManager():
    def __init__(self):
        self.document = "tasklist.json"
        self.task_list = self.load_task()

    def load_task(self):
        if os.path.exists(self.document):
            try: 
                with open(self.document, "r", encoding="utf-8") as arq:
                    return json.load(arq)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save(self):
        with open(self.document, "w", encoding="utf-8") as arq:
            json.dump(self.task_list, arq, indent=4, ensure_ascii=False)   

    def reorder_ids(self):
        for index, task in enumerate(self.task_list, start=1):
            task["ID"] = str(index).zfill(5)

    def new_task(self, title, desc, status="Pendente"):
        """Cria um objeto Task, converte em dict e salva na lista"""
        new_t = Task(None, title, desc, status)  
        self.task_list.append(new_t.to_dict())
        self.reorder_ids()
        self.save()
        print(f"Tarefa '{title}' salva com sucesso!")

    def remove_task(self, id_for_remove):
        """Remove pelo ID e reajusta todos os outros IDs"""
        # Filtra a lista mantendo apenas quem NÃO tem o ID digitado
        nova_lista = [t for t in self.task_list if t["ID"] != id_for_remove]
        
        if len(nova_lista) == len(self.task_list):
            print("ID não encontrado!")
            return

        self.task_list = nova_lista
        self.reorder_ids() # Puxa os IDs "para cima" para tapar o buraco
        self.save()
        print(f"Tarefa {id_for_remove} removida e IDs reorganizados!")

    def list_task(self):
        os.system("clear")
        """ Função que exibe uma listagem das tarefas cadastrados no arquivo .json"""
        if not self.task_list:
            print("Nenhuma tarefa cadastrada!")
            return
        print(f"{'ID':<5} | {'TÍTULO':<30} | {'DESCRIÇÂO': <100} | {'STATUS':<12}") # Cabeçalho alinhado
        print("-" * 45)
        for task in self.task_list:
            iid = task.get("ID")
            title = task.get("Title")
            desc = task.get("Desc")
            status = task.get("Status")
            print(f"{iid:<5} | {title:<30} | {desc:<100} | {status:<12}")

    def conclude_task(self):
        os.system("clear")
        """ Função que exibe uma listagem das tarefas cadastrados no arquivo json e
        pede ao usuário para digitar o código da tarefa que quer concluir"""
        self.list_task()
        id_task = input("Digite o ID da tarefa para concluir (ex: 00001):")
        for task in self.task_list:
            if int(task["ID"]) == int(id_task):
                task["Status"] = "Concluida"
                break
        self.save()
        print(f"Tarefa {id_task} concluída com sucesso!")
        input("\nPressione ENTER para confirmar...")
        os.system("clear")
        self.list_task()
        input("\nPressione ENTER para voltar ao menu...")