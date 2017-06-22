from django.shortcuts import get_object_or_404
from models import Stu
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Student.serializers import StuSerializer


# Create your views here.
class Stud_info(APIView):

    def get(self,request):
        info=Stu.objects.all()
        serializer=StuSerializer(info, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
