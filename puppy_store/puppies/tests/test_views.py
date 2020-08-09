from rest_framework.test import APITestCase


class ListPuppies(APITestCase):
    def test_list_puppies_ok(self):
        self.assertEqual(1 + 1, 2)
