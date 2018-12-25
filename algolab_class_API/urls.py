"""algolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from . import views, routers

router = routers.AppRouter()
router.register(r'course', views.api.course.CourseViewSet, 'course')


api_info = openapi.Info(
    title="algolab_class API 문서",
    default_version='v1',
    description="algolab_class의 API 문서화",
    contact=openapi.Contact(email="***@***.com"),
    license=openapi.License(name="BSD License"),
)
schema_view = get_schema_view(
    api_info,
    # validators=['flex', 'ssv'],
    public=False,
    permission_classes=(permissions.DjangoModelPermissionsOrAnonReadOnly,),
)

urlpatterns = [
    url(r'^', include(router.urls)),
    # JWT 로그인
    url(r'^token/authorize/?$', obtain_jwt_token),
    url(r'^token/verify/?$', verify_jwt_token),
    # 온라인 API 문서화
    url(r'^docs/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^docs/swagger/?$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    url(r'^docs/?$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]