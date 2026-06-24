#!/bin/bash
# compose 파일 문법/설정 검증 (Docker 데몬 없이도 동작)
# 실행: bash check.sh
if ! command -v docker >/dev/null; then
  echo "⚠️  docker가 설치되어 있지 않습니다. 설치 후 다시 시도하세요."
  exit 1
fi
if docker compose config >/dev/null 2>&1; then
  echo "✅ docker-compose.yml 유효 — 설정 파싱 통과!"
else
  echo "❌ 설정 오류:"
  docker compose config 2>&1 | head -20
  exit 1
fi
