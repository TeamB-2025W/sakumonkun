# sakumonkun

Docker環境構築
https://zenn.dev/ramu_k/articles/20240401-docker-django-setting-up


## ローカル環境構築手順

``` shell
# システムパッケージをインストール（Django + MySQL環境用）
apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# プロジェクトディレクトリに仮装環境を作成
cd sakumonkun
python -m venv .

source bin/activate  # Unix/Mac
.\Scripts\activate   # Windows

# Django環境の依存関係をインストール
pip install -r requirements.txt
```

# PEP 8: Python 命名規則

Python の公式スタイルガイドラインに基づいた命名規則を表形式で整理。

| 項目 | 形式 | 例 | 注意点 |
|------|------|----|--------|
| クラス名 | パスカルケース | `MyClass`, `CustomerOrder` | 主にオブジェクトの定義に使用。関数のように使用する場合は関数の命名規則に従う。 |
| 型変数名 | 単一の大文字 or パスカルケース | `T`, `AnyStr`, `Num`, `VT_co` | 共変・反変を示す場合は `_co`, `_contra` を付ける。 |
| 例外名 | パスカルケース（`Error` 接尾辞） | `IOError`, `CustomError` | 例外クラスは `Error` で終わるようにする。 |
| グローバル変数名 | 小文字スネークケース | `_internal_variable`, `global_value` | 非公開変数は `_` を先頭に付ける。 |
| 関数名・変数名 | 小文字スネークケース | `calculate_area`, `user_name` | 一般的に関数や変数はスネークケースを用いる。 |
| 関数・メソッドの引数 | `self` (インスタンスメソッド), `cls` (クラスメソッド) | `def method(self):`, `def class_method(cls):` | 予約語と衝突する場合は `_` を末尾に付ける（例: `class_`）。 |
| メソッド名・インスタンス変数 | 小文字スネークケース | `_private_method`, `__mangled_variable` | 非公開メソッドは `_` を1つ、名前マングリング用は `__` を先頭に付ける。 |
| 定数 | 大文字スネークケース | `MAX_LENGTH`, `DEFAULT_TIMEOUT` | モジュールレベルで定義し、全て大文字にする。 |
| 継承時の設計 | 明確にパブリック・非パブリックを分ける | `class Base: __private_var = 42` | 非公開属性には `__` を付け、サブクラスとの競合を防ぐ。 |
| パブリック/内部インターフェース | `__all__` で定義 | `__all__ = ['public_function', 'PublicClass']` | 内部関数には `_` を付け、モジュールのエクスポートを制御する。 |
| 避けるべき名前 | 組み込み関数名と衝突しないようにする | `user_list`, `string_value` | `list`, `str` などの組み込み関数名は避ける。 |
| ASCII 互換性 | ASCII 文字のみを使用 | `valid_name`, `function_name` | 国際化が必要な場合は明示的に対応を考慮する。 |
| プロジェクト固有の命名規則 | 一貫性のあるプレフィックス/サフィックスを導入 | `db_connector`, `ui_component` | `db_`, `ui_` などのプレフィックスを利用する。 |
