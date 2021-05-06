from django.db import models
from account.models import User

# Create your models here.


class Question(models.Model):
    '''
    질문에 대한 테이블
    '''
    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    question = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True) # 질문 작성 시간 자동기록

    likes = models.ManyToManyField(
        User,
        blank=True,
        through ='LikeQuestion', # automatically generate table 말고 직접 table 을 설계한 경우 해당 테이블의 이름 작성
        through_fields = ('question_number', 'like_user'),
        related_name='likes' # 역참조시 이름을 정하지 않을 경우 makemigrations 에서 SystemCheckError 발생
    )

    class Meta:
        db_table = 'forum_question'
        ordering = ['created_time']
        verbose_name = 'question'
        verbose_name_plural = 'question_list'


class Comment(models.Model):
    '''
    특정 질문에 댓글의 정보 테이블
    '''
    question_number = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    writer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    body = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True) # 댓글 작성 시간 자동 기록

    def __str__(self):
        return self.question_number

    class Meta:
        db_table = 'forum_comment'
        ordering = ['question_number']
        verbose_name ='comment'
        verbose_name_plural = 'comment list'

class LikeQuestion(models.Model):
    '''
    특정 질문에 좋아요를 누른 사용자 정보 테이블
    '''
    question_number = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    like_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.question_number

    class Meta:
        db_table = 'forum_likequestion'
        ordering = ['question_number']
        verbose_name = 'question like'
        verbose_name_plural = 'question like list'