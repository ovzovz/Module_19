from django.contrib import admin
from .models import Game, Buyer,News, Test

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title',)
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    #readonly_fields = ('balance',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date',)
    search_fields = ('title',)
    list_per_page = 30

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 10

