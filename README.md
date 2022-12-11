# A simple Blog Application that allows users to navigate through all published posts and read single posts
## What the app can do
### To the users:
- Navigate through all published posts and read single posts

### To the admin:
- Manage and publish posts
- Remove irrelevant comments

#### Commands
- pip install pipenv
- pipenv install django
- django-admin startproject mysite .
- python manage.py migrate
- python manage.py runserver
- python manage.py runserver 127.0.0.1:80001 --settings=mysite.settings
- code .
- pipenv --venv
- **virtualenvpath\bin\python**
- python
- python --version
- python -m django --version
- pipenv install python-dotenv
- python manage.py shell
- python manage.py sqlmigrate blog 0001
- python manage.py createsuperuser
- pip list
- pipenv install django-taggit==3.0.0
- pipenv install markdown==3.4.1
- pipenv install psycopg2-binary==2.9.3
- python -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json
- python manage.py loaddata mysite_data.json

- pipenv install gunicorn
- pip freeze > requirements.txt
- python --version
- pipenv install whitenoise
- python manage.py collectstatic
##### Querysets:
 <p>
    Post.objects.filter(publish__year__in=[2022, 2023]) <br>
    Post.objects.filter(publish__year__gte=2022) <br>
    Post.objects.filter(title__iendswith='Django') <br>
    import datetime <br>
    Post.objects.filter(publish__date=datetime.date(2022, 10, 20)) <br>
    Post.objects.filter(publish__year__range=(2022, 2023)) <br>
    User.objects.filter(first_name__isnull=True)   <br>
    Post.objects.filter(title__iregex=r'^(who|new) +')     <br>
    Post.objects.filter(publish__year=2022, author__username='admin') <br>
    Post.objects.filter(publish__year=2022).filter(author__username='admin') <br>
    Post.objects.filter(publish__year=2022).exclude(title__istartswith='why') <br>
    Post.objects.order_by('-title') <br>
    post = Post.objects.get(id=3) <br>
    post.delete() <br>
    user = User.objects.get(username='admin') <br>
    post = Post(title='', slug='', body='', author=admin) <br>
    post.save() <br>
    Post.objects.create()<br>
    To update: <br>
    post.title = '' <br>
 </p>

- user = Post.objects.get(id=1)
- user.status = Post.Status.DRAFT
- user.save()
- Post.published.all()


###### Notes
- Specify an app_name='appname' in app.urls.py then specify a namespace in project.urls.py
- To create a custom manager
   1. students = models.Manager(): it inherits everything from the object manager
   2. Student.students.all()
   - method 2
      1. Create a ModelManager inheriting from models.Manager and override get_queryset() by adding a filter()
      2. new_manager = ModelManager()
