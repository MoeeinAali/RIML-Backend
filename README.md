# RIML Backend

## How to run project?

### development mode

1. clone the project
2. create new virtual env
```
python -m venv venv
```
3. active env
```
on windows:
./venv/source/activate

on linux:
source venv 
```
4. install requirements
```
pip install -r requirements.txt
```

5. create `.env` file like `.env.example`
6. set `MODE="DEVELOPMENT"` in `.env` file
7. migrate database:
```
python manage.py migrate
```
8. create new superuser
```
python manage.py createsuperuser
```
9. run project
```
python mange.py runserver
```
