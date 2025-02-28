#!/bin/bash

# スクリプトの実行ディレクトリを取得
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"
echo "Current directory: $(pwd)"

# MySQLでDBを削除・作成（警告を回避）
# DBにScriptで接続できない設定があるっぽい

# MySQLのパスワードを環境変数に設定
export MYSQL_PWD="root"

echo "Dropping and recreating database..."
docker-compose exec -T db mysql -u root -e "DROP DATABASE IF EXISTS sakumon_db; CREATE DATABASE sakumon_db;"

# MySQLの準備ができるまで待機
sleep 3

# マイグレーションファイルの削除
echo "Removing migration files..."
rm -rf ../project/app/migrations/*
mkdir -p ../project/app/migrations
touch ../project/app/migrations/__init__.py  # migrationsディレクトリをDjangoが認識できるようにする

# Djangoマイグレーション
echo "Applying migrations..."
cd ..  # プロジェクトのルートディレクトリに移動
docker-compose exec web python manage.py makemigrations app

# 既存のデータ移動
echo "Moving initial data migration files..."
if [ -f "${SCRIPT_DIR}/0002_create_superuser.py" ] && [ -f "${SCRIPT_DIR}/0003_initial_data.py" ]; then
    echo "Found migration files, copying..."
    cp "${SCRIPT_DIR}/0002_create_superuser.py" project/app/migrations/0002_create_superuser.py
    cp "${SCRIPT_DIR}/0003_initial_data.py" project/app/migrations/0003_initial_data.py
else
    echo "Error: Migration files not found in ${SCRIPT_DIR}"
    echo "Required files:"
    echo "- ${SCRIPT_DIR}/0002_create_superuser.py"
    echo "- ${SCRIPT_DIR}/0003_initial_data.py"
    exit 1
fi

# Djangoの準備ができるまで少し待つ
sleep 2

docker-compose exec web python manage.py migrate

# マイグレーションの適用状況を表示
echo "Current migrations for app:"
docker-compose exec web python manage.py showmigrations app | tee /dev/tty

echo "Database reset and migration complete!"