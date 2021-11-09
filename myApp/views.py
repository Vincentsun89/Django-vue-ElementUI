# Create your views here.
from __future__ import unicode_literals

import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from myApp.models import Student


#创建view 
#add_student 接受一个get请求 网数据里添加一条student 数据
@require_http_methods(["GET"])
def add_student(request):
    response = {}
    try:
        student = Student(student_name=request.GET.get('student_name'))
        student.save()
        response['msg']="success"
        response['error_num']=0
    except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
    return JsonResponse(response)

# show_students返回所有的学生列表（通过JsonResponse返回能被前端识别的json格式数据）
@require_http_methods(["GET"])
def show_students(request):
    response = {}
    try:
        students = Student.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", students))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
 
    return JsonResponse(response)
