from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.Index, basename='questions')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', views.Question_detail.as_view()),
]