from django.db import migrations
from django.utils import timezone
from django.contrib.auth.hashers import make_password

def create_initial_user(apps, schema_editor):
    User = apps.get_model('app', 'User')
    
    # rootユーザーのみ作成
    User.objects.create(
        username='root',  # idは自動採番させる
        email='root@example.com',
        password=make_password('root'),
        is_superuser=True,
        is_staff=True,
        is_active=True,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_user,
            reverse_code=migrations.RunPython.noop
        ),
    ] 