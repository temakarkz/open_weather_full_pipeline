ENV=${1:-local}


case $ENV in
  local)
    ENV_FILE=".env.local"
    COMPOSE_FILE="docker-compose.local.yml"
    ;;
  stage)
    ENV_FILE=".env.stage"
    COMPOSE_FILE="docker-compose.stage.yml"
    ;;
  prod)
    ENV_FILE=".env.prod"
    COMPOSE_FILE="docker-compose.prod.yml"
    ;;
  *)
    echo "Неизвестное окружение: $ENV"
    echo "Используй: ./run.sh [local|stage|prod]"
    exit 1
    ;;
esac

echo "Запуск окружения: $ENV"
echo "Используем env-файл: $ENV_FILE"
echo "Используем compose-файл: $COMPOSE_FILE"

docker compose -f $COMPOSE_FILE --env-file $ENV_FILE up -d

