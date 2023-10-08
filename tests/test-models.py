from django.test import TestCase
from reservation import models
class MenuItemTest(TestCase):
    def test_1(self):
        item = models.Menu.objects.create(Title = 'IceCream', Price = 80, Inventory = 100)
        self.assertEqual(item,'IceCream : 80')