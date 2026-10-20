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

@api_view(["POST"])
def add_student(request):
    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
