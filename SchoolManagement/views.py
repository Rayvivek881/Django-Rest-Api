from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Teacher
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoObjectPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def list(self, request):
    filterObject = {}
    for key, val in request.query_params.items():
      filterObject[key] = val
    queryset = Student.objects.filter(**filterObject)
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = StudentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def retrieve(self, request, pk=None):
    queryset = Student.objects.get(id=pk)
    serializer = StudentSerializer(queryset)
    return Response(serializer.data)
  
  def update(self, request, pk=None):
    queryset = Student.objects.get(id=pk)
    serializer = StudentSerializer(queryset, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def partial_update(self, request, pk=None):
    queryset = Student.objects.get(id=pk)
    serializer = StudentSerializer(queryset, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, pk=None):
    queryset = Student.objects.get(id=pk)
    queryset.delete()
    return Response('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
  

class TeacherViewSet(viewsets.ViewSet):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]

  def list(self, request):
    filterObject = {}
    for key, val in request.query_params.items():
      filterObject[key] = val
    queryset = Teacher.objects.filter(**filterObject)
    serializer = TeacherSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = TeacherSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def retrieve(self, request, pk=None):
    queryset = Teacher.objects.get(id=pk)
    serializer = TeacherSerializer(queryset)
    return Response(serializer.data)
  
  def update(self, request, pk=None):
    queryset = Teacher.objects.get(id=pk)
    serializer = TeacherSerializer(queryset, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def partial_update(self, request, pk=None):
    queryset = Teacher.objects.get(id=pk)
    serializer = TeacherSerializer(queryset, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  def destroy(self, request, pk=None):
    queryset = Teacher.objects.get(id=pk)
    queryset.delete()
    return Response('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
