# Проект "Новостной сайт" — M2M-связи

## Описание
Проект демонстрирует работу с отношением **«многие ко многим»** между моделями `Article` (статья) и `Tag` (тег) через промежуточную модель `Scope`.

Каждая статья может иметь несколько тематических тегов, при этом **один из них должен быть основным**.  
На главной странице теги отображаются в следующем порядке:
- сначала — **основной тег** (если указан),
- затем — остальные теги в **алфавитном порядке**.

В админке реализована возможность:
- создавать теги,
- назначать теги статьям,
- указывать один и только один основной тег (с валидацией).

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
   - Убедитесь, что в PostgreSQL создана база данных `netology_m2m_relations`.

5. **Пример `settings_local.py`**:
   ```python
   # m2m-relations/website/settings_local.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'netology_m2m_relations',
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

7. **Загрузите тестовые данные**:
   ```bash
   python manage.py loaddata articles.json
   ```

8. **Создайте суперпользователя (опционально, для админки)**:
   ```bash
   python manage.py createsuperuser
   ```

9. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```

10. **Откройте в браузере**:
    - Главная страница: http://127.0.0.1:8000/
    - Админка: http://127.0.0.1:8000/admin

## Особенности реализации
- Связь между `Article` и `Tag` реализована через `ManyToManyField` с параметром `through='Scope'`.
- Промежуточная модель `Scope` содержит поле `is_main`, определяющее, является ли тег основным.
- В представлении (`views.py`) используется `Prefetch` с `to_attr='ordered_scopes'` для корректной сортировки тегов **без вызова методов в шаблоне**.
- В шаблоне `news.html` итерация происходит по `article.ordered_scopes`, а не по `article.scopes`, чтобы избежать ошибки `'RelatedManager' object is not iterable`.
- В админке используется `TabularInline` с кастомным `BaseInlineFormSet` для валидации: **ровно один тег должен быть основным**.
- Все запросы оптимизированы: используются `prefetch_related` и `select_related` для предотвращения N+1.

---