from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import  *
from .forms import UserRegister
from django.core.paginator import Paginator

def start(request):
    title = 'Главная страница'
    context = {'title':title}
    return render(request, 'platform.html', context)

def get_catalog(request):
    title = 'Каталог игр'
    context = {'title':title, 'games':Game.objects.all()}
    return render(request, 'catalog.html', context)

class ClassCart(TemplateView):
    template_name = 'cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Корзина"
        return context


users = Buyer.objects.all()
info = {}
def info_set(username, password, repeat_password, age):
    if password != repeat_password:
        info['error'] = 'Пароли не совпадают'
    if int(age)<18:
        info['error'] ='Вы должны быть старше 18'
    if username in [user.name for user in Buyer.objects.all()]:
        info['error'] = 'Пользователь уже существует'
    if not info:
        info['new_user'] = username
    return

def sign_up_by_django(request):
    info.clear()
    if request.method == 'POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            repeat_password=form.cleaned_data['repeat_password']
            age=form.cleaned_data['age']
            info_set(username, password, repeat_password, age)
            if not 'error' in info:
               Buyer.objects.create(name=username, balance=0, age=age)
    else:
        form=UserRegister()
    info["form"]=form
    return render(request, 'registration_page.html', context=info)

def sign_up_by_html(request):
    info.clear()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        age=request.POST.get('age')
        info_set(username, password, repeat_password, age)
        return render(request, 'registration_page.html', context=info)
    return render(request, 'registration_page.html')

def news(request):
    all_news=News.objects.all()
    paginator=Paginator(all_news,3)
    page_number=request.GET.get('page')
    news=paginator.get_page(page_number)
    return render(request,'news.html', {'news':news})


