# from django.test import TestCase
# from django.forms import ValidationError
# from .models import Thing

# class thingsModelTest(TestCase):
#     def setUp(self): # runs before each test
#         self.thing = Thing.objects.create(name="test", description="", quantity="50")
        
#     def test_integer_thing(self):
#         self.assert_thing_is_valid()

#     def test_integer_thing_over_100(self):
#         self.thing.quantity=101
#         self.assert_thing_is_invalid()

#     def assert_thing_is_valid(self):
#         try:
#             self.thing.full_clean()
#         except (ValidationError):
#             self.fail("Test thing should be valid")

#     def assert_thing_is_invalid(self):
#         with self.assertRaises(ValidationError):
#             self.thing.full_clean()