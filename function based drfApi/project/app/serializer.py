
from rest_framework import serializers
from.models import Student

class StuSerializer(serializers.Serializer):
    stu_name=serializers.CharField()
    stu_email=serializers.EmailField()
    stu_contact=serializers.IntegerField()