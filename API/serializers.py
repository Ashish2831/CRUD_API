from rest_framework import serializers
from .models import Student

class Student_Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    rollNo = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.rollNo = validated_data.get('rollNo', instance.rollNo)
        instance.city = validated_data.get('city', instance.city)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance