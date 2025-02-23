from django.db import migrations
from django.utils import timezone
from django.contrib.auth.hashers import make_password

def create_initial_data(apps, schema_editor):
    User = apps.get_model('app', 'User')
    Test = apps.get_model('app', 'Test')
    Question = apps.get_model('app', 'Question')
    QuestionChoice = apps.get_model('app', 'QuestionChoice')
    Examination = apps.get_model('app', 'Examination')
    Answer = apps.get_model('app', 'Answer')
    

    # ユーザーデータ
    users = [
        User(
            id=2,
            username='佐藤健一',
            email='test1@example.com',
            password=make_password('password123'),
            is_superuser=False,
            is_staff=False,
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        User(
            id=3,
            username='田中美咲',
            email='test2@example.com',
            password=make_password('password456'),
            is_superuser=False,
            is_staff=False,
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        User(
            id=4,
            username='山田太郎',
            email='test3@example.com',
            password=make_password('password789'),
            is_superuser=False,
            is_staff=False,
            is_active=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    User.objects.bulk_create(users)

    # テストデータ
    tests = [
        Test(
            id=1,
            userid_id=2,
            title='基本情報技術者試験模擬テスト',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Test(
            id=2,
            userid_id=4,
            title='Python基礎テスト',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Test(
            id=3,
            userid_id=2,
            title='データベース基礎テスト',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Test(
            id=4,
            userid_id=3,
            title='ネットワーク基礎テスト',
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
            correct_choiceid=4,
            text='データベースとは？',
            explanation='データを効率的に管理するシステム',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=3,
            testid_id=2,
            correct_choiceid=6,
            text='変数とは？',
            explanation='データを格納する箱のようなもの',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=4,
            testid_id=2,
            correct_choiceid=10,
            text='オブジェクト指向とは？',
            explanation='データと処理を一つのオブジェクトとしてまとめる考え方',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=5,
            testid_id=3,
            correct_choiceid=13,
            text='SQLの基本コマンドは？',
            explanation='SELECT, INSERT, UPDATE, DELETEが基本',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=6,
            testid_id=4,
            correct_choiceid=16,
            text='TCPとUDPの違いは？',
            explanation='TCPは信頼性重視、UDPは速度重視',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=7,
            testid_id=1,
            correct_choiceid=19,
            text='ソフトウェアテストとは？',
            explanation='プログラムの品質を確認する作業',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=8,
            testid_id=1,
            correct_choiceid=22,
            text='アジャイル開発とは？',
            explanation='短期間の反復による開発手法',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=9,
            testid_id=2,
            correct_choiceid=25,
            text='Pythonのリストとは？',
            explanation='順序付けられたデータの集合',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=10,
            testid_id=2,
            correct_choiceid=28,
            text='デコレータとは？',
            explanation='関数やクラスの機能を拡張する機能',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=11,
            testid_id=3,
            correct_choiceid=31,
            text='トランザクションとは？',
            explanation='データベースの一連の処理単位',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=12,
            testid_id=3,
            correct_choiceid=34,
            text='インデックスの役割は？',
            explanation='データベースの検索を高速化する',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=13,
            testid_id=4,
            correct_choiceid=37,
            text='IPアドレスとは？',
            explanation='ネットワーク上の機器を識別する番号',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Question(
            id=14,
            testid_id=4,
            correct_choiceid=40,
            text='HTTPとHTTPSの違いは？',
            explanation='暗号化の有無による安全性の違い',
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    Question.objects.bulk_create(questions)

    # 選択肢データを2-4個にランダム化
    choices = [
        # 問題1の選択肢（3つ）
        QuestionChoice(id=1, questionid_id=1, text='読みやすい構文'),
        QuestionChoice(id=2, questionid_id=1, text='複雑な構文'),
        QuestionChoice(id=3, questionid_id=1, text='難しい文法'),
        
        # 問題2の選択肢（2つ）
        QuestionChoice(id=4, questionid_id=2, text='データ管理システム'),
        QuestionChoice(id=5, questionid_id=2, text='プログラム言語'),
        
        # 問題3の選択肢（4つ）
        QuestionChoice(id=6, questionid_id=3, text='データ格納場所'),
        QuestionChoice(id=7, questionid_id=3, text='プログラム名'),
        QuestionChoice(id=8, questionid_id=3, text='実行ファイル'),
        QuestionChoice(id=9, questionid_id=3, text='変数の型'),
        
        # 問題4の選択肢（3つ）
        QuestionChoice(id=10, questionid_id=4, text='データと処理をまとめる'),
        QuestionChoice(id=11, questionid_id=4, text='データのみを扱う'),
        QuestionChoice(id=12, questionid_id=4, text='処理のみを扱う'),
        
        # 問題5の選択肢（2つ）
        QuestionChoice(id=13, questionid_id=5, text='SELECT, INSERT等'),
        QuestionChoice(id=14, questionid_id=5, text='PRINT, SCAN等'),
        
        # 問題6の選択肢（4つ）
        QuestionChoice(id=15, questionid_id=6, text='信頼性と速度の違い'),
        QuestionChoice(id=16, questionid_id=6, text='使用ポートの違い'),
        QuestionChoice(id=17, questionid_id=6, text='実装言語の違い'),
        QuestionChoice(id=18, questionid_id=6, text='開発者の違い'),
        
        # 問題7の選択肢（3つ）
        QuestionChoice(id=19, questionid_id=7, text='品質確認作業'),
        QuestionChoice(id=20, questionid_id=7, text='プログラミング作業'),
        QuestionChoice(id=21, questionid_id=7, text='文書作成作業'),
        
        # 問題8の選択肢（2つ）
        QuestionChoice(id=22, questionid_id=8, text='反復的な開発手法'),
        QuestionChoice(id=23, questionid_id=8, text='一括開発手法'),
        
        # 問題9の選択肢（4つ）
        QuestionChoice(id=24, questionid_id=9, text='順序付きデータ集合'),
        QuestionChoice(id=25, questionid_id=9, text='単一データ型'),
        QuestionChoice(id=26, questionid_id=9, text='関数の集まり'),
        QuestionChoice(id=27, questionid_id=9, text='クラスの定義'),
        
        # 問題10の選択肢（3つ）
        QuestionChoice(id=28, questionid_id=10, text='機能拡張する仕組み'),
        QuestionChoice(id=29, questionid_id=10, text='データの保存方法'),
        QuestionChoice(id=30, questionid_id=10, text='画面装飾の方法'),
        
        # 問題11の選択肢（2つ）
        QuestionChoice(id=31, questionid_id=11, text='処理の単位'),
        QuestionChoice(id=32, questionid_id=11, text='データの型'),
        
        # 問題12の選択肢（4つ）
        QuestionChoice(id=33, questionid_id=12, text='検索速度向上'),
        QuestionChoice(id=34, questionid_id=12, text='データ保存'),
        QuestionChoice(id=35, questionid_id=12, text='バックアップ'),
        QuestionChoice(id=36, questionid_id=12, text='データ圧縮'),
        
        # 問題13の選択肢（3つ）
        QuestionChoice(id=37, questionid_id=13, text='機器識別番号'),
        QuestionChoice(id=38, questionid_id=13, text='ソフトウェア名'),
        QuestionChoice(id=39, questionid_id=13, text='ユーザー名'),
        
        # 問題14の選択肢（2つ）
        QuestionChoice(id=40, questionid_id=14, text='暗号化の違い'),
        QuestionChoice(id=41, questionid_id=14, text='通信速度の違い'),
    ]
    QuestionChoice.objects.bulk_create(choices)
    
    # 受験データ
    examinations = [
        Examination(
            id=1,
            testid_id=1,
            guestname='ゲスト太郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=2,
            testid_id=1,
            guestname='ゲスト次郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=3,
            testid_id=2,
            guestname='ゲスト三郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=4,
            testid_id=2,
            guestname='ゲスト四郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=5,
            testid_id=3,
            guestname='ゲスト五郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=6,
            testid_id=3,
            guestname='ゲスト六郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Examination(
            id=7,
            testid_id=4,
            guestname='ゲスト七郎',
            answered_at=timezone.now(),
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    Examination.objects.bulk_create(examinations)

    # 回答データ
    answers = [
        # ゲスト太郎の回答（testid=1の全問題に回答）
        Answer(
            id=1,
            examinationid_id=1,
            questionid_id=1,
            selected_choiceid=1,  # 正解：読みやすい構文
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=2,
            examinationid_id=1,
            questionid_id=2,
            selected_choiceid=4,  # 正解：データ管理システム
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        # ゲスト次郎の回答（testid=1の全問題に回答、一部不正解）
        Answer(
            id=3,
            examinationid_id=2,
            questionid_id=1,
            selected_choiceid=2,  # 不正解：複雑な構文
            iscorrect=False,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=4,
            examinationid_id=2,
            questionid_id=2,
            selected_choiceid=4,  # 正解：データ管理システム
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        # ゲスト三郎の回答（testid=2の問題に回答）
        Answer(
            id=5,
            examinationid_id=3,
            questionid_id=3,
            selected_choiceid=6,  # 正解：データ格納場所
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=6,
            examinationid_id=4,
            questionid_id=4,
            selected_choiceid=10,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=7,
            examinationid_id=5,
            questionid_id=5,
            selected_choiceid=13,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=8,
            examinationid_id=6,
            questionid_id=11,
            selected_choiceid=31,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=9,
            examinationid_id=6,
            questionid_id=12,
            selected_choiceid=34,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=10,
            examinationid_id=7,
            questionid_id=13,
            selected_choiceid=37,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
        Answer(
            id=11,
            examinationid_id=7,
            questionid_id=14,
            selected_choiceid=40,
            iscorrect=True,
            created_at=timezone.now(),
            updated_at=timezone.now()
        ),
    ]
    Answer.objects.bulk_create(answers)

    
def remove_initial_data(apps, schema_editor):
    User = apps.get_model('app', 'User')
    Test = apps.get_model('app', 'Test')
    Question = apps.get_model('app', 'Question')
    QuestionChoice = apps.get_model('app', 'QuestionChoice')
    Examination = apps.get_model('app', 'Examination')
    Answer = apps.get_model('app', 'Answer')

    # 外部キー制約があるため、削除順序が重要
    Answer.objects.all().delete()
    Examination.objects.all().delete()
    QuestionChoice.objects.all().delete()
    Question.objects.all().delete()
    Test.objects.all().delete()
    User.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_create_superuser'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_data,
            reverse_code=remove_initial_data
        ),
    ] 
    