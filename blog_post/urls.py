from django.urls import path
from . import views
from .views import index, by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric),
    path('', index),
]
