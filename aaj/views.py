from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import modi
from .serializers import sermodi


class TodayAPI(APIView):
    def get(self,request,pk=None,format=None):

        id=pk
        if id is not None:
            a =modi.objects.get(id=id)
            serializer= sermodi(a)
            return Response(serializer.data)
        a= modi.objects.all()
        serializer = sermodi(a, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer= sermodi(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data cretared'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        id=pk
        a= modi.objects.get(id=id)
        serializer = sermodi(a,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'competed data update'})
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk=None,format=None):
        id=pk 
        a= modi.objects.get(id=id)
        serializer= sermodi(a,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg':'one data update'})
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        id=pk
        aa= modi.objects.get(id=id)
        aa.delete()
        return Response({'msg':'deleted data'})







