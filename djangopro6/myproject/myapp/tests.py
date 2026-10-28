from django.test import TestCase

from .models import Student


class StudentCrudTests(TestCase):
    def test_create_list_and_delete_student(self):
        response = self.client.post(
            '/create/',
            {'name': 'Ada Lovelace', 'age': 36, 'email': 'ada@example.com'},
        )

        self.assertRedirects(response, '/')
        student = Student.objects.get(email='ada@example.com')
        self.assertEqual(student.age, 36)

        response = self.client.get('/')
        self.assertContains(response, 'Ada Lovelace')

        response = self.client.get(f'/delete/{student.id}/')
        self.assertRedirects(response, '/')
        self.assertFalse(Student.objects.filter(pk=student.id).exists())
