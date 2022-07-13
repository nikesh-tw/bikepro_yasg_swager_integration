from django.urls import path
from .views import BikeDetailView
from . import views
#from .views import SwaggerSchemaView
#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='My great API', url='/a-different-path')


urlpatterns = [
    path('search-bike/',BikeDetailView.as_view(), name="bike-detail"),
    path('',views.index,name="index"),
]
#path('',SwaggerSchemaView.as_view(),name="swagger"),