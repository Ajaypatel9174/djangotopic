from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stu_name = serializers.CharField(max_length=100)
    stu_email = serializers.EmailField()
    stu_contact = serializers.IntegerField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.stu_name = validated_data.get('stu_name', instance.stu_name)
        instance.stu_email = validated_data.get('stu_email', instance.stu_email)
        instance.stu_contact = validated_data.get('stu_contact', instance.stu_contact)
        instance.save()
        return instance