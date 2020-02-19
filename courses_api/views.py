from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from courses.models import Course, Teacher
from .serializers import CourseSerializer, TeacherSerializer


# class CoursesApiListView(APIView):
#     def get(self, request):
#         items = Course.objects.all()
#         serializer = CourseSerializer(items, many=True)
#         return Response(serializer.data)

class CoursesApiListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer

class TeacherApiListView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


