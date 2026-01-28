# Основные команды Alembic

Краткий и практичный справочник по основным командам Alembic.

## Инициализация проекта
```
alembic init alembic                          # обычная (синхронная) инициализация
```
```
alembic init -t async alembic                 # асинхронная версия (рекомендуется)
```
## Создание миграций
```
alembic revision -m "create users table"                            # пустая миграция вручную
```
```
alembic revision --autogenerate -m "add user last_login column"     # автогенерация по моделям
```
```
alembic revision --autogenerate --sql -m "..."                      # посмотреть SQL без создания файла
```
```
alembic revision --head-only -m "mark new head"                     # только новая версия без операций
```

## Применение миграций (upgrade)
```
alembic upgrade head                      # до последней версии
```
```
alembic upgrade head --sql                # показать SQL, который будет выполнен (без применения)
```
```
alembic upgrade +1                        # применить только следующую миграцию
```
```
alembic upgrade +3                        # применить следующие 3 миграции
```
```
alembic upgrade 3f2a1d4c9e2b              # до конкретной ревизии
```

## Откат миграций (downgrade)
```
alembic downgrade -1                      # откатить последнюю миграцию
```
```
alembic downgrade -3                      # откатить на 3 миграции назад
```
```
alembic downgrade base                    # откатить всё до начального состояния
```
```
alembic downgrade 1a2b3c4d5e6f            # откатить до конкретной ревизии
```
## Информационные команды
```
alembic current                           # текущая версия базы
```
```
alembic current --verbose                 # текущая + дополнительные данные
```
```
alembic heads                             # показать голову/головы (branches)
```
```
alembic history                           # вся история миграций
```
```
alembic history -r :head                  # от base до head
```
```
alembic history --verbose                 # история с подробностями (включая down revision)
```
```
alembic show 3f2a1d4c9e2b                 # посмотреть содержимое конкретной миграции
```
```
alembic stamp head                        # пометить БД как head (без выполнения SQL)
```
```
alembic stamp 3f2a1d4c9e2b                # пометить БД как конкретную ревизию
```


## Полезные комбинации (самые частые сценарии)
# 1. Стандартный цикл разработки
```
alembic revision --autogenerate -m "added payment_status"
```
```
alembic upgrade head
```

# 2. Посмотреть, что изменится
```
alembic upgrade head --sql
```
# 3. Откат + исправление
```
alembic downgrade -1
```
```
alembic revision --autogenerate -m "fix previous migration"
```
# 4. Сброс до начала (осторожно!)
```
alembic downgrade base
```
```
alembic stamp base        # если нужно просто пометить без отката
```
Удачи с миграциями!
