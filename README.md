# Kittygram 🐱

**Kittygram** — это социальная сеть для обмена фотографиями любимых питомцев. Проект включает в себя:
- **Бэкенд-приложение** на Django для обработки данных и API.
- **Фронтенд-приложение** на React для удобного взаимодействия с пользователями.
- **Автоматизированный деплой** на удаленный сервер с использованием GitHub Actions.

## Возможности проекта

- **Публикация фотографий питомцев**: Пользователи могут загружать фотографии своих питомцев, добавлять описание и имена.
- **Просмотр ленты**: Возможность просматривать фотографии других пользователей.
- **Редактирование профиля**: Пользователи могут обновлять информацию о своих питомцах.
- **Автоматический деплой**: Проект автоматически развертывается на удаленном сервере при обновлении кода в репозитории.

## Технологический стек

### Бэкенд
- **Django**: Основной фреймворк для разработки API.
- **Django REST Framework (DRF)**: Для создания RESTful API.
- **PostgreSQL**: База данных для хранения информации о пользователях и питомцах.
- **Docker**: Для контейнеризации приложения.

### Фронтенд
- **React**: Библиотека для создания пользовательского интерфейса.
- **React Router**: Для навигации между страницами.
- **Axios**: Для взаимодействия с бэкендом через API.

### Инфраструктура
- **GitHub Actions**: Для автоматизации CI/CD (непрерывная интеграция и доставка).
- **Nginx**: Веб-сервер для раздачи статики и проксирования запросов.
- **Docker Compose**: Для управления многоконтейнерными приложениями.

## Установка и запуск

### Локальная разработка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш-username/kittygram.git
   cd kittygram
2. **Создайте и активируйте виртуальное окружение**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
3. **Примените миграции**:
   ```bash
   python manage.py migrate



## Деплой на удаленный сервер

### Настройте GitHub Actions:

1. **Добавьте секреты в репозиторий (Settings -> Secrets and variables -> Actions)**:
   ```bash
   SSH_PRIVATE_KEY: Приватный ключ для доступа к серверу.
   DOCKER_USERNAME: Логин от Docker Hub.
   DOCKER_PASSWORD: Пароль от Docker Hub.
   HOST: IP-адрес или домен сервера.
   USER: Имя пользователя на сервере.

2. **Настройте сервер**:
  - Установите Docker и Docker Compose.
  - Скопируйте файл docker-compose.production.yml на сервер.
  - Создайте и скопируйте файл .env на сервер
    ```bash
    POSTGRES_USER=...
    POSTGRES_PASSWORD=...
    POSTGRES_DB=...
    DB_NAME=...
    DB_HOST=...
    DB_PORT=...
    SECRET_KEY=...
    DEBUG=...

### Автоматический деплой:

При каждом пуше в ветку main GitHub Actions автоматически соберет и загрузит Docker-образы, а затем развернет проект на сервере.

## Структура проекта
- backend/: Директория с бэкенд-приложением на Django.
- frontend/: Директория с фронтенд-приложением на React.
- nginx/: Директория с файлами конфигурации gateway.
- tests/: Тесты pytest.
- .env.example: Пример оформления .env
- docker-compose.production.yml: Файл конфигурации docker для развертывания на сервере.
- docker-compose.yml: Файл конфигурации docker для развертывания локально.
- .gitignore: Исключения git.
- 
- .github/workflows/: Конфигурации GitHub Actions для CI/CD.

Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

Авторы
Ваше имя
