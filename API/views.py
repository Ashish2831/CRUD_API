from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .serializers import Student_Serializer
from django.http import JsonResponse
import io

# Create your views here.
@csrf_exempt
def Student_API(request):
    if request.method == "GET":
        # Converting json data into stream bytes
        stream = io.BytesIO(request.body)
        # Converting stream bytes into python native data type (Dictionary)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        if id is not None:
            student = Student.objects.get(pk=id)
            # Converting complex data type into python native data type
            serializer = Student_Serializer(student)
        else:
            students = Student.objects.all()
            # Converting complex data type into python native data type
            serializer = Student_Serializer(students, many=True)
        
        # Converting python native data type into json data
        json_data = JSONRenderer().render(serializer.data)
        # Sending JSON Data
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)

    if request.method == "POST":
        # Converting json data into stream bytes
        stream = io.BytesIO(request.body)
        # Converting stream bytes into python native data type (Dictionary)
        pythonData = JSONParser().parse(stream)
        # Converting python native data type into complex data type
        serializer = Student_Serializer(data=pythonData)
        if serializer.is_valid():
            serializer.save() # Saving data into database
            response = {'message' : 'Data Inserted Successfully!'}
            # Converting python native data type into json data
            json_data = JSONRenderer().render(response)
        else:
            # Converting python native data type into json data
            json_data = JSONRenderer().render(serializer.errors)

        # Sending JSON Data
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)

    if request.method == "PUT":
        # Converting json data into stream bytes
        stream = io.BytesIO(request.body)
        # Converting stream bytes into python native data type (Dictionary)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        student = Student.objects.get(pk=id)
        # Converting python native data type into complex data type along with partial update
        serializer = Student_Serializer(student, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save() # Saving data into database
            response = {'message' : 'Data Updated Successfully!'}
            # Converting python native data type into json data
            json_data = JSONRenderer().render(response)
        else:
            # Converting python native data type into json data
            json_data = JSONRenderer().render(serializer.errors)
        
        # Sending JSON Data
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)

    if request.method == "DELETE":
        # Converting json data into stream bytes
        stream = io.BytesIO(request.body)
        # Converting stream bytes into python native data type (Dictionary)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            response = {'message' : 'Data Deleted Successfully!'}
        except Exception as e:
            response = {'message' : f'{e}'}
        # Converting python native data type into json data
        json_data = JSONRenderer().render(response)
        # Sending JSON Data
        return HttpResponse(json_data, content_type="application/json")
        # return JsonResponse(json_data)