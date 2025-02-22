"""
import について
ModelBackend    : Djangoのデフォルト認証バックエンドを継承する。
get_user_model  : Userモデルを取得する。UserModel = get_user_model()
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrUsernameModelBackend(ModelBackend):
    """
    メールアドレスまたはユーザー名でログインできるカスタム認証バックエンド
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        認証メソッド
        Args:
            request: HTTPリクエスト
            username: メールアドレスまたはユーザー名
            password: パスワード
            **kwargs: 追加の引数
        Returns:
            認証成功時: Userオブジェクト
            認証失敗時: None
        """
        # まずメールアドレスでユーザーを検索
        try:
            user = UserModel.objects.filter(email=username).first()
        except UserModel.DoesNotExist:
            # メールアドレスが見つからない場合、ユーザー名で検索
            try:
                user = UserModel.objects.filter(username=username).first()
            except UserModel.DoesNotExist:
                return None

        # パスワードチェックと認証可能状態の確認
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None