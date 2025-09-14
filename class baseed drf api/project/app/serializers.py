from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stu_name = serializers.CharField(max_length=100)
    stu_email = serializers.EmailField()
    stu_contact = serializers.IntegerField()