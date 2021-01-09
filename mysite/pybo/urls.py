from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hwanils', views.hwanils),
    path('<int:question_id>/', views.detail),
]