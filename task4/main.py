import os
###os.system('python -m venv venv')
#os.system('source .venv/bin/activate')
#os.system('pip install django')
#os.system('python.exe -m pip install --upgrade pip')
#os.system('django-admin startproject UrbanDjango')
#os.chdir('UrbanDjango')
#print(os.getcwd())
#os.system('python manage.py startapp task1')
#os.system("pip freeze > requirements.txt")

#os.chdir('UrbanDjango')
#os.system("python manage.py migrate")
#os.system('python manage.py makemigrations')
#os.system("python manage.py migrate")
#os.system("python manage.py shell")


# без терминала create_superuser
#os.system("python manage.py shell")
# в shell:
#from django.contrib.auth.models import User
#User.objects.create_superuser(username='admin', password='123')


if __name__=='__main__':
    os.chdir('UrbanDjango')
    os.system('python manage.py runserver')



#from django.contrib.auth.models import User
#User.objects.create_superuser(username='admin', password='123')