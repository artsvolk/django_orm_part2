# Проект "Школа" — Миграции

## Описание
Проект демонстрирует замену связи «один ко многим» между моделями `Student` и `Teacher` на связь «многие ко многим» с использованием `ManyToManyField`.

Теперь у одного ученика может быть несколько учителей, а у одного учителя — несколько учеников.

## Требования
- Python 3.13
- PostgreSQL 18

## Установка и запуск

1. **Создайте виртуальное окружение**:
   ```bash
   python -m venv .venv
   ```

2. **Активируйте виртуальное окружение**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте подключение к базе данных**:
   - Создайте файл `website/settings_local.py` (пример ниже).
   - Убедитесь, что в PostgreSQL создана база данных `school`.

5. 5. **Пример `settings_local.py`**:
   ```python
   # orm_migrations/website/settings_local.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'school',
           'USER': 'postgres',
           'PASSWORD': 'ваш_пароль_от_postgresql',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```

6. **Выполните миграции**:
   ```bash
   python manage.py migrate
   ```

7. **Создайте суперпользователя (опционально, для админки)**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```

9. **Откройте в браузере**:
   - Список учеников: http://127.0.0.1:8000/
   - Админка: http://127.0.0.1:8000/admin

## Особенности реализации
- Связь между `Student` и `Teacher` реализована через `ManyToManyField`.
- В шаблоне используется вложенный цикл для отображения всех учителей ученика.
- Для оптимизации запросов используется `prefetch_related`, чтобы избежать проблемы N+1.
- Данные создаются вручную через админку (так как исходные данные `school.json` несовместимы с новой структурой модели).
```