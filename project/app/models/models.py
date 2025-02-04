from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('ユーザー名', max_length=20)
    email = models.EmailField('メールアドレス', max_length=50)
    password = models.CharField('パスワード', max_length=50)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'users'

# class Test(models.Model):

# class Question(models.Model):

# class Choice(models.Model):

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    testid = models.ForeignKey(
        Test, verbose_name='テストID', on_delete=models.PROTECT,
    )
    guestname = models.CharField('ゲスト名', max_length=20)
                                 
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'sessions'

# 問題単位に対応している
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    sessionid =  models.ForeignKey(
        Session, verbose_name='セッションID', on_delete=models.PROTECT,
    )
    questionid =  models.ForeignKey(
        Question, verbose_name='質問ID', on_delete=models.PROTECT,
    )
    selectedchoice = models.IntegerField('選択肢')
    iscorrect = models.BooleanField('正解', default=False)
    answered_at = models.DateTimeField('回答日時', default=timezone.now)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'answers'
