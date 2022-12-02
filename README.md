## Тестовое задание для ORBIS

Тестовый проект по использованию фреймворка Flask

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Установка и запуск:
 - Клонируйте репозиторий на свою локальную машину и перейдите в директорию проекта:
```sh
git clone https://github.com/aimerkz/flaskProject.git
cd flaskProject
```
 - Создайте файл .env, скопировав в него содержимое
из env.example
 - Запустите команду docker:
```sh
docker-compose up -d
```
- Выполните миграции:
```sh
docker-compose exec web flask db init
docker-compose exec web flask db migrate
docker-compose exec web flask db upgrade
```
- Загрузите файл: \
[FileUploadForm](http://0.0.0.0:5000/api/files/upload/upload_form/)

:open_file_folder: Документация к API проекта: \
[Swagger UI](http://0.0.0.0:5000/api/swagger/)
