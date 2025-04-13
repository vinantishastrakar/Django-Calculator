from django.shortcuts import render
from .serializers import CalculationSerializer
from rest_framework import APIView
from rest_framework import status
from rest_framework.response import Response

class CalculationNum(APIView):
    























# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import CalculationSerializer

# # Create your views here.

# @api_view(["POST"])
# def calculatorNum(request):
#     serializer = CalculationSerializer(data=request.data)

#     if serializer.is_valid():
#         num1 = serializer.validated_data['num1']
#         num2 = serializer.validated_data['num2']
#         operation = serializer.validated_data['operation']

#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             if num1 == 0 or num2 == 0:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             result = num1 * num2
#         elif operation == 'divide':
#             if num2 == 0:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             result = num1 / num2
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         return Response({
#             'num1' : num1,
#             'num2' : num2,
#             'operation' : operation,
#             'result' : result
#         })
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)