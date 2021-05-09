from django.urls import path
from. import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('<int:pk>', views.Question_detail.as_view()),
]