from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('ユーザー名', max_length=30)
    email = models.EmailField('メールアドレス', max_length=254)
    password = models.CharField('パスワード', max_length=128)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.id)


class Test(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        User, 
        verbose_name='ユーザーID', 
        on_delete=models.PROTECT,
        db_column='userid'
    )
    title = models.CharField('問題タイトル', max_length=50)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'tests'

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    testid = models.ForeignKey(
        Test, 
        verbose_name='テストID', 
        on_delete=models.PROTECT,
        db_column='testid'
    )
    correct_choiceid = models.IntegerField('正解の選択肢')
    text = models.CharField('問題文', max_length=20)
    explanation = models.CharField('解説', max_length=20)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'questions'

    def __str__(self):
        return str(self.id)


class QuestionChoice(models.Model):
    id = models.AutoField(primary_key=True)
    questionid = models.ForeignKey(
        Question, 
        verbose_name='問題ID', 
        on_delete=models.PROTECT,
        db_column='questionid'
    )
    
    text = models.CharField('選択肢文', max_length=20)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'question_choices'

    def __str__(self):
        return str(self.id)


class Examination(models.Model):
    id = models.AutoField(primary_key=True)
    testid = models.ForeignKey(
        Test, 
        verbose_name='テストID', 
        on_delete=models.PROTECT,
        db_column='testid'
    )
    guestname = models.CharField('ゲスト名', max_length=20)
                                 
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'examinations'

    def __str__(self):
        return str(self.id)


# 問題単位に対応している
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    examinationid = models.ForeignKey(
        Examination, 
        verbose_name='受験ID', 
        on_delete=models.CASCADE,
        db_column='examinationid'
    )
    questionid = models.ForeignKey(
        Question, 
        verbose_name='質問ID', 
        on_delete=models.CASCADE,
        db_column='questionid'
    )
    selected_choiceid = models.IntegerField('選択肢')
    iscorrect = models.BooleanField('正解', default=False)
    answered_at = models.DateTimeField('回答日時', default=timezone.now)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return str(self.id)
        