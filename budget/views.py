import sys
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from .serializers import  TransactionSerializer, ThresholdSerializer, AlertSerializer
#, ThresholdTypeSerializer, TransactionCategorySerializer, TransactionTypeSerializer
from .models import  Transaction, User, Threshold, Alert
#, TransactionCategory, TransactionType, ThresholdType 

# Create your views here.

class ThresholdViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Threshold.objects.filter(user=request.user)
        serializer = ThresholdSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ThresholdSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        threshold = get_object_or_404(Threshold, user=request.user)
        serializer = ThresholdSerializer(threshold, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class AlertViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Alert.objects.filter(user=request.user)
        serializer = AlertSerializer(queryset, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save(user=request.user)

            # Begin checking if the transaction exceeds the user's threshold
            threshold = Threshold.objects.get(user=request.user)
           
            
            if transaction.amount > threshold.threshold_amount:
                message = f"Transaction amount ({transaction.amount}) exceeds threshold ({threshold.threshold_amount})"
                Alert.objects.create(user=request.user, threshold=threshold, message=message)
                return Response({'message': "Transaction amount exceeds threshold"}, status=201)
    
            return Response({'message': 'Transaction processed successfully'}, status=201)
        
        else:
            return Response(serializer.errors, status=400)
        

# class TransactionCategoryView(generics.ListCreateAPIView):
#     queryset = TransactionCategory.objects.all()
#     serializer_class = TransactionCategorySerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != 'GET':
#             permission_classes = [IsAuthenticated]

#         return [permission() for permission in permission_classes]

    
# class TransactionTypeView(generics.ListCreateAPIView):
#     queryset = TransactionType.objects.all()
#     serializer_class = TransactionTypeSerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != 'GET':
#             permission_classes = [IsAuthenticated]

#         return [permission() for permission in permission_classes]
    
# class ThresholdTypeView(generics.ListCreateAPIView):
#     queryset = ThresholdType.objects.all()
#     serializer_class = ThresholdTypeSerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != 'GET':
#             permission_classes = [IsAuthenticated]

#         return [permission() for permission in permission_classes]