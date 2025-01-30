from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('ユーザー名', max_length=200)
    email = models.EmailField('メールアドレス', max_length=200)
    password = models.CharField('パスワード', max_length=200)
    created_at = models.DateTimeField('作成日時', default=timezone.now)
    updated_at = models.DateTimeField('更新日時', default=timezone.now)