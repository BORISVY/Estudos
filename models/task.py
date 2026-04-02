from datetime import datetime

class Task():
    def __init__(self, iid, title, desc, created_at=None, status="Pendente"):
        self.iid = iid
        self.title = title
        self.desc = desc
        self.created_at = created_at or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.status = status

    def to_dict(self):
        return {
            "id": self.iid,
            "title": self.title,
            "desc": self.desc,
            "created_at": self.created_at,
            "status": self.status
        }