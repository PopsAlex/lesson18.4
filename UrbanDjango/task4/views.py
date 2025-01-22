from django.shortcuts import render

# Create your views here.
def platform(request):
    title = 'Главная'
    link1 = 'Главная'
    link2 = 'Магазин'
    link3 = 'Корзина'
    context = {
        'title': title,
        'link1': link1,
        'link2': link2,
        'link3': link3,
    }
    return render(request, 'platform.html', context)

def games(request):
    title = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    button1 = 'Купить'
    button2 = 'Вернуться обратно'
    context = {
        'title': title,
        'games': games,
        'button1': button1,
        'button2': button2,
    }
    return render(request, 'games.html', context)

def cart(request):
    title = 'Корзина'
    game = 'Извините, ваша корзина пуста'
    button = 'Вернуться обратно'
    context = {
        'title': title,
        'games': game,
        'button': button,
    }
    return render(request, 'cart.html', context)