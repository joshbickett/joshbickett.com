from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('projects/', views.projects, name='portfolio-projects'),
    path('blog/', views.blog, name='portfolio-blog'),
]
