import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from .views import ThresholdViewSet, AlertViewSet, TransactionViewSet
from .serializers import  TransactionSerializer, ThresholdSerializer, AlertSerializer
from .models import  Transaction, User, Threshold, Alert

# Create your tests here.

class BudgetAppTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create(username='test_user', password='password')

        # Create a threshold for the user
        self.threshold = Threshold.objects.create(user=self.user, threshold_amount=1000)

        # Create transactions
        Transaction.objects.create(user=self.user, date='2024-04-01', category='Groceries', description='Grocery shopping', amount=50, type='Expense')
        Transaction.objects.create(user=self.user, date='2024-04-02', category='Salary', description='Monthly salary', amount=2000, type='Income')

    # Check if 50 transaction is viewable
    def test_transaction_model(self):
        transaction = Transaction.objects.get(category='Groceries')
        self.assertEqual(transaction.user, self.user)
        self.assertEqual(transaction.amount, 50)

    # Check if 1000 threshold was triggered
    def test_threshold_model(self):
        threshold = Threshold.objects.get(user=self.user)
        self.assertEqual(threshold.user, self.user)
        self.assertEqual(threshold.threshold_amount, 1000)

    # Check if entire 50 transaction was created and serialized on return
    def test_transaction_serializer(self):
        transaction = Transaction.objects.get(category='Groceries')
        serializer = TransactionSerializer(transaction)
        expected_data = {'id': 1, 'user': self.user.id, 'date': '2024-04-01', 'category': 'Groceries', 'description': 'Grocery shopping', 'amount': '50.00', 'type': 'Expense'}
        self.assertEqual(serializer.data, expected_data)

if __name__ == '__main__':
    unittest.main()