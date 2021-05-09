from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.Index, basename='questions')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', views.Question_detail.as_view()),
]