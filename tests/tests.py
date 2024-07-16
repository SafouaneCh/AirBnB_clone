import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def test_init_no_kwargs(self):
        """Test initialization with no kwargs"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertEqual(len(model.id), 36)  # UUID length
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_init_with_kwargs(self):
        """Test initialization with kwargs"""
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": "2023-07-15T12:34:56",
            "updated_at": "2023-07-16T12:34:56",
            "name": "Test Model"
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, kwargs["id"])
        self.assertEqual(model.name, kwargs["name"])
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(model.updated_at, datetime.fromisoformat(kwargs["updated_at"]))

    def test_str(self):
        """Test the __str__ method"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertGreater(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
