from rest_framework import serializers
from .models import Question, Comment, LikeQuestion

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['writer', 'question_number', 'body', 'created_time']
        
class QuestionSerializer(serializers.ModelSerializer):
    #nested serializer : 1:N, M:N 관계를 serializer 로 정의 가능
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        # field 에 nested serializer 변수 추가
        fields = ['id', 'writer', 'title', 'question', 'created_time','comments']

class TreatQuestionSerializer(serializers.ModelSerializer):
    # writer = serializers.ReadOnlyField(source = 'writer') # perform_create 에서 Return 한 값을 받아옴
    class Meta:
        model = Question
        fields = ['id','writer', 'title', 'question']
        read_only_fields = ['writer']
