from django.urls import path
from . import views
from .views import index, by_rubric, by_post, about

urlpatterns = [
    path('posts/<int:post_id>/', by_post, name='by_post'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('about/', about, name='about'),
    path('', index, name='index'),
]
