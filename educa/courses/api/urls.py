from django.urls import path ,include
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers


app_name = 'courses'

router = routers.DefaultRouter()
router.register('course',views.CourseViewSet)

# schema for the swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Courses API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@courses.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<int:pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),
    path('courses/<int:pk>/enroll/',
         views.CourseEnrollView.as_view(),
         name='course_enroll'),
    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    # Redoc documentation URLs (optional)
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('',include(router.urls)),
    
]
