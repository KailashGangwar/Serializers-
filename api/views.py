
from django.shortcuts import render
from .serializer import studentSerializers
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse 

def student_details(request,pk):
    stu=Student.objects.get(id=pk)
    # print(stu)
    serializer=studentSerializers(stu)
    # print(serializer)
    # print(serializer.data)
    # json_data =JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)



def student_list(request):
    stu=Student.objects.all()
    # print(stu)
    serializer=studentSerializers(stu,many=True)
    # print(serializer)
    # print(serializer.data)
    json_data =JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    
