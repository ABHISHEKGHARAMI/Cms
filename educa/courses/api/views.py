from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from courses.models import Subject , Course 
from courses.api.serializers import SubjectSerializer, CourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
# Adding the custom api view for the enrolling the course for the student
class CourseEnrollView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="Enroll in a specific course",
        request_body=None,  # Adjust if you expect a request body
        responses={200: openapi.Response(description="Enrollment status", examples={
                                         'application/json': {'enrolled': True}})},
    )
    def post(self,request,pk,format=None):
        course = get_object_or_404(Course,pk=pk)
        course.students.add(request.user)
        return Response({
            'enrolled' : True
        }, status=status.HTTP_200_OK)
        
    

    
    