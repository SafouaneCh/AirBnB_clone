import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import time

class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)

    def test_id_is_uuid(self):
        instance = BaseModel()
        try:
            uuid_obj = uuid.UUID(instance.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID4")

    def test_created_at_is_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_updated_at_is_datetime(self):
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime)

    def test_updated_at_changes_on_save(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        time.sleep(1)  # Ensure there's a noticeable difference in time
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertGreater(instance.updated_at, old_updated_at)

    def test_unique_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str_method(self):
        instance = BaseModel()
        expected_str = f"[{instance.__class__.__name__}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_to_dict(self):
        instance = BaseModel()
        dict_repr = instance.to_dict()
        self.assertEqual(dict_repr['__class__'], instance.__class__.__name__)
        self.assertEqual(dict_repr['id'], instance.id)
        self.assertEqual(dict_repr['created_at'], instance.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], instance.updated_at.isoformat())
        self.assertEqual(dict_repr['created_at'], instance.to_dict()['created_at'])
        self.assertEqual(dict_repr['updated_at'], instance.to_dict()['updated_at'])



if __name__ == "__main__":
    unittest.main()
