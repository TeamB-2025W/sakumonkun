from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("メールアドレスは必須です")
        user = self.model(email=self.normalize_email(email), username=username) # emailのフォーマットを正規化
        user.set_password(password)  # パスワードをハッシュ化
        user.save(using=self._db)
        return user
    
    # 管理者ユーザーの作成 
    # AllAuthを採用するした場合、 python manage.py createsuperuserでエラーになる
    # この記述により、管理者ユーザーの作成が可能になる
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# AbstractBaseUserを継承することで、ユーザー認証の機能を持たせる
# PermissionsMixinを継承することで、ユーザーの権限を管理する機能を持たせる
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField('ユーザー名', max_length=30, unique=True)
    email = models.EmailField('メールアドレス', max_length=254, unique=True)
    password = models.CharField('パスワード', max_length=128)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    is_superuser = models.BooleanField(default=False)  # スーパーユーザー権限
    is_staff = models.BooleanField(default=False)      # 管理画面アクセス権限
    is_active = models.BooleanField(default=True)      # アカウントアクティブ状態

    # この定義により、UserManagerを使用することができる
    # 使用例： User.objects.create_user(email, username, password)
    # 使用例： User.objects.create_superuser(email, username, password)
    objects = UserManager()

    USERNAME_FIELD = "username" # 認証に必要なフィールド
    REQUIRED_FIELDS = ["email"] # `createsuperuser` で追加入力が必要なフィールド

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
        db_column='userid',
        
        # デバッグ中のみ
        null=True,
        blank=True
        # ここまで
    
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
        db_column='testid',
        related_name='questions', 
    )
    correct_choiceid = models.IntegerField('正解の選択肢')
    text = models.TextField('問題文')
    explanation = models.TextField('解説', null=True, blank=True)
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
    
    text = models.TextField('選択肢文')
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
    answered_at = models.DateTimeField('回答日時', default=timezone.now)
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
        on_delete=models.PROTECT,
        db_column='examinationid'
    )
    questionid = models.ForeignKey(
        Question, 
        verbose_name='問題ID', 
        on_delete=models.PROTECT,
        db_column='questionid'
    )
    selected_choiceid = models.IntegerField('選択肢')
    iscorrect = models.BooleanField('正解', default=False)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)

    class Meta:
        db_table = 'answers'

    def __str__(self):
        return str(self.id)
        