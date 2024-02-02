# NotifService

### О проекте
Cервис управления рассылками API администрирования и получения статистики.

### В проекте используется:

![version](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![version](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![version](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![version](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)


### Перед началом работы:

#### Установка зависимостей:

В корневой папке находится файл с зависимостями requirements.txt
```shell
pip install poetry
```
```shell
poetry init
```


#### Настройка переменных окружения:

Для работы проекта необходимо создать **.env** в корневой папке.
В нем нужно указать необходимые значения переменных:

* SECRET_KEY = **секретный ключ**
* DEBUG = **True**
* DATABASE_URL = **psql://<имя пользователя>:<пароль пользователя>@<ip адрес>:<порт>/<имя базы>**
* REDIS_HOST = **хост Redis**
* REDIS_PORT = **порт Redis**

* PROBE_SERVER_TOKEN = **Токен Probe Server API**

* GOOGLE_OAUTH2_KEY = **Ключ  Google Oauth**
* GOOGLE_OAUTH2_SECRET = **Секрет для Google Oauth**

* EMAIL_HOST = **Емейл хост (пример : smtp.gmail.com)**
* EMAIL_PORT = **Емейл порт (пример : 587)**
* EMAIL_HOST_USER = **Пользователь Google**
* EMAIL_HOST_PASSWORD = **Пароль пользователя Google**
* RECIPIENT_EMAIL = **Емейл получателя статистики по сервису**




### Запуск проекта Django:

#### Docker:
* Разворачиваем docker контейнер с проектом, запустив файл docker-compose.yml.

```shell
docker compose up --build -d
```
#### Локально:
* Перед запуском проект локально требуется выполнить миграции на базу данных командой

```shell
python ./manage.py migrate
```
* Запуск проекта

```shell
python ./manage.py runserver
```


### Состав проекта:
* Swagger UI ``` localhost/docs``` (Формат интервала рассылки, при его наличии, описан)
* администраторский Web UI ``` localhost/admin``` тестовый аккаунт (admin@mail.com : test)
* Custom Google Oauth ``` localhost/auth/google``` (Требуется настроить env-переменные: GOOGLE_OAUTH2_KEY, GOOGLE_OAUTH2_SECRET)
* Custom Facebook Oauth ``` localhost/auth/facebook```
* Ежедневная отправка статистики по сервису (Требуется настроить все EMAIL* env-переменные )
* Prometheus метрики  ``` localhost/metrics``` 
* Prometheus service  ``` localhost:9090``` 
* Grafana service ``` localhost:3060```  (Вход: admin admin , Добавить Data sources http://prometheus:9090)
* Flower service ``` localhost:5555``` 
* Тесты ``` pytest --cov``` 
* Логи  ```app.log celery_beat.log celery_worker.log``` 