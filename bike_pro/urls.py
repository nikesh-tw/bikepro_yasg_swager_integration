"""bike_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include, re_path

#rest_framework_swagger 
#from rest_framework.views import schema_view
from rest_framework_swagger.views import get_swagger_view # <-- Here 1
#schema_view = get_swagger_view(title='My Vehicle API',version='1.0',description = "welcome to the world of swagger vehicle api",) # <-- Here 2
#path('docs/',schema_view), in urlpatterns ## <-- Here 3


# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title ="My drf yasg API",
        default_version = 'v1',
        description = "welcome to the world of yasg vehicle api"            
    ),
    #public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),  #<-- Here
    
    path('admin/', admin.site.urls),
    path('bike/',include('bike_app.urls')),    
]

#http://127.0.0.1:8000/bike/search-bike/ POST method input parameter- bike_number ="encoded"
#output-bike detail by bike_number.