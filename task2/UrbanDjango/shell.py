"""
from task1.models import Buyer, Game
Buyer.objects.create(name='buyer1',balance=5.07,age=17)
Buyer.objects.create(name='buyer2',balance=51.07,age=20)
Buyer.objects.create(name='buyer3',balance=15,age=30)

Game.objects.create(title='game1',cost=31, size=10, description='game1', age_limited=True)
Game.objects.create(title='game2',cost=5, size=12, description='game2', age_limited=False)
Game.objects.create(title='game3',cost=12, size=36.6, description='game3', age_limited=True)

Game.objects.get(id=1).buyer.set((2,3))
Game.objects.get(id=2).buyer.set((1,3))
Game.objects.get(id=3).buyer.set((3,))
Game.objects.get(id=2).buyer.set((2,))
"""