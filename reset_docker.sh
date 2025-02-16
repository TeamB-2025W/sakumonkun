#!/bin/bash

# すべてのコンテナを停止して削除
echo "Stopping and removing all containers..."
docker container stop $(docker container ls -aq) 2>/dev/null
docker container rm $(docker container ls -aq) 2>/dev/null

# すべてのイメージを削除
echo "Removing all Docker images..."
docker image rm $(docker image ls -aq) 2>/dev/null

# すべてのビルドキャッシュを削除
echo "Removing all Docker build cache..."
docker builder prune -af

# 不要なDockerデータを削除
echo "Running docker system prune..."
docker system prune -af

# Docker Compose ビルド（キャッシュなし）
echo "Building Docker Compose services with no cache..."
docker compose build --no-cache

# Docker Compose 起動
echo "Starting Docker Compose services..."
docker compose up
