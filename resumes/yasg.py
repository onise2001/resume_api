from django.urls import re_path, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from resumes_api.serializers import ResumeSerializer


schema_view = get_schema_view(
    openapi.Info(
        title='Resume API',
        default_version='V1',
        description='Resume API',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]


from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema

class CustomAutoSchema(SwaggerAutoSchema):
    def get_serializer_fields(self, serializer):
        fields = super().get_serializer_fields(serializer)
        if isinstance(serializer, ResumeSerializer):
            fields['general'] = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'image': openapi.Schema(type=openapi.TYPE_STRING),
                    'about_me': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'phone_number': openapi.Schema(type=openapi.TYPE_STRING),

                    # Add other fields as needed
                },
            )
            fields['experience'] = openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'position': openapi.Schema(type=openapi.TYPE_STRING),
                        'employer': openapi.Schema(type=openapi.TYPE_STRING),
                        'started_at': openapi.Schema(type=openapi.TYPE_STRING),
                        'ended_at': openapi.Schema(type=openapi.TYPE_STRING),
                        'description': openapi.Schema(type=openapi.TYPE_STRING),

                        # Add other fields as needed
                    },
                ),
            )
            fields['education'] = openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'school': openapi.Schema(type=openapi.TYPE_STRING),
                    'degree': openapi.Schema(type=openapi.TYPE_STRING),
                    'graduation_date': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING),

                    # Add other fields as needed
                },
            )
        return fields