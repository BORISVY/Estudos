import json
import os

class TaskList():
    def __init__(self):
        self.document = "tasklist.json"
        self.task_list = self.load_task()

    def load_task(self):
        if os.path.exists(self.document):
            try: 
                with open(self.document, "r", encoding="utf-8") as arq:
                    return json.load(arq)
            except json.JSONDecodeError:
                return []
        return []
    
    def save(self):
        with open("tasklist.json", "r", encoding="utf-8") as arq:
            json.dump(self.task_list, arq, indent=4, ensure_ascii=False)
        

    def new_task(self, iid, tittle, desc, status):
        
        task = {
            "ID": iid,
            "Tittle": tittle,
            "Description": desc,
            "Status": status
        }   
        self.task_list.append(task)
        self.save()
        print("Tarefa salva com sucesso!")

    
