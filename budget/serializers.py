from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal

from .models import Threshold, Alert,Transaction 
#ThresholdType,  TransactionCategory, TransactionType, 


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'user', 'threshold', 'message']


class ThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threshold
        fields = ['id', 'user', 'name', 'slug', 'threshold_amount', 'type']


class TransactionSerializer(serializers.ModelSerializer):
    # category = TransactionCategorySerializer()
    # type = TransactionCategorySerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'user', 'date', 'category', 'description', 'amount', 'type']

    def create(self, validated_data):
        # category_data = validated_data.pop('category')
        # category = TransactionCategory.objects.create(**category_data)
        # validated_data['category'] = category
        # type_data = validated_data.pop('type')
        # type = TransactionCategory.objects.create(**type_data)
        # validated_data['type'] = type
        return Transaction.objects.create(**validated_data)
    


# class ThresholdTypeSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = ThresholdType
#         fields = ['id', 'name', 'slug']

# class TransactionCategorySerializer (serializers.ModelSerializer):
#     class Meta:
#         model = TransactionCategory
#         fields = ['id', 'title', 'slug']

# class TransactionTypeSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = TransactionType
#         fields = ['id', 'name', 'slug']