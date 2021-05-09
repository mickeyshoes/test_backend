from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .models import Question, Comment, LikeQuestion
from .serializers import QuestionSerializer , TreatQuestionSerializer, CommentSerializer
from account.models import User
from .permissions import CheckObjectOwnerPermission
# Create your views here.

class Index(viewsets.ModelViewSet):

    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, CheckObjectOwnerPermission]
    serializer_class = TreatQuestionSerializer

    #serializer.save() 오버라이딩 하는 함수
    def perform_create(self, serializer):
        return serializer.save(writer=self.request.user)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        serializer = TreatQuestionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 여기서 null constraint 제약 조건이 걸려서 에러가 나는것 같음 -> 사용자 객체를 미리 넣어줄 수는 없나?
            serializer.save(writer=user)
            return Response({'message' : 'success'}, status=status.HTTP_201_CREATED)
        
        else:
            return Response({'message' : 'fail'}, status=status.HTTP_412_PRECONDITION_FAILED)
        

class Question_detail(APIView):

    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response({'message' : 'invalid access'}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        permission_classes = [IsAuthenticated]
        question = self.get_object(pk)
        serializer = TreatQuestionSerializer(question)
        if serializer.is_valid(raise_exception=True):
            question = serializer.validate_data
            print(question)
        '''
        삭제하는 사람이 본인이 맞는지 확인하는 로직 들어가야함
        '''
        # question.delete()
        return Response({'message' : 'success'}, status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly, CheckObjectOwnerPermission]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(writer=request.user, question_number=request.pk)

    def retrieve(self, request, pk):
        print(pk)