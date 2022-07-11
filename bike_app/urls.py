from django.urls import path
from .views import BikeDetailView
#from .views import SwaggerSchemaView
#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='My great API', url='/a-different-path')


urlpatterns = [
    path('search-bike/',BikeDetailView.as_view(), name="bike-detail"),
]
#path('',SwaggerSchemaView.as_view(),name="swagger"),