from rest_framework import serializers
from .models import Question, Comment, LikeQuestion

class CommentSerializer(serializers.ModelSerializer):
    login_id = serializers.ReadOnlyField(source='user.login_id')
    question_number = serializers.ReadOnlyField(source='')
    class Meta:
        model = Comment
        fields = '__all__'
        
class QuestionSerializer(serializers.ModelSerializer):
    #nested serializer : 1:N, M:N 관계를 serializer 로 정의 가능
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        # field 에 nested serializer 변수 추가
        fields = ['id', 'writer', 'title', 'question', 'created_time','comments']

class TreatQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','writer', 'title', 'question']
        read_only_fields = ['writer']
