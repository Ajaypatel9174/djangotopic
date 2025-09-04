from rest_framework import serializers

class Stu_Serializer(serializers.Serializer):
    stu_name = serializers.CharField()
    stu_email = serializers.EmailField()
    stu_contact = serializers.IntegerField()
    stu_image = serializers.ImageField()
    stu_resume = serializers.FileField()