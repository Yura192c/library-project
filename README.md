# library-project
Тестовое задание для компании LikeSoft


# Запуск проекта с docker
Перед запуском отредактируйте файл ***.evn.example***
1) Переименуйте файл на **.env**
2) Заполните данные для отправки эл. сообщений (**EMAIL_HOST_USER** и **EMAIL_HOST_PASSWORD**)

<br>***Запуск приложения***
```
docker-compose up --build
```

Далее создайте суперпользователя (если в этом есть надобность)
```
docker-compose exec app python manage.py createsuperuser
```

# API
После запуска проекта API будет доступно по адресу
<br>http://127.0.0.1:8000/docs/ либо 
<br>http://127.0.0.1:8000/redoc

