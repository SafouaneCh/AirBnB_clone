import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Initilialize the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_representation = dict.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__

        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()

        return dict_representation