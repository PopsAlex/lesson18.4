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
    list_punkt1 = 'Atomic Heart'
    list_punkt2 = 'Cyberpunk 2077'
    list_punkt3 = 'PayDay 2'
    button1 = 'Купить'
    button2 = 'Вернуться обратно'
    context = {
        'title': title,
        'list_punkt1': list_punkt1,
        'list_punkt2': list_punkt2,
        'list_punkt3': list_punkt3,
        'button1': button1,
        'button2': button2,
    }
    return render(request, 'games.html', context)

def cart(request):
    title1 = 'Корзина'
    title2 = 'Извините, ваша корзина пуста'
    button = 'Вернуться обратно'
    context = {
        'title1': title1,
        'title2': title2,
        'button': button,
    }
    return render(request, 'cart.html', context)