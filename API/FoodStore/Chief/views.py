from django.shortcuts import render
from .models import chief
from .serializers import ChiefSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class chiefViewSet(ModelViewSet):
    queryset=chief.objects.all()
    serializer_class=ChiefSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . models import chief
from .serializers import ChiefSerializer
from rest_framework import status,parsers
from rest_framework.exceptions import APIException
from rest_framework.response import Response

# Create your views here.
class ChiefViewSet(ModelViewSet):
    queryset = chief.objects.all()
    serializer_class = ChiefSerializer
    

    def get_serializer_class(self):
        if self.action == 'list':
            return ChiefSerializer
        if self.action == 'create':
            return ChiefSerializer
        return self.serializer_class
    
   
    #get all chiefs

    def list(self,request):
        try:
            chief_objs = chief.objects.all()
            serializer = self.get_serializer(chief_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add chief
    def create(self,request):
        try:
            serializer =self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'chief added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single chief
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:

                #chief_objs = chief.objects.all()
                chief_objs = self.get_object()
                serializer = self.get_serializer(chief_objs)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of chief
    def update(self,request, pk=None):
        try:
            #chief_objs = chief.objects.all()
            chief_objs = self.get_object()
            serializer = self.get_serializer(chief_objs,data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'chief updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields

    def partial_update(self,request, pk=None):
        try:
            #chief_objs = chief.objects.all()
            chief_objs = self.get_object()
            serializer = self.get_serializer(chief_objs,data=request.data,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'chief updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    def destroy(self, request,pk):
        try:
            id=pk
            chief_obj = self.get_object()
            chief_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'chief deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })