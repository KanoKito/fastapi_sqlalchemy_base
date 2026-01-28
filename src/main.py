# src/main.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from loguru import logger
from api.fastapi_app import get_fastapi_app
from core.config import BASE_DIR, settings


def configure_logger() -> None:
    """Настройка логгера Loguru."""
    logger.remove()
    logger.add(
        BASE_DIR / 'log/fasql.log',
        rotation='100 MB',
        retention=10,
        format='{time:DD-MM-YYYY HH:mm:ss} {level} {module} {function} {message}',
        level='INFO',
        enqueue=True,
        colorize=True,
    )
    logger.add(
        sys.stdout,
        format='<g>{time:DD-MM-YYYY HH:mm:ss}</g> <b>{level}</b> {module} {function} {message}',
        level='INFO',
        enqueue=True,
        colorize=True,
    )


# Важно: приложение создаётся на уровне модуля
app = get_fastapi_app()

if __name__ == '__main__':
    configure_logger()
    logger.info("Запуск приложения через if __name__ == '__main__'")
    # Можно оставить для ручного запуска python src/main.py
    import uvicorn

    uvicorn.run(
        'src.main:app',
        host='0.0.0.0',
        port=settings.app_port,
        reload=True,
    )
