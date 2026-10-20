from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    serializers = StudentSerializers(students, many=True)
    return Response(serializers.data)