from django.db import migrations
from django.utils import timezone

def create_initial_data(apps, schema_editor):
    User = apps.get_model('app', 'User')
    Test = apps.get_model('app', 'Test')
    Question = apps.get_model('app', 'Question')
    QuestionChoice = apps.get_model('app', 'QuestionChoice')

    # ユーザーデータ
    users = [
        User(
            id=1,
            username='test_user1',
            email='test1@example.com',
            password='password123',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        User(
            id=2,
            username='test_user2',
            email='test2@example.com',
            password='password456',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    User.objects.bulk_create(users)

    # テストデータ
    tests = [
        Test(
            id=1,
            userid_id=1,
            title='基本情報技術者試験模擬テスト',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Test(
            id=2,
            userid_id=2,
            title='Python基礎テスト',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    Test.objects.bulk_create(tests)

    # 問題データ
    questions = [
        Question(
            id=1,
            testid_id=1,
            correct_choiceid=1,
            text='Pythonの特徴は？',
            explanation='Pythonは読みやすい構文が特徴です',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=2,
            testid_id=1,
            correct_choiceid=5,
            text='データベースとは？',
            explanation='データを効率的に管理するシステム',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=3,
            testid_id=2,
            correct_choiceid=7,
            text='変数とは？',
            explanation='データを格納する箱のようなもの',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    Question.objects.bulk_create(questions)

    # 選択肢データ
    choices = [
        QuestionChoice(id=1, questionid_id=1, text='読みやすい構文'),
        QuestionChoice(id=2, questionid_id=1, text='複雑な構文'),
        QuestionChoice(id=3, questionid_id=1, text='難しい文法'),
        QuestionChoice(id=4, questionid_id=2, text='ファイル集合'),
        QuestionChoice(id=5, questionid_id=2, text='データ管理システム'),
        QuestionChoice(id=6, questionid_id=2, text='プログラム言語'),
        QuestionChoice(id=7, questionid_id=3, text='データ格納場所'),
        QuestionChoice(id=8, questionid_id=3, text='プログラム名'),
        QuestionChoice(id=9, questionid_id=3, text='実行ファイル'),
    ]
    QuestionChoice.objects.bulk_create(choices)

def remove_initial_data(apps, schema_editor):
    User = apps.get_model('app', 'User')
    Test = apps.get_model('app', 'Test')
    Question = apps.get_model('app', 'Question')
    QuestionChoice = apps.get_model('app', 'QuestionChoice')

    QuestionChoice.objects.all().delete()
    Question.objects.all().delete()
    Test.objects.all().delete()
    User.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data, remove_initial_data),
    ] 
    