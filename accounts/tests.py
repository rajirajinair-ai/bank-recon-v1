from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Role, Permission, RolePermission

class AccountsModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="Admin", description="Administrator Role")
        self.permission = Permission.objects.create(name="Can View Reports", code="view_reports")
        self.role_permission = RolePermission.objects.create(role=self.role, permission=self.permission)
        self.user = User.objects.create_user(username="testuser", password="testpassword123", role=self.role)

    def test_role_creation(self):
        self.assertEqual(self.role.name, "Admin")
        self.assertEqual(str(self.role), "Admin")

    def test_permission_creation(self):
        self.assertEqual(self.permission.name, "Can View Reports")
        self.assertEqual(str(self.permission), "Can View Reports")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.role, self.role)
        self.assertEqual(str(self.user), "testuser")
        self.assertTrue(self.user.check_password("testpassword123"))

class AccountsAPITest(APITestCase):
    def setUp(self):
        self.role = Role.objects.create(name="Manager")

    def test_get_roles(self):
        url = reverse('role-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'password': 'newpassword123', 'role': self.role.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
