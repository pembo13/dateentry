# django imports
from django.urls import path
# app imports
from . import views


# patterns

app_name = 'frontend'
urlpatterns = [

	path('', views.entry, name='entry'),

]
