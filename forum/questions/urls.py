from django.urls import path, include
from. import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.Index, basename='questions') # 모든 질문들 확인 url
router.register('comment', views.CommentViewSet, basename='comment') # 모든 댓글 확인 url

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', views.Question_detail.as_view()), # 상세 댓글을 위한 url
]