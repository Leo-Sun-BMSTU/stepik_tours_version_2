import random
import data
from django.shortcuts import render


def main_view(request):
    '''
    Представление для главной страницы
    :param request:
    :return:
    '''
    return render(request, 'index.html', context={'title': data.title,
                                                  'subtitle': data.subtitle,
                                                  'description': data.description,
                                                  'departures': data.departures,
                                                  'tours': dict(random.sample(data.tours.items(), 6))})


def departure_view(request, departure: str):
    '''
    Представление для страницы направления
    :param request:
    :return:
    '''
    return render(request, 'departure.html', context={'title': data.title,
                                                      'subtitle': data.subtitle,
                                                      'description': data.description,
                                                      'departures': data.departures,
                                                      'tours': departure_filter(data.tours, departure),
                                                      'current_departure': departure,
                                                      'from_city': data.departures.get(departure),
                                                      'tour_count': len(departure_filter(data.tours, departure)),
                                                      'min_price': min([tour.get('price') for key, tour in
                                                                    departure_filter(data.tours, departure).items()]),
                                                      'max_price': max([tour.get('price') for key, tour in
                                                                    departure_filter(data.tours, departure).items()]),
                                                      })


def departure_filter(input_data: dict, departure: str) -> dict:
    '''
    Фильтрация по направлениям
    :param input_data: dict
    :param departure: str - город вылета
    :return: dict
    '''
    result = {key: val for key, val in input_data.items() if val.get('departure') == departure}
    return result


def tour_view(request, id: int):
    '''
    Представление для страницы тура
    :param request:
    :return:
    '''
    return render(request, 'tour.html', context={'choisen_tour': data.tours.get(id),
                                                 'departures': data.departures,
                                                 'title': data.title})
