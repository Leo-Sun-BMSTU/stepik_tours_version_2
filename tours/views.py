from django.shortcuts import render


def main_view(request):
    '''
    Представление для главной страницы
    :param request:
    :return:
    '''
    return render(request, 'index.html')


def departure_view(request):
    '''
    Представление для страницы направления
    :param request:
    :return:
    '''
    return render(request, 'departure.html')


def tour_view(request):
    '''
    Представление для страницы тура
    :param request:
    :return:
    '''
    return render(request, 'tour.html')
