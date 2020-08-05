
from django.urls import path
from hello_app.views import index_view

urlpatterns = [
    path('',index_view),   
   
]
