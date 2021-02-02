from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,\
    DestroyModelMixin

# Create your views here.


#-----------GenericAPIView and Model Mixin----------------

class StudentList(ListModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class StudentRetrieve(RetrieveModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class StudentUpdate(UpdateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)



class StudentDestroy(DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

























#-----------------class APIView------------------
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data)


    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})








#-----------------------function------------------------------

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def student_api(request,pk=None):
#     if request.method == 'GET':
#         #this will give u whole data
#         id = pk
#         # id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         else:
#             stu = Student.objects.all()
#             serializer = StudentSerializer(stu,many=True)
#             return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     elif request.method == 'PUT':
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data updated'})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PATCH':
#         # id = request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data updated'})
#         return Response(serializer.errors)
#
#     elif request.method == 'DELETE':
#         # id =  request.data.get('id')
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})










#----GET------------
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello world'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':"this is POST request"})

#---------Both get and post combine---------
# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg': 'this is GET request'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':"this is POST request"})