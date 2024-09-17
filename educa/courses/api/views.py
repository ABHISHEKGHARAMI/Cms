from rest_framework import generics
from courses.models import Subject , Course
from courses.api.serializers import SubjectSerializer, CourseSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
    

    
    