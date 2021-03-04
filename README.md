# Catálogo de exploración de cursos
​
Catálogo que permite explorar cursos utilizando filtros y paginación, mostrando la información de los cursos y poder realizar la compra del curso.
​
### Características
​
- Fueron utilizados Django + DjangoRestFramework 
- Python3.8.8 
​
​
### How to run the project for development
- Create yout virtual environment
​
```python3 -m venv venv```
​
- Active your virtual environment
​
```source venv/bin/activate```
​
- Install requirements
​
```pip install -r requirements.txt```
​  
- Configure Database in settings files, uncomment lines from 87 to 94  and comment 95 to 97

- Run migrations
​
```python manage.py migrate```
  
- Run project
​
```python manage.py runserver```