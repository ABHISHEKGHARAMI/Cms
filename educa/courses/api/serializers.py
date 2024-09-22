from rest_framework import serializers
from  courses.models import Subject , Course , Module, Content

# class for serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','title','slug']
        
# serializer for module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']
        
        
# serializer for the course
class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner',
                  'modules']
        
        
# serializer for item fields to render the item
class ItemRelatedField(serializers.RelatedField):
    def to_representation(self,value):
        return value.render()
    
    

# content serializer
class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)
    class Meta:
        model = Content
        fields = ['order','item']
        


# class with alternative content serializer
class ModuleWithContentSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = ['order','title','description','content']
        
        
# alternative serializer for course
class CourseWithContentSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)
    class Meta:
        model = Course
        fields = ['id','subject','title','slug',
                  'overview','created','owner','modules']
    
        