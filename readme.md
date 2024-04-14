1- Activate the venv 

``` bash
source .venv/Scripts/activate
```

2- create a new app

``` bash
 py manage.py startapp posts
```

3- start the server

``` bash
 py manage.py runserver
```

4- apply migrations

``` bash
 py manage.py migrate
```
5- make custom migrations

``` bash
 py manage.py makemigrations
```



--- 
In order to use the admin panel u have to create a super user for django which can be done by:

- run the command in the main project directory

```python
py manage.py createsuperuser
```

```go through the process remeber the password needs to be at least 8 chars longs and not too common and dont forget it```

