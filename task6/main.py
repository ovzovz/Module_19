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


#os.system('pip install psycopg2-binary')
#os.chdir('UrbanDjango')
#os.system('python manage.py makemigrations')
#os.system("python manage.py migrate")


"""

from task1.models import Buyer
# Запрос на получение всех объектов базы данных 
buyers=Buyer.objects.all()
for buyer in buyers:
           print (buyer.id, buyer.name, buyer.balance, buyer.age)

# и конкретного по id
buyer=Buyer.objects.get(id=3)
print (buyer.name, buyer.balance, buyer.age)

#Запрос на фильтрацию
buyers=Buyer.objects.filter(balance__gt=100)
for buyer in buyers:
    print (buyer.name, buyer.balance)
    
#Запрос на добавление объекта
Buyer.objects.create(name='Buyer+', balance=123.45, age=77)

#Запрос на подсчет количества объектов(len()) с фильтрацией
Buyer.objects.filter(age__lt=50).count()


"""
