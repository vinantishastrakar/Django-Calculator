from rest_framework import serializers

class CalculationSerializer(serializers.Serializer):
    num1 = serializers.FloatField()
    num2 = serializers.FloatField()
    operation = serializers.CharField(max_length = 20)
    result = serializers.FloatField(read_only = True)

    