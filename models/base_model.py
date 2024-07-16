import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at =  datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__

        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict

