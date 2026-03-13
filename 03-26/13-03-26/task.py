class Task():
    def __init__(self, iid, title, desc, status="Pendente"):
        self.iid = iid
        self.title = title
        self.desc = desc
        self.status = status

    def to_dict(self):
        """Converte o objeto para dicionário para salvar no JSON
        """
        return {
            "ID": self.iid,
            "Title": self.title,
            "Desc": self.desc,
            "Status": self.status
        }

        

    
